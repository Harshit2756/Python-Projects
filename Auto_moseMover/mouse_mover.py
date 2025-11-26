import pyautogui
import random
import time
from pynput import keyboard

# Flag to control the mouse movement
running = True

# List of random texts to type
random_texts = [
    "hello",
    "testing",
    "working",
    "active",
    "running"
]

def on_press(key):
    global running
    if key == keyboard.Key.esc:
        running = False
        return False  # Stop listener

# Create keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Ensure a safe exit is possible
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5  # Add a pause between actions

# Get screen size
screen_width, screen_height = pyautogui.size()

# Define safe area (avoiding taskbar and top menu)
TASKBAR_HEIGHT = 70  # Typical taskbar height
TOP_MARGIN = 50      # Avoid top of screen
safe_top = TOP_MARGIN
safe_bottom = screen_height - TASKBAR_HEIGHT
safe_left = 20
safe_right = screen_width - 20

print("Mouse mover started. Press ESC to stop.")

try:
    while running:
        # Choose a random action: 1=move, 2=click, 3=type
        action = random.randint(1, 3)
        
        # Generate random coordinates within safe boundaries
        x = random.randint(safe_left, safe_right)
        y = random.randint(safe_top, safe_bottom)
        
        if action == 1:
            # Just move
            pyautogui.moveTo(x, y, duration=1)
        
        elif action == 2:
            # Move and click
            pyautogui.moveTo(x, y, duration=1)
            pyautogui.click()
        
        else:
            # Move, click and type
            pyautogui.moveTo(x, y, duration=1)
            pyautogui.click()
            text = random.choice(random_texts)
            pyautogui.write(text, interval=0.1)
            # pyautogui.press('enter')
        
        # Wait between actions
        time.sleep(random.uniform(1, 3))

except Exception as e:
    print(f"\nError: {e}")

print("\nScript stopped")