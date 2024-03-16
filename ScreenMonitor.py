import time
import pyautogui
import pygetwindow as gw
import os

def take_screenshot(window, timestamp):
    # Replace invalid characters in the window title
    sanitized_title = ''.join(char for char in window.title if char.isalnum() or char in (' ', '-', '_'))
    # Take a screenshot of the active window
    screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))
    # Save the screenshot to a file using the sanitized title and timestamp
    screenshot.save(f"screenshots/{sanitized_title}_{timestamp}.png")

def monitor_active_window():
    # Get the current active window
    current_window = gw.getActiveWindow()
    # Record the start time
    start_time = time.time()
    # Record the end time
    end_time = start_time + 60 * 60  # 60 minutes
    # Variable to store the time of the last window change
    last_window_change_time = start_time
    # Variable to store the total elapsed time
    total_elapsed_time = 0

    # Monitor the active window and take a screenshot when the active windo1w changes
    while time.time() < end_time:
        # Get the current active window
        new_window = gw.getActiveWindow()

        # If the active window has changedndsvnkasacnk
        if new_window != current_window:
            # Wait for 0.5 seconds to ensure that the new window is stable
            time.sleep(0.5)
            # Check if the title has changed (indicating a window change)
            if new_window.title != current_window.title:
                # Take a screenshot of the old window
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                take_screenshot(current_window, timestamp)
                # Record the time of the window change
                last_window_change_time = time.time()
                # Record the new active window

        # Check if the code running window is active
        code_running_window = gw.getWindowsWithTitle("Your Code Running Window Title")
        if code_running_window and code_running_window[0] == current_window:
            # Take a screenshot when returning to the code running window
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            take_screenshot(current_window, timestamp)

        # Calculate the total elapsed time
        total_elapsed_time = time.time() - start_time

        # Sleep for 1 second to prevent high CPU usage
        time.sleep(10)

    print(f"Total elapsed time: {total_elapsed_time} seconds")

if __name__ == "__main__":
    # Create a folder to save the screenshots
    os.makedirs("screenshots", exist_ok=True)
    # Monitor the active window and take a screenshot when the active window changes
    monitor_active_window()
