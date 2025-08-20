from time import sleep

import pytest
from playwright.sync_api import Page,expect

def test_UIchecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name = "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #hover
    page.locator("#mousehover").hover()
    sleep(3)
    page.get_by_role("link",name = "Top").click()

def test_alerts(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button",name = "Confirm").click()

def test_handleFrames(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageframe = page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link",name = "All Access plan").click()
    expect(pageframe.locator("body")).to_contain_text("Happy Subscibers!")

def test_handleTables(page:Page):
    #check price of rice equal to 37
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count() > 0:
            colValue = i
            print(f"Price col value: {colValue}")
            break

    row = page.locator("tr").filter(has_text="Rice")
    print(f"Price row: {row}")

    expect(row.locator("td").nth(colValue)).to_have_text("37")
