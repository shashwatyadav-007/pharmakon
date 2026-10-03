# Session 1: Deep Dive into FastAPI & `app/main.py`

This document provides a line-by-line, architectural walkthrough of the **PharmaKon** backend as implemented in `backend/app/main.py`, followed by a trace of the `GET /api/v1/products` request lifecycle.

---

## Part 1: Deep Dive into `backend/app/main.py`

Here is the structure and purpose of each component in [`backend/app/main.py`](file:///d:/PharmaKon/pharmakon/backend/app/main.py).

---

### 1. What `FastAPI()` Does

In [`app/main.py`](file:///d:/PharmaKon/pharmakon/backend/app/main.py#L28-L40):

```python
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="PharmaKon is a clean, modern pharmacy management and analytics backend API...",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)
```

`FastAPI()` creates the **master ASGI (Asynchronous Server Gateway Interface) web application instance**. 

When Uvicorn runs `uvicorn app.main:app --reload`, Uvicorn communicates directly with this `app` instance. Specifically, `FastAPI()`:
1. **Initializes the HTTP & WebSocket Router**: Creates the internal routing tree that maps incoming HTTP requests (method + URL path) to the appropriate Python endpoint functions.
2. **Generates the OpenAPI Schema**: Automatically inspects route signatures, type hints, docstrings, and Pydantic models to build an OpenAPI 3.1 JSON document at `/openapi.json`.
3. **Mounts Interactive Documentation**:
   - `docs_url="/docs"`: Renders Swagger UI.
   - `redoc_url="/redoc"`: Renders ReDoc.
4. **Registers Lifespan Management**: Hooks up startup and shutdown event handling.

---

### 2. What the `lifespan` Function Does

In [`app/main.py`](file:///d:/PharmaKon/pharmakon/backend/app/main.py#L20-L25):

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager that runs startup and shutdown tasks."""
    # Pre-populate sample in-memory data for development and testing
    seed_sample_data()
    yield
```

In modern FastAPI, `lifespan` uses Python's standard `asynccontextmanager` to control what happens **before the server starts receiving requests** and **after the server stops**.

- **Startup (Before `yield`)**: When Uvicorn boots up, FastAPI runs the code before `yield`. Here, it calls `seed_sample_data()` from `app.services.data_store`. This populates the in-memory dictionaries with 3 sample products (Paracetamol, Amoxicillin, Face Wash), 4 batches, and 1 supplier so the application is immediately testable and functional.
- **`yield`**: Pauses while the application is live and processing HTTP requests.
- **Shutdown (After `yield`)**: If code were placed after `yield` (such as closing database connection pools), it would run when the server shuts down.

*(Note: `lifespan` replaces the older deprecated `@app.on_event("startup")` and `@app.on_event("shutdown")` patterns).*

---

### 3. What Middleware is Being Used

In [`app/main.py`](file:///d:/PharmaKon/pharmakon/backend/app/main.py#L42-L49):

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**CORSMiddleware (Cross-Origin Resource Sharing)** is an HTTP security layer.
- **What problem it solves**: By default, web browsers block frontend web apps (e.g., React running on `http://localhost:5173`) from making HTTP requests to a backend on a different port or domain (`http://127.0.0.1:8000`).
- **How it works**: For every request, `CORSMiddleware` intercepts the request and adds standard HTTP headers (like `Access-Control-Allow-Origin: *` and `Access-Control-Allow-Methods: *`) to the HTTP response, allowing the browser to permit frontend communication with the backend.

---

### 4. What the Exception Handlers Do

In [`app/main.py`](file:///d:/PharmaKon/pharmakon/backend/app/main.py#L51-L79):

We registered three exception handlers to guarantee that **every error response follows the documented API envelope contract**:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "details": []
  }
}
```

#### A. Custom Business Error Handler (`AppError`)
```python
app.add_exception_handler(AppError, app_error_handler)
```
When business logic raises `AppError(code="DUPLICATE_CODE", message="...", status_code=400)`, `app_error_handler` catches it and returns a `JSONResponse` with status `400` matching the error envelope.

#### B. Request Validation Error Handler (`RequestValidationError`)
```python
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    details = []
    for err in exc.errors():
        location = " -> ".join(str(loc) for loc in err.get("loc", []))
        details.append(f"{location}: {err.get('msg', 'Validation error')}")

    content = error_response(
        code="VALIDATION_ERROR",
        message="Request validation failed. Please check your payload parameters.",
        details=details,
    )
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=content)
```
When a client submits invalid JSON (e.g., negative price, missing required fields, or invalid category), FastAPI's Pydantic validation automatically raises `RequestValidationError`. This handler catches it and formats it into the standard error envelope with status `422`.

#### C. General HTTP Error Handler (`HTTPException`)
```python
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    content = error_response(
        code="HTTP_ERROR",
        message=str(exc.detail),
    )
    return JSONResponse(status_code=exc.status_code, content=content)
```
Catches standard Starlette/FastAPI `HTTPException` and ensures it uses the same unified JSON structure.

---

### 5. How `APIRouter` is Registered

FastAPI avoids putting every endpoint into one giant file by using `APIRouter`.

1. In [`app/api/routes/products.py`](file:///d:/PharmaKon/pharmakon/backend/app/api/routes/products.py#L13), a mini-router is defined:
   ```python
   router = APIRouter(prefix="/products", tags=["Products"])
   ```
2. In [`app/main.py`](file:///d:/PharmaKon/pharmakon/backend/app/main.py#L11-L14), routers are imported:
   ```python
   from app.api.routes.auth import router as auth_router
   from app.api.routes.inventory import router as inventory_router
   from app.api.routes.products import router as products_router
   from app.api.routes.suppliers import router as suppliers_router
   ```
3. In [`app/main.py`](file:///d:/PharmaKon/pharmakon/backend/app/main.py#L115-L118), each router is mounted onto the main app:
   ```python
   app.include_router(auth_router, prefix=settings.API_V1_PREFIX)
   app.include_router(products_router, prefix=settings.API_V1_PREFIX)
   app.include_router(inventory_router, prefix=settings.API_V1_PREFIX)
   app.include_router(suppliers_router, prefix=settings.API_V1_PREFIX)
   ```

---

### 6. How `/api/v1` is Added to the Routes

The URL prefix concatenation works hierarchically:

1. Global Setting in [`app/core/config.py`](file:///d:/PharmaKon/pharmakon/backend/app/core/config.py#L6):
   ```python
   API_V1_PREFIX: str = "/api/v1"
   ```
2. Main App inclusion in [`app/main.py`](file:///d:/PharmaKon/pharmakon/backend/app/main.py#L116):
   ```python
   app.include_router(products_router, prefix="/api/v1")
   ```
3. Router definition in [`app/api/routes/products.py`](file:///d:/PharmaKon/pharmakon/backend/app/api/routes/products.py#L13):
   ```python
   router = APIRouter(prefix="/products")
   ```
4. Endpoint decorator in [`app/api/routes/products.py`](file:///d:/PharmaKon/pharmakon/backend/app/api/routes/products.py#L16):
   ```python
   @router.get("")  # or @router.get("/{id}")
   ```

FastAPI joins these paths:
$$\text{Base Prefix } (/api/v1) + \text{Router Prefix } (/products) + \text{Route Path } ("") = \mathbf{/api/v1/products}$$
$$\text{Base Prefix } (/api/v1) + \text{Router Prefix } (/products) + \text{Route Path } (/\{id\}) = \mathbf{/api/v1/products/\{id\}}$$

---

### 7. How `GET /health` Works

In [`app/main.py`](file:///d:/PharmaKon/pharmakon/backend/app/main.py#L101-L111):

```python
@app.get(
    "/health",
    summary="Health Check",
    description="Liveness probe returning application health status.",
    tags=["System"],
)
def health_check() -> dict[str, Any]:
    return success_response(
        data={"status": "healthy"},
        message="PharmaKon API is running smoothly",
    )
```

- `@app.get("/health")` registers a handler on the root path without the `/api/v1` prefix.
- It acts as a **liveness probe** (used by Docker, monitoring tools, or load balancers to check if the backend process is up).
- It calls `success_response(data={"status": "healthy"}, ...)` which formats the output into:
  ```json
  {
    "success": true,
    "data": {
      "status": "healthy"
    },
    "message": "PharmaKon API is running smoothly",
    "meta": null
  }
  ```

---

## Part 2: Tracing One Complete Request: `GET /api/v1/products`

Let us trace what happens when an HTTP client sends:
```http
GET /api/v1/products?query=Paracetamol&page=1&limit=20 HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json
```

```text
1. Client (Browser / Swagger / POS)
   │  Sends GET /api/v1/products?query=Paracetamol
   ▼
2. Uvicorn Server
   │  Receives raw TCP socket, parses HTTP headers & query string, passes ASGI scope
   ▼
3. FastAPI Application (backend/app/main.py: app)
   │  Checks CORSMiddleware
   │  Matches URL path "/api/v1/products" to products_router
   ▼
4. Products Router (backend/app/api/routes/products.py: list_products)
   │  Extracts and validates query parameters:
   │    query="Paracetamol", category=None, is_active=None, page=1, limit=20
   ▼
5. Service Layer (backend/app/services/product_service.py: get_all_products)
   │  Iterates over data_store.products.values()
   │  Filters by query string ("paracetamol" in name/code/barcode)
   │  Calculates total_stock for matching product by calling _calculate_total_stock()
   │  _calculate_total_stock() sums quantity of active batches in data_store.batches
   │  Applies pagination slice [0:20]
   │  Returns (paginated_items, total_count)
   ▼
6. Pydantic Serialization (backend/app/schemas/products.py: ProductResponse)
   │  Converts product dictionaries into ProductResponse models
   │  model_dump(mode="json") ensures UUIDs, Decimals, and Datetimes format properly
   ▼
7. Response Envelope Formatting (backend/app/core/responses.py: success_response)
   │  Wraps items in envelope: {"success": True, "data": [...], "message": "...", "meta": {...}}
   ▼
8. JSON Serialization & HTTP Response
   │  FastAPI serializes dict to JSON string and returns HTTP 200 OK
   ▼
9. Client Receives Response
```

---

### Step-by-Step Code Execution

#### Step 1: Route Matching & Parameter Extraction
In [`backend/app/api/routes/products.py`](file:///d:/PharmaKon/pharmakon/backend/app/api/routes/products.py#L22-L28):
```python
def list_products(
    query: str | None = Query(None, description="Search by name, SKU code, or barcode"),
    category: str | None = Query(None, description="Filter by category (Medicine, Surgical, Cosmetic, Baby, Food)"),
    is_active: bool | None = Query(None, description="Filter by active status"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(settings.DEFAULT_PAGE_SIZE, ge=1, le=settings.MAX_PAGE_SIZE, description="Items per page"),
) -> dict:
```
FastAPI automatically parses `query="Paracetamol"`, `page=1`, `limit=20` from the URL.

#### Step 2: Delegating to the Service Layer
In [`backend/app/api/routes/products.py`](file:///d:/PharmaKon/pharmakon/backend/app/api/routes/products.py#L29-L35):
```python
items, total = product_service.get_all_products(
    query=query,
    category=category,
    is_active=is_active,
    page=page,
    limit=limit,
)
```

#### Step 3: Business Logic & Stock Aggregation in Service
In [`backend/app/services/product_service.py`](file:///d:/PharmaKon/pharmakon/backend/app/services/product_service.py#L8-L41):
```python
def _calculate_total_stock(product_id: uuid.UUID) -> int:
    return sum(
        b["quantity"]
        for b in data_store.batches.values()
        if b["product_id"] == product_id and b.get("is_active", True)
    )

def get_all_products(...):
    filtered = []
    for product in data_store.products.values():
        # Searches name, code, barcode
        searchable = product["code"].lower() + " " + product["name"].lower()
        if "paracetamol" in searchable:
            item = product.copy()
            item["total_stock"] = _calculate_total_stock(product["id"]) # 8 + 25 = 33
            filtered.append(item)
    
    total_count = len(filtered)
    paginated = filtered[0:20]
    return paginated, total_count
```

#### Step 4: Schema Validation & Response Packaging
In [`backend/app/api/routes/products.py`](file:///d:/PharmaKon/pharmakon/backend/app/api/routes/products.py#L37-L44):
```python
validated_items = [ProductResponse(**item).model_dump(mode="json") for item in items]
meta = paginated_meta(page=page, limit=limit, total=total)

return success_response(
    data=validated_items,
    message="Products retrieved successfully",
    meta=meta,
)
```

#### Step 5: Final JSON Returned to Client
```json
{
  "success": true,
  "data": [
    {
      "id": "11111111-1111-1111-1111-111111111111",
      "code": "MED-PAR-500",
      "name": "Paracetamol 500mg",
      "category": "Medicine",
      "unit": "Strip",
      "mrp": "60.00",
      "default_purchase_price": "45.00",
      "barcode": "8901234567890",
      "reorder_level": 15,
      "is_active": true,
      "total_stock": 33,
      "created_at": "2026-10-04T02:30:00Z",
      "updated_at": "2026-10-04T02:30:00Z"
    }
  ],
  "message": "Products retrieved successfully",
  "meta": {
    "page": 1,
    "limit": 20,
    "total": 1
  }
}
```
