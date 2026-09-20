# Context: AI Agent Operating Rules and Workflow

## Core Philosophy

> "You are the architect and developer; AI is the implementation engine."

When editing or implementing features in this repository, all AI agents MUST strictly follow these rules.

---

## 1. Specification-Driven Implementation

1. **Read Specifications First:** Before writing code for any component, read the corresponding document in `docs/` or feature specification in `specs/`.
2. **Obey Bounded Scopes:** Implement strictly what is defined in the target specification. Do NOT invent unrequested modules, microservices, or external integrations.
3. **No Architecture Improvisation:** Maintain the single-account authentication model and modular monolith structure defined in `docs/04-user-roles.md` and `docs/07-system-architecture.md`.

---

## 2. Code Modification Safeguards

1. **Preserve Documentation and Comments:** Do not delete or mangle existing docstrings, requirement tags (`FR-XXX`, `BR-XXX`), or comments.
2. **Never Mask Errors:** Never catch exceptions silently or return dummy fallback data when an operational logic or data integrity error occurs.
3. **Atomic Changes:** Keep edits modular and tightly focused on the relevant files.

---

## 3. UI and Copy Quality Rules

**Before generating any frontend code, UI component, landing page, marketing copy, or user-facing text, the AI agent MUST read [`DESIGN_CONSTRAINTS.md`](../DESIGN_CONSTRAINTS.md) in the project root.**

Key rules (non-exhaustive; the full list is in `DESIGN_CONSTRAINTS.md`):

1. **No prohibited visual patterns.** No purple gradients, pill-shaped buttons, glassmorphism, gradient hero text, scroll-triggered fade-ins, cursor-following animations, Lucide icons, untouched shadcn components, low-contrast dark mode, grain textures, or three-icon-boxes-in-a-row layouts.
2. **No prohibited typography.** Do not use Inter as the primary font. Do not use Space Grotesk + Instrument Serif. Do not use serif italics for decorative accent words. Use the system font stack.
3. **No emoji in headings or documentation.** Headings use plain text only.
4. **No em dashes.** Use commas, semicolons, colons, or separate sentences.
5. **No fake content.** No fake reviews, fake metrics, fake customer counters, AI-generated stock photos, or vague hero text.
6. **No AI attribution.** Remove any "made with AI", "built with [tool]", or similar tags from all user-facing surfaces.
7. **Real data only.** Dashboard metrics, counters, and charts must display real database data. If no data exists, show "No data yet" instead of zeros or placeholder numbers.

---

## 4. Mandatory Verification Checklist

Before declaring any task or feature specification complete, the AI agent must:

- [ ] Run backend unit tests (`pytest`) and confirm 100% pass rate.
- [ ] Verify Alembic database migrations run cleanly (`alembic upgrade head`).
- [ ] Verify API endpoints match OpenAPI contracts in `docs/09-api-design.md`.
- [ ] Verify that inventory quantity constraints and FEFO business rules hold.
- [ ] Verify that any new UI code complies with every rule in `DESIGN_CONSTRAINTS.md`.
- [ ] Verify that no emoji characters, em dashes, or vague copy appear in new or modified files.
- [ ] Record progress update in `context/progress.md`.
