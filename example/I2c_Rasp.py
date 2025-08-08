from RPiLCD import I2C
from time import sleep

lcd = I2C(address=0x27, width=16, rows=2)

lcd.clear()

lcd.display_text("Hello everyone", line=1, align="left")

sleep(2)

lcd.display_text("Welcome people!", line=2, align="center")

lcd.toggle_backlight(False)
sleep(1)

lcd.toggle_backlight(True)

lcd.clear()

