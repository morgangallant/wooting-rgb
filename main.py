import time
import requests
from wooting_rgb import wooting_rgb_wrapper


def wooting_connected():
    """
    Check if the Wooting keyboard is connected.
    """
    return wooting_rgb_wrapper.wooting_rgb_kbd_connected()


def set_color(red: int, green: int, blue: int):
    """
    Set the color of all keys on the Wooting keyboard.
    """
    assert wooting_connected(), "Wooting keyboard is not connected."
    for i in range(wooting_rgb_wrapper.WOOTING_ROW_COUNT):
        for j in range(wooting_rgb_wrapper.WOOTING_COLUMN_COUNT):
            wooting_rgb_wrapper.wooting_rgb_direct_set_key(i, j, red, green, blue)


def main():
    """
    Every minute, polls https://lovely.software/rgb and sets the color of the Wooting keyboard, if
    the keyboard is connected and the color is different from the current one.
    """
    last_color = None
    while True:
        if not wooting_connected():
            print("Wooting keyboard is not connected.")
            time.sleep(60)
            continue

        # Fetch the color from the API
        print("Fetching color from API...")
        try:
            response = requests.get("https://lovely.software/rgb")
            response.raise_for_status()
            json = response.json()
            red = json.get("red", 0)
            green = json.get("green", 0)
            blue = json.get("blue", 0)
            color = (red, green, blue)
            if color != last_color:
                print(f"Setting color: {color}")
                set_color(red, green, blue)
                last_color = color
            else:
                print("Color is the same, skipping update.")
        except requests.RequestException as e:
            print(f"Error fetching color: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        time.sleep(60)  # Wait for 1 minute before the next poll


if __name__ == "__main__":
    main()
