import pyautogui
import pytesseract
from shared import is_running

from pykeyboard import PyKeyboard

def screenshot_and_ocr():
    """
    Take a screenshot and run OCR on it.
    """
    if is_running():
        screenshot = pyautogui.screenshot()
        text = pytesseract.image_to_string(screenshot)
        return text
    return ""

def ocrF3():
    """
    Press F3,
    take a screenshot,
    crop it to the first 600x600 pixels from the top-left corner,
    and run OCR on it.
    """
    if is_running():
        PyKeyboard().press_key(PyKeyboard().function_keys[3])
        screenshot = pyautogui.screenshot()
        PyKeyboard().release_key(PyKeyboard().function_keys[3])
        cropped_screenshot = screenshot.crop((0, 0, 600, 600))
        text = pytesseract.image_to_string(cropped_screenshot)
        return text
    return ""

def ocr_custom_region(left, top, width, height):
    """
    Take a screenshot, crop it to a custom region, and run OCR on it.
    """
    if is_running():
        screenshot = pyautogui.screenshot()
        cropped_screenshot = screenshot.crop((left, top, width, height))
        text = pytesseract.image_to_string(cropped_screenshot, config='--psm 6')
        return text
    return ""
