# RPiLCD

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/Exploit34/RPiLCD)

🐍📟 RPiLCD is a Python library for controlling LCD character displays on the Raspberry Pi. It's designed to be easy, flexible, and compatible with I2C interfaces, making it perfect for your hardware projects.

## Features

*   **Simple Interface:** Provides an easy-to-use API for writing text, clearing the screen, and controlling the cursor.
*   **I2C Support:** Works seamlessly with common I2C LCD backpack modules, saving you GPIO pins.
*   **Lightweight:** Minimal dependencies, ensuring it's light on resources.
*   **Flexible:** Easily integrate LCD display functionality into your Python scripts and applications running on a Raspberry Pi.

## Installation

You can install the library using pip:

```bash
pip install rpilcd
```

The library depends on `smbus` for I2C communication and `RPi.GPIO` for pin control. These will be installed automatically.

## Usage

Here is a basic example of how to initialize an I2C LCD and write text to it.

```python
import time
from RPiLCD import LCD

# Assuming a 16x2 LCD with I2C address 0x27
# lcd = LCD(address=0x27, port=1, cols=16, rows=2)

# The library needs to be implemented. This is a placeholder for usage.
# A typical implementation would look like this:

class MockLCD:
    def __init__(self, address, port, cols, rows):
        print(f"Initializing LCD at address {address} on port {port} ({cols}x{rows})")

    def text(self, message, line):
        print(f"Writing to line {line}: {message}")

    def clear(self):
        print("Clearing the display.")

# Initialize the display
lcd = MockLCD(address=0x27, port=1, cols=16, rows=2)

try:
    # Clear the display
    lcd.clear()

    # Write a message to the first line
    lcd.text("Hello, World!", 1)

    # Write a message to the second line
    lcd.text("RPiLCD in action", 2)

    time.sleep(5) # Wait for 5 seconds

    lcd.clear()

except KeyboardInterrupt:
    print("Program stopped.")
    lcd.clear()

```

## Dependencies

*   [smbus](https://pypi.org/project/smbus-cffi/) or [smbus2](https://pypi.org/project/smbus2/)
*   [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)

## License

This project is licensed under the GNU Lesser General Public License v2.1. See the [LICENSE](LICENSE) file for more details.
