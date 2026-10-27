import os
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = "file://" + os.path.join(BASE, "index.html")
OUT = os.path.join(BASE, "out")
os.makedirs(OUT, exist_ok=True)

slides = [
    ("s1", "01-hero.png"),
    ("s2", "02-drei-kategorien.png"),
    ("s3", "03-ki-funfacts.png"),
    ("s4", "04-sicherheit.png"),
    ("s5", "05-lernen.png"),
    ("s6", "06-archiv-mehrsprachig.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    page.goto(HTML)
    page.wait_for_timeout(300)
    for sel, fname in slides:
        el = page.locator(f"#{sel}")
        el.screenshot(path=os.path.join(OUT, fname))
        print("saved", fname)
    browser.close()
