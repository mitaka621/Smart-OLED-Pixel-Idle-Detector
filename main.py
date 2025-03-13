import time
import numpy as np
import ctypes
import mss
from PIL import Image, ImageChops
import os
import logging

DEBUG = False #when set to True, screenshots, containing only the pixels which changed between captures, will be saved and also the activity will be logged in the activity.log file

CHECK_INTERVAL = 2  # The check interval in seconds
INACTIVITY_THRESHOLD = 60 * 3  # The time in seconds of screen inactivity before turning off the monitors
TASKBAR_HEIGHT = 40  # Approximate taskbar height in px in order not to capture the clock change (adjust if needed)

if DEBUG:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[
        logging.FileHandler("activity.log"),
        logging.StreamHandler()
    ])

def turn_off_monitor():
    ctypes.windll.user32.PostMessageW(0xFFFF, 0x0112, 0xF170, 2)
    return

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

def get_idle_time():
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
    return (ctypes.windll.kernel32.GetTickCount() - lii.dwTime) / 1000.0 

def capture_screen():
     with mss.mss() as sct:
        monitors = sct.monitors[1:]
        screenshots = []
        for i, monitor in enumerate(monitors):
            screenshot = sct.grab(monitor)
            img = Image.frombytes("RGB", (screenshot.width, screenshot.height - TASKBAR_HEIGHT), screenshot.rgb)
            screenshots.append(img)
        
        total_width = sum(img.width for img in screenshots)
        max_height = max(img.height for img in screenshots)
        combined_image = Image.new("RGB", (total_width, max_height))

        x_offset = 0
        for img in screenshots:
            combined_image.paste(img, (x_offset, 0))
            x_offset += img.width

        return combined_image

def images_are_different(img1, img2):
    diff = ImageChops.difference(img1, img2)    
    
    isDiff=np.any(np.array(diff));
    
    if DEBUG & isDiff:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        diff.save(f"screenshots/screenshot_{timestamp}.png")
        
    return isDiff

last_screenshot = capture_screen()
last_change_time = time.time()
monitor_is_off = False

while True:
    time.sleep(CHECK_INTERVAL)

    if monitor_is_off:
        if get_idle_time() < 2: 
            logging.info("User activity detected, resuming monitoring...")
            last_change_time = time.time()
            monitor_is_off = False
        continue

    current_screenshot = capture_screen()

    dif = images_are_different(last_screenshot, current_screenshot)
    
    logging.info(f"Difference detected: {dif}")
    
    if dif:
        last_change_time = time.time()
    elif time.time() - last_change_time > INACTIVITY_THRESHOLD:
        logging.info("Turning off monitor...")
        turn_off_monitor()
        monitor_is_off = True

    last_screenshot = current_screenshot