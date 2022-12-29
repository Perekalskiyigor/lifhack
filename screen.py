import pyautogui
# Снимок экрана.
screenshot = pyautogui.screenshot()
# Сохранение изображения.
screenshot.save("screenshot.png")


# Захват части экрана.
# screenshot = pyautogui.screenshot(region=(50, 50, 400, 300))