# Context — AI Agent Operating Rules & Workflow

## Core Philosophy
> *"You are the architect and developer; AI is the implementation engine."*

When editing or implementing features in this repository, all AI agents MUST strictly follow these rules:

---

## 1. Specification-Driven Implementation
1. **Read Specifications First:** Before writing code for any component, read the corresponding document in `docs/` or feature specification in `specs/`.
2. **Obey Bounded Scopes:** Implement strictly what is defined in the target specification. Do NOT invent unrequested modules, microservices, or external integrations.
3. **No Architecture Improvisation:** Maintain the single-account authentication model and modular monolith structure defined in `docs/04-user-roles.md` and `docs/07-system-architecture.md`.

---

## 2. Code Modification Safeguards
1. **Preserve Documentation & Comments:** Do not delete or mangle existing docstrings, requirement tags (`FR-XXX`, `BR-XXX`), or comments.
2. **Never Mask Errors:** Never catch exceptions silently or return dummy fallback data when an operational logic or data integrity error occurs.
3. **Atomic Changes:** Keep edits modular and tightly focused on the relevant files.

---

## 3. Mandatory Verification Checklist
Before declaring any task or feature specification complete, the AI agent must:
- [ ] Run backend unit tests (`pytest`) and confirm 100% pass rate.
- [ ] Verify Alembic database migrations run cleanly (`alembic upgrade head`).
- [ ] Verify API endpoints match OpenAPI contracts in `docs/09-api-design.md`.
- [ ] Verify that inventory quantity constraints and FEFO business rules hold.
- [ ] Record progress update in `context/progress.md`.
