#!/usr/bin/env python3
"""
Regenerate the QR codes for both profiles.

Usage:
    pip install "qrcode[pil]"
    python3 generate_qr.py

Edit BASE_URL below once you know your real GitHub Pages (or custom domain)
URL, then re-run this script. The QR codes point at the HTTPS contact page
URL only -- never at the .vcf file directly -- so they keep working even
after you edit contact details later.
"""

import qrcode
import qrcode.image.svg

# ---------------------------------------------------------------------------
# EDIT THIS: your real deployed URL, e.g. "https://yourusername.github.io/digital-card"
# If you use a custom domain instead, e.g. "https://connect.posterityconsulting.com"
BASE_URL = "https://posterity-consulting.github.io/digital-card"
# ---------------------------------------------------------------------------

PROFILES = ["kaamini-jha", "pragya-jha"]

for slug in PROFILES:
    url = f"{BASE_URL}/connect/{slug}/"

    # PNG (for the physical card / Canva / printing)
    img = qrcode.make(url, box_size=20, border=2)
    img.save(f"{slug}-qr.png")

    # SVG (scalable, for print at any size)
    factory = qrcode.image.svg.SvgPathImage
    svg_img = qrcode.make(url, image_factory=factory, box_size=20, border=2)
    svg_img.save(f"{slug}-qr.svg")

    print(f"{slug}: {url}  ->  {slug}-qr.png, {slug}-qr.svg")

print("\nDone. Re-run this script any time the base URL changes.")
