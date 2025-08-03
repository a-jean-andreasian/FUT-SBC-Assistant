# X, Y coordinates for various UI elements in a game or application.

SBC_CELL = 724, 432
AUTO_SBC_LOGO = 212, 292
AUTO_SBC_BUILD = 953, 709
# Pause 1,5 sec

EXCHANGE_BUTTON = 1671, 809
CLAIM_BUTTON = 955, 765

from lib import pyautogui
import time


def click_on_scb(position):
    pyautogui.moveTo(position)
    pyautogui.click()
    time.sleep(0.8)


def click_on_logo(position):
    pyautogui.moveTo(position)
    pyautogui.click()
    time.sleep(0.1)


def click_on_build(position):
    pyautogui.moveTo(position)
    pyautogui.click()
    time.sleep(2)  # Wait for the build to complete


def click_on_exchange(position):
    pyautogui.moveTo(position)
    pyautogui.click()
    time.sleep(2)  # Wait for the exchange to complete


def click_on_claim(position):
    pyautogui.moveTo(position)
    pyautogui.click()
    time.sleep(0.5)


def sbc_script():
    print("Starting Auto SBC script...")
    time.sleep(2)  # Wait for 2 seconds before starting

    click_on_scb(SBC_CELL)
    click_on_logo(AUTO_SBC_LOGO)
    click_on_build(AUTO_SBC_BUILD)
    click_on_exchange(EXCHANGE_BUTTON)
    click_on_claim(CLAIM_BUTTON)

    print("Auto SBC script completed.")


def pick_83_plus():
    try:
        while True:
            sbc_script()
    except Exception as e:
        print(f"Script stopped by the user.")
