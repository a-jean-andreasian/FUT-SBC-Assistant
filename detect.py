import pyautogui

print("Move your mouse. Press Ctrl+C to stop.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}", end='\r')
except KeyboardInterrupt:
    print("\nStopped.")
