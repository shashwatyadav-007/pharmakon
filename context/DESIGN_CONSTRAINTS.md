# PharmaKon Design Constraints

**Authority:** This document is binding. Every developer, designer, and AI agent working on this project must comply with every rule listed here. No exceptions. No partial compliance.

**Scope:** These rules apply to all frontend code, UI components, marketing copy, landing pages, documentation headings, README files, and any user-facing output.

---

## Prohibited Visual Patterns

The following visual patterns are permanently banned from this project:

| Category | Banned Item |
| :--- | :--- |
| Color | Purple-to-blue gradient, or any color gradient used as a background or hero element |
| Color | Gradient text (headings, hero text, or any other text rendered with CSS gradients) |
| Color | Low-contrast dark mode (text must always meet WCAG AA contrast ratio of 4.5:1 minimum) |
| Buttons | Pill-shaped buttons (use standard rectangular buttons with visible borders and defined corners) |
| Cards | Glassmorphism cards (frosted glass, backdrop-blur, semi-transparent overlays) |
| Cards | Color-left-border accent cards (cards with a colored vertical stripe on the left edge) |
| Layout | Three icon boxes in a row as a feature section |
| Layout | A badge or label positioned above the main headline |
| Layout | Inconsistent spacing between sections, cards, or elements |
| Animation | Sections fading in as the user scrolls (scroll-triggered fade/slide animations) |
| Animation | Cursor-following beam, spotlight, or glow effect |
| Animation | Buttons that fade on hover instead of using a clear, instant state change |
| Animation | Over-the-top scroll animations of any kind |
| Animation | Cursor animation or trail effects |
| Icons | Lucide icons used as the default icon set |
| Icons | Emoji characters used as icons in headings, navigation, buttons, or feature lists |
| Components | Untouched, default shadcn/ui components shipped without customization |
| Typography | Inter font used as the primary or sole typeface |
| Typography | Space Grotesk + Instrument Serif font pairing |
| Typography | Serif italics used purely for decorative accent on individual words |
| Typography | Gradient-rendered heading text |
| Texture | Grain texture overlay on backgrounds or images |

---

## Prohibited Content Patterns

| Category | Banned Item |
| :--- | :--- |
| Copy | Vague hero text ("Revolutionize your...", "Supercharge your...", "The future of...") |
| Copy | Generic buzzwords without specific meaning ("seamless", "cutting-edge", "next-gen", "leverage") |
| Copy | Em dashes used as a stylistic crutch throughout prose |
| Copy | AI-generated stock copy that reads like filler |
| Data | Fake reviews or testimonials |
| Data | Fake metrics, counters, or statistics |
| Data | Fake customer counters ("10,000+ happy users") |
| Media | AI-generated stock photos or illustrations |
| Branding | Any "made with AI", "built with [AI tool]", or similar attribution tags visible to end users |
| Headings | Emoji characters placed before or after heading text in any document |

---

## Mandatory Launch Checklist

This application will not be deployed to production until every item below is satisfied:

- [ ] Custom domain connected (DNS A-record or CNAME configured, no default platform subdomain)
- [ ] Favicon added (`/public/favicon.ico` and appropriate `<link>` tags in HTML head)
- [ ] All "made with AI" or "built with [tool]" tags removed from the UI, footer, and HTML source
- [ ] Privacy Policy page implemented at `/privacy-policy` with real, applicable content
- [ ] Terms and Conditions page implemented at `/terms-and-conditions` with real, applicable content
- [ ] All visible content reviewed for compliance with every rule in this document

---

## What to Use Instead

| Instead of | Use |
| :--- | :--- |
| Purple gradients | Flat, solid brand colors (Emerald #059669, Slate #0f172a, Amber #f59e0b) |
| Pill-shaped buttons | Rectangular buttons with `border-radius: 4px` to `6px`, visible borders, and clear hover states |
| Glassmorphism cards | White cards with `1px` solid border (`border-slate-200`) and `shadow-sm` |
| Lucide icons everywhere | SVG icons from a neutral set (Heroicons, Phosphor) or custom SVGs, used sparingly |
| Inter font | System font stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`) |
| Fade-on-hover buttons | Buttons with instant background-color change on hover (no transition longer than 100ms) |
| Scroll-triggered fade-ins | Elements rendered immediately in their final position, no entrance animation |
| Emoji in headings | Plain text headings. If a visual marker is needed, use a small inline SVG icon |
| Vague hero copy | Specific, factual description of what the product does for the user |
| Fake metrics | Real data from the database, or no metrics shown at all until real data exists |
| Em dashes | Commas, semicolons, colons, or separate sentences |

---

## Enforcement

- Any AI agent that generates code, copy, or UI for this project must read this file before producing output.
- Any pull request or commit that introduces a banned pattern must be rejected.
- This file is referenced from `context/ai-workflow.md`, `context/ui-context.md`, `context/coding-standards.md`, and `README.md`.
