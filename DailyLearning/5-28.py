# from webbrowser import Chrome
# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False,slow_mo=50,channel="chrome")
#     page = browser.new_page()
#     page.goto("http://154.39.243.212:5000/oo/r/658488368579000999#tid=4")

import pendulum
day1 = pendulum.today()
print(day1)
day2 = pendulum.now()
print(day2)