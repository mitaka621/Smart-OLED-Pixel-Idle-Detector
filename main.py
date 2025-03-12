import time
import numpy as np
import ctypes
import mss
from PIL import Image, ImageChops
import os

CHECK_INTERVAL = 2  # The check interval in seconds
INACTIVITY_THRESHOLD = 60 * 3  # The time in seconds of screen inactivity before turning off the monitor
TASKBAR_HEIGHT = 40  # Approximate taskbar height in px in order not to capture the clock change (adjust if needed)

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
    return np.any(np.array(diff))

last_screenshot = capture_screen()
last_change_time = time.time()
monitor_is_off = False

while True:
    time.sleep(CHECK_INTERVAL)

    if monitor_is_off:
        if get_idle_time() < 2: 
            print("User activity detected, resuming monitoring...")
            last_change_time = time.time()
            monitor_is_off = False
        continue

    current_screenshot = capture_screen()

    dif=images_are_different(last_screenshot, current_screenshot)
    
    print(dif)
    
    if dif:
        last_change_time = time.time()
    elif time.time() - last_change_time > INACTIVITY_THRESHOLD:
        print("Turning off monitor...")
        turn_off_monitor()
        monitor_is_off = True

    last_screenshot = current_screenshot
