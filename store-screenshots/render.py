import os
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = "file://" + os.path.join(BASE, "index.html")
OUT = os.path.join(BASE, "out")
os.makedirs(OUT, exist_ok=True)

slides = [
    ("s1-en", "01-hero.png"),
    ("s2", "02-three-categories.png"),
    ("s3", "03-ai-funfacts.png"),
    ("s4", "04-safety.png"),
    ("s5", "05-learning.png"),
    ("s6", "06-progress.png"),
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
    page.close()

    fg_page = browser.new_page(viewport={"width": 1024, "height": 500}, device_scale_factor=1)
    fg_page.goto(HTML)
    fg_page.wait_for_timeout(300)
    fg_page.locator("#feature-graphic").screenshot(path=os.path.join(OUT, "feature-graphic.png"))
    print("saved feature-graphic.png")
    fg_page.close()

    browser.close()
