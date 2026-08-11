# Posterity Consulting — Digital Visiting Card

A free, self-hosted, contactless replacement for a printed business card.
Tap an NFC card or scan a QR code → opens a contact page → tap **Save
Contact** → the person's real address book gets your official details.

No backend, no database, no login, no subscription, no analytics.

**Live site:** https://posterity-consulting.github.io/digital-card/
- Kaamini Jha: https://posterity-consulting.github.io/digital-card/connect/kaamini-jha/
- Pragya Jha: https://posterity-consulting.github.io/digital-card/connect/pragya-jha/

---

## 1. Architecture (read this before touching any files)

```
 Recipient's phone
   │
   │  taps NFC tag  OR  scans QR code
   ▼
 https://posterity-consulting.github.io/digital-card/connect/kaamini-jha/   ← plain static HTML
   │
   │  page shows name, title, company, contact buttons
   │  "Save Contact" button links directly to:
   ▼
 /contacts/kaamini-jha.vcf   ← plain text vCard file, no JS required to open it
```

Three deliberate design choices, and why:

- **The NFC tag stores only the page URL, never the vCard itself.**
  NDEF tags have very little storage, and a URL-only tag means you can
  correct a phone number or job title later by editing one file and
  re-deploying — the physical tag and the printed QR code never need to
  change.

- **"Save Contact" is a plain link to a static `.vcf` file, not a
  JavaScript-generated download.** This is the most reliable way to get
  iOS Safari to show its native "Add to Contacts" preview, and it means a
  non-developer can update someone's phone number by editing a short text
  file — no code to touch.

- **Two almost-identical HTML pages instead of one clever templated page.**
  A single JavaScript-templated page would technically be "less
  duplication," but it means a non-developer has to edit a JavaScript
  object to change a phone number. Two plain HTML files, sharing one CSS
  file for all the styling, are easier to safely edit and harder to break.
  The "large amount of code" that actually repeats (the layout and design)
  lives once, in `assets/styles.css`.

---

## 2. Project structure

```text
digital-card/
├── index.html                     # internal test page, links to both profiles
├── assets/
│   ├── styles.css                 # ALL colours, fonts, spacing — edit once, both cards change
│   └── logo.png                   # real Posterity Consulting logo, shared by both cards
├── connect/
│   ├── kaamini-jha/
│   │   └── index.html             # Kaamini's contact page — edit the text in here
│   └── pragya-jha/
│       └── index.html             # Pragya's contact page
├── contacts/
│   ├── kaamini-jha.vcf             # Kaamini's vCard — keep in sync with the page above
│   └── pragya-jha.vcf
└── qr/
    ├── generate_qr.py              # regenerate QR codes if the deployed URL ever changes
    ├── kaamini-jha-qr.png / .svg   # QR codes, already pointing at the live URLs above
    └── pragya-jha-qr.png / .svg
```

---

## 3. Requirement-by-requirement: what's free vs. what physically costs money

Everything **software-side** here is $0, forever, with no subscription:
static hosting, the vCard, the QR codes, the contact pages.

One thing is physical hardware and cannot be made free — flagging this
clearly, as requested:

| Item | Cost | Why it can't be $0 |
|---|---|---|
| Blank NTAG213/215/216 NFC cards or stickers | ~₹25–90 (~$0.30–1) each, one-time | You're writing a URL onto a physical chip; there's no software substitute for the chip itself. This is *writing*, not *printing* — no ink or card stock involved. |

**No printing is used in this setup.** Per your preference, this build
relies on:
- **NFC tap** — a blank tag, written once with the free NFC Tools app (§9).
- **On-screen QR** — each contact page already renders its own QR code
  (the `qr-panel` section) pointing at itself, so you show that directly
  off your phone screen — nothing gets printed.

If you'd rather skip even the NFC tag's small hardware cost, QR-only
(scan straight off your screen) is entirely free with nothing to buy.

Everything else — the domain (`*.github.io`), hosting, the contact page,
the vCard, the QR image files, and the NFC-writing app — is free with no
catch.

---

## 4. How to create/edit the VCF

Each `.vcf` file is plain text. Open `contacts/kaamini-jha.vcf` in any
text editor and edit the values after each colon:

```
BEGIN:VCARD
VERSION:3.0
N:Jha;Kaamini;;;
FN:Kaamini Jha
ORG:Posterity Consulting
TITLE:Senior Manager
TEL;TYPE=CELL,VOICE:+919871704410
EMAIL;TYPE=INTERNET,WORK:kaamini@posterity.in
URL:https://www.posterity.in
NOTE:LinkedIn: https://www.linkedin.com/in/kaamini-jha/
REV:2026-08-12T00:00:00Z
END:VCARD
```

Notes:
- `N:` is `Last;First;;;` — used internally by contact apps for sorting.
- `FN:` is the "display name" shown when the contact is added — this is
  what recipients actually see.
- Keep every line ending as-is; don't add blank lines inside the block.
- vCard 3.0 was used because it has the most consistent iOS + Android
  compatibility of the two candidate versions. 4.0 is newer but iOS
  Contacts has historically been fussier about it.

## 5. How to replace contact details

Two files need to stay in sync for each person:

1. `contacts/<name>.vcf` — the actual data added to the recipient's
   address book (edit as shown above).
2. `connect/<name>/index.html` — what's *displayed on the page* and
   what the Call / WhatsApp / Email / LinkedIn / Website buttons link to.
   Open it in any text editor and replace the name, role, `tel:`,
   `wa.me`, `mailto:`, and the LinkedIn/website `href` values.

No build step, no compiling — just save the file.

**Company logo:** both cards share one logo file —
`assets/logo.png` — the real Posterity Consulting mark, since it's the
same for both of you (unlike the vCard/details, which are per-person).
Replace that one file (same filename) if the logo ever changes.

## 6. How to deploy the site (GitHub Pages)

Already done for this project — live at the URLs listed at the top. For
reference, or if you ever start a fresh copy:

1. **Create a free GitHub account** at github.com if you don't have one.
2. **Create a new repository**, set it to **Public** (GitHub Pages' free
   tier requires a public repo).
3. **Upload the files**: click *Add file → Upload files*, then drag in
   the **contents** of the `digital-card` folder — not the folder itself
   — so `assets/`, `connect/`, `contacts/`, `qr/`, and `index.html` sit
   directly at the repo root. (A common mistake: dragging the whole
   folder creates a nested `digital-card/digital-card/...` path and the
   site 404s — check the repo's file list has no double folder.)
4. **Turn on Pages**: *Settings → Pages* → Source: `Deploy from a
   branch`, Branch: `main`, folder: `/ (root)`. Save.
5. Wait 1–2 minutes, refresh Settings → Pages for the green "site is
   live" banner with your URL.

## 7. The HTTPS URLs

```
https://posterity-consulting.github.io/digital-card/connect/kaamini-jha/
https://posterity-consulting.github.io/digital-card/connect/pragya-jha/
```

These are the URLs on the NFC tags and in the QR codes — never a link
straight to the `.vcf` file.

## 8. How to generate the QR code

Already generated and correct for the live URLs above. If the deployed
URL ever changes (new repo name, custom domain, etc.):

1. Open `qr/generate_qr.py`, edit the `BASE_URL` line near the top.
2. Run:
   ```
   pip install "qrcode[pil]"
   python3 generate_qr.py
   ```
3. This overwrites `kaamini-jha-qr.png/.svg` and `pragya-jha-qr.png/.svg`.
   Re-upload them to the same `qr/` folder in GitHub, same filenames.

No paid QR API was used — this generates the codes entirely offline.

## 9. How to program an NFC card/tag

**What to buy:** blank **NTAG213** tags (cheapest, ~144 bytes — plenty for
one URL). NTAG215/216 also work if that's what you already have.

**On iPhone (no computer needed):**
1. Install the free app **NFC Tools** (by wakdev) from the App Store.
2. Open NFC Tools → **Write** tab → **Add a record** → **URL/URI**.
3. Type the exact page URL from §7 → **OK**.
4. Tap **Write** → hold the blank NFC card/sticker to the **top back** of
   the iPhone (near the camera bump) until it confirms "Written".
5. Optional: use **Lock tag** only once you're fully done editing —
   locking makes it permanently read-only (the *contact details* can
   still change freely afterward, since the tag only stores the URL).

## 10. How to test NFC on an iPhone

- iPhone XS/XR and later read NFC natively — no app needed to *read* a
  tag, only to *write* one.
- Hold the top back of the phone near the tag; a notification banner
  appears with the URL — tap it to open Safari.
- If nothing happens: check the phone isn't in a thick magnetic case
  that blocks the antenna.

## 11. How to test NFC on Android

- **Settings → Connected devices → Connection preferences → NFC** — make
  sure it's on (often off by default).
- Hold the back of the phone against the tag for 1–2 seconds. A
  notification appears with the link — tap to open Chrome.
- Screen must be on and unlocked for NFC reads to register.

## 12. How a recipient saves the contact on iPhone

1. They tap **Save Contact** (or the page opens automatically after the
   NFC tap/QR scan).
2. Safari opens the `.vcf` and shows a native **contact preview card**
   with the details already filled in.
3. They tap **Add to Contacts** → **Done**. No app install needed.

## 13. How a recipient saves the contact on Android

1. They tap **Save Contact**. Chrome downloads the `.vcf` file.
2. They tap that download notification (or open it via **Files** /
   **Downloads**) → choose **Contacts**.
3. Contacts opens with the details pre-filled → they tap **Save**.

   *Platform limitation:* unlike iOS, not all Android skins behave
   identically — most modern phones open Contacts in one tap; a few
   older/customized ones need the extra step of opening Files first.
   This is a difference in each manufacturer's Chrome build, not
   something the site's code controls.

## 14. How to update details later without changing the NFC tag or QR code

1. Edit `connect/<name>/index.html` and `contacts/<name>.vcf` with the
   new details (§4–5).
2. Re-upload just those two files to the same GitHub repo, same paths,
   same filenames.
3. Done — the physical NFC tag and QR code both still point at the same
   URL, so they now serve the *updated* page and vCard automatically.

---

## 15. No physical card

This build deliberately skips a printed card — only the NFC tag and the
on-screen QR panel are used. `canva-card-spec.md` is included only as an
optional reference in case a printable card is ever wanted later; it
isn't needed for anything described above.
