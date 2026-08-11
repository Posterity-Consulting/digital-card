# Digital business card — Canva build spec

A minimal physical card whose only job is to point to the NFC tap / QR
scan experience — not to carry all your contact details itself.

## Canvas

- Create a **Custom size** in Canva: **85.6mm × 54mm** (standard credit
  card / NFC card size — matches the physical NTAG card stock most
  suppliers sell), at **300 DPI**.
- In pixels at 300 DPI: **1011 × 638 px**.
- Set a **3mm bleed** if you're sending this to a printer (Canva → Print
  settings → Bleed).
- Keep all text at least **4mm (≈47px)** from every edge — this is your
  safe margin so nothing gets trimmed.

## Palette (matches the digital contact page)

- Ink navy background: `#101B33`
- Paper white text: `#FFFFFF`
- Brass accent (rule lines, tap icon only): `#AD8A50`
- Do not introduce a third colour — one accent, used sparingly, is the
  whole point of "premium and minimal."

## Type hierarchy (top to bottom)

1. **Name** — largest element on the card. Serif display font (Canva:
   "Playfair Display" or "Lora"), ~24–28pt, white.
2. **Designation** — one size down, ~11–12pt, brass or 70%-opacity white,
   directly under the name.
3. **Company** — smallest of the text stack, ~9pt, uppercase, letter-
   spaced (~150), full opacity white or brass. "POSTERITY CONSULTING".
4. Nothing else in text. No phone number, no email, no address printed
   on the card — that's deliberate; it all lives behind the tap/scan, and
   printing it defeats the "keep it minimal" and "always current" goals
   (a printed number can't be updated; the linked page can).

## Layout placement

```
┌─────────────────────────────────────────────┐
│  (16mm margin)                               │
│                                               │
│   NAME PLACEHOLDER                    ┌───┐  │
│   Designation Placeholder             │QR │  │
│   POSTERITY CONSULTING                └───┘  │
│                                               │
│         ›)))  TAP OR SCAN TO CONNECT         │
│                                               │
└─────────────────────────────────────────────┘
```

- **Logo/name block**: left-aligned, vertically centered, starting ~16mm
  from the left edge.
- **QR code**: top-right corner, ~18mm × 18mm square, ~10mm from the top
  and right edges. Export the SVG from `qr/kaamini-jha-qr.svg` (or the
  regenerated one) and place it directly — don't recreate the QR pattern
  by hand in Canva.
- **Tap/scan instruction**: bottom-center or bottom-left, small NFC
  "waves" icon (Canva icon search: "nfc" or "contactless") next to the
  words **"TAP OR SCAN TO CONNECT"**, ~8pt, brass colour, letter-spaced.
  This is the single most important line of copy on the card — it's the
  instruction, not decoration.
- Leave the remaining ~50% of the card as clean navy negative space. The
  restraint is the design; resist the urge to fill it.

## Two-up variant (for print sheets)

If your printer wants a print-ready sheet with both cards, duplicate the
frame in Canva onto an A4 or Letter page, one card per person, each
pulling its own QR export (`kaamini-jha-qr.svg` / `pragya-jha-qr.svg`) and its
own name/designation text — everything else on the template stays
identical, which is the same "shared template, swapped content" approach
used in the website's HTML/CSS.
