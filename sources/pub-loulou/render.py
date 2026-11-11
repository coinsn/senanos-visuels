import os
from playwright.sync_api import sync_playwright
os.makedirs('ov',exist_ok=True); FPS=30; D=27.5
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file:///home/claude/ad1/ad.html'); pg.wait_for_timeout(900)
    for i in range(int(FPS*D)):
        pg.evaluate(f'render({i/FPS})'); pg.screenshot(path=f'ov/f{i:04d}.png',omit_background=True)
    b.close()
