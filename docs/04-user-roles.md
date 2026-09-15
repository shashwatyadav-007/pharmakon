# 04 — User Roles

## 1. Document Purpose

This document defines the **users, responsibilities, and access model** for PharmaKon.

The client's confirmed requirement is intentionally simple: the initial system should **not create separate employee accounts**. A single account will provide the required operational access to manage stock and view analytics.

Therefore, this document does **not** introduce a detailed role-based access-control (RBAC) model that the client has not requested.

---

# 2. Confirmed User Structure

Aayushman Pharmacy has:

- **1 owner**
- **3 staff members**

The pharmacy is a **single retail pharmacy**.

For the initial PharmaKon system, these people will operate through **one shared system account** rather than individual employee accounts.

### Confirmed Access Model

```text
                    PharmaKon
                       │
                 Single Account
                       │
          ┌────────────┴────────────┐
          │                         │
    Operational Access         Analytics Access
          │                         │
   Manage pharmacy data       View analytics
```

The client explicitly requested that separate employee accounts should not be created for the initial system.

---

# 3. User Types vs System Roles

It is important to distinguish the pharmacy's **people** from the application's **roles**.

| Concept | Current Requirement |
|---|---|
| Owner | Person who owns/manages the pharmacy |
| Staff | 3 pharmacy employees |
| Application accounts | One account |
| Individual staff accounts | Not required |
| Advanced RBAC | Not required for initial system |
| Operational access | Required |
| Stock management access | Required |
| Analytics viewing | Required |

The owner and staff are therefore **business user types**, but they are not separate authenticated application roles in the initial version.

---

# 4. Initial System Role

## ROLE-001 — Pharmacy System User

The initial application will effectively operate with one system role:

**Pharmacy System User**

This account represents the operational user of the pharmacy management system.

### Responsibilities

The account must be capable of performing the operational activities required by the confirmed system scope, including:

- Managing product information
- Managing inventory
- Managing batches
- Recording purchases
- Recording supplier information
- Processing sales
- Generating invoices
- Recording payments
- Recording customer information
- Processing customer returns
- Recording credit transactions
- Recording later credit payments
- Recording damaged/expired stock returns
- Performing stock adjustments after physical verification
- Viewing stock and expiry information
- Viewing low-stock information
- Viewing analytics and reports
- Viewing purchasing/replenishment insights

These responsibilities are derived from the confirmed operational requirements. Detailed permission boundaries beyond the single-account model are not currently specified by the client.

---

# 5. Owner Responsibilities

The owner is the primary business decision-maker.

The owner's responsibilities include:

### Inventory

- Monitor current stock.
- Review low-stock products.
- Review expiry-risk products.
- Review stock movement.
- Review stock adjustments.

### Sales & Financial Information

- Review sales performance.
- Review revenue indicators.
- Review profit indicators.
- Review discount/custom-price activity through recorded sales information.

### Purchasing

- Use sales movement and current stock to make purchasing decisions.
- Review products requiring replenishment.
- Consider approximate replenishment quantities suggested by the system.

### Analytics

- Review fast-moving products.
- Review slow-moving products.
- Review sales trends.
- Review purchase patterns.
- Review inventory analytics.
- Review expiry-risk information.
- Use system insights to support purchasing decisions.

The system provides decision support; it does not replace the owner's purchasing judgment.

---

# 6. Staff Responsibilities

The pharmacy has **3 staff members** responsible for day-to-day pharmacy operations.

Their operational responsibilities include:

### Product & Inventory Operations

- Manage product information as required.
- Record and monitor stock.
- Work with product batches and expiry information.
- Perform physical stock verification.
- Record stock adjustments.
- Identify damaged or expired stock.

### Purchasing

- Record supplier purchases.
- Record purchase invoice/reference information.
- Record product, batch, expiry, quantity and purchase cost.
- Record payment information.
- Record supplier returns for damaged/expired stock.

### Sales & Billing

- Select or scan products.
- Process sales.
- Enter quantities.
- Use the appropriate batch according to FEFO.
- Enter actual/custom selling prices where required.
- Apply the configured discount.
- Complete tax and round-off calculations through the system.
- Record payment.
- Generate/print invoices.
- Provide digital invoices when requested.

### Customer Operations

- Record customer name and phone number where required.
- Process valid customer returns using the original invoice.
- Record refunds.
- Record credit sales.
- Record later credit payments.

Because all staff use the same initial account, the system does not currently distinguish one staff member's permissions from another's.

---

# 7. Permission Model

## 7.1 Confirmed Permission Principle

The single account should have the operational access necessary to run the pharmacy system.

The client specifically confirmed access to:

- **Manage stock**
- **View analytics**

The broader operational permissions listed in this document correspond to the confirmed workflows that the system must support.

## 7.2 Initial Permission Matrix

| Capability | Single Pharmacy Account |
|---|:---:|
| Authenticate | Yes |
| Product management | Yes |
| Batch management | Yes |
| Inventory management | Yes |
| Stock adjustment | Yes |
| Low-stock monitoring | Yes |
| Expiry monitoring | Yes |
| Supplier management | Yes |
| Purchase management | Yes |
| Sales processing | Yes |
| Invoice generation | Yes |
| Custom selling price | Yes |
| Discount entry/application | Yes |
| Tax calculation | Yes |
| Round-off | Yes |
| Payment recording | Yes |
| Customer management | Yes |
| Customer returns/refunds | Yes |
| Credit ledger | Yes |
| Damaged/expired stock handling | Yes |
| Supplier returns | Yes |
| Analytics | Yes |
| Purchasing/replenishment insights | Yes |
| Advanced role administration | No separate role requirement |

The final implementation of individual permissions should not become more granular than required without a confirmed business need.

---

# 8. Authentication Scope

The initial authentication requirement is intentionally limited.

## Required

- One account.
- Authentication before accessing the application.
- Access to the required pharmacy operations.
- Access to stock management.
- Access to analytics.

## Not Currently Required

- Separate accounts for the owner and each staff member.
- Individual staff profiles.
- Complex RBAC.
- Staff-specific dashboards.
- Staff-specific sales targets.
- Staff-specific permissions.
- Employee attendance management.
- Employee payroll management.

These items are not part of the client's confirmed initial requirement.

---

# 9. Accountability Limitation

Because the initial system uses one shared account, PharmaKon will **not be able to reliably attribute an individual transaction to a specific staff member** unless an additional user-identification mechanism is introduced later.

This is a consequence of the confirmed single-account design.

The current requirements do not specify a need for:

- Per-employee audit attribution
- Individual staff login history
- Individual staff sales performance
- Individual staff permissions

If the client later requires these capabilities, the authentication and authorization design will need to be revised.

---

# 10. Future Role Expansion

A future version may introduce separate accounts and more granular permissions if the pharmacy requires them.

Possible future roles could include:

- Owner/Administrator
- Pharmacy Staff
- Manager

However, these are **not current PharmaKon roles** and should not be implemented merely as a design assumption.

Any future role system must be based on a new confirmed client requirement.

---

# 11. Role-Related Business Boundaries

The following boundaries apply to the current design:

### Boundary 1 — One Account

The initial application has one authenticated account for the pharmacy.

### Boundary 2 — No Artificial RBAC

Do not create separate employee roles simply because a conventional business application might have them.

### Boundary 3 — Operational Access First

The account must support the pharmacy's confirmed operational workflows.

### Boundary 4 — Analytics Access

The account must be able to view the analytics required by the owner.

### Boundary 5 — Future Changes Require Confirmation

If the client requests individual accounts or differentiated permissions, the role model must be formally updated before implementation.

---

# 12. User Responsibilities by Workflow

| Workflow | Owner | Staff | System Account |
|---|---|---|---|
| Product management | Business oversight | Operational use | Same access |
| Purchase entry | Review/oversight | Operational use | Same access |
| Inventory monitoring | Review | Operational use | Same access |
| Stock adjustment | Review | Perform operational process | Same access |
| Sales | Review | Process sales | Same access |
| Invoice generation | Review | Generate/print/send | Same access |
| Customer return | Review | Process return | Same access |
| Credit sale | Review | Record transaction | Same access |
| Credit payment | Review | Record payment | Same access |
| Supplier return | Review | Record/process | Same access |
| Low-stock monitoring | Review | Operational visibility | Same access |
| Expiry monitoring | Review | Operational visibility | Same access |
| Analytics | Primary consumer | Available through shared account | Same access |
| Purchasing decision | Primary decision-maker | Provide operational input | System provides insight |

This table describes **business responsibilities**, not separate application permissions.

---

# 13. Audit and History Considerations

Although there is currently only one account, PharmaKon must still preserve operational history where required.

The system should retain records for:

- Sales
- Returns
- Purchases
- Supplier returns
- Stock adjustments
- Credit transactions
- Credit payments
- Stock movements

A shared account must not be interpreted as permission to delete or overwrite historical business transactions.

Transaction history remains important for analytics, reconciliation, and operational traceability.

---

# 14. Requirements That Would Trigger a Role-Model Change

The authentication/authorization design should be reconsidered if the client later requests any of the following:

- Individual employee logins.
- Different permissions for owner and staff.
- Restricting staff from viewing analytics.
- Restricting staff from changing prices or discounts.
- Approval requirements for stock adjustments.
- Approval requirements for returns/refunds.
- Staff-level audit attribution.
- Employee performance reports.
- Staff-specific sales targets.
- Multiple pharmacy branches.

Any such change should be recorded as a new or changed requirement and evaluated for its impact on the architecture, database, API, UI, testing, and project timeline.

---

# 15. Final Role Baseline

For the current PharmaKon MVP:

```text
Aayushman Pharmacy
        │
        ├── Owner
        │
        └── 3 Staff Members
                 │
                 ▼
        ┌───────────────────┐
        │  ONE SYSTEM       │
        │     ACCOUNT       │
        └───────────────────┘
                 │
       ┌─────────┴──────────┐
       ▼                    ▼
Operational Access     Analytics Access
       │                    │
       ├─ Products           ├─ Sales trends
       ├─ Batches            ├─ Product performance
       ├─ Inventory          ├─ Stock analytics
       ├─ Purchases          ├─ Expiry risk
       ├─ Sales              ├─ Purchase patterns
       ├─ Invoices           ├─ Revenue/profit
       ├─ Returns            └─ Replenishment insights
       ├─ Credit
       └─ Stock adjustments
```

**Current role count: 1 application account/role.**

The owner and three staff members are business users of the same account, not separate application roles.

---

# 16. Source of Truth

The role and access model in this document is based on the client's confirmed requirement that the initial system should use **one account**, with the required operational access to manage stock and view analytics, and should not introduce advanced role-based accounts.

If the client later changes the access model, this document must be updated before implementing the new authentication/authorization behavior.
