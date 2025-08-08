import unittest
from unittest.mock import patch, MagicMock
from src.RPiLCD import I2C

class testDisplay(unittest.TestCase):
    @patch('src.RPiLCD.I2CRasp.SMBus')
    def test_write_text(self, mock_smbus):
        mock_bus_instance = MagicMock()
        mock_smbus.return_value = mock_bus_instance

        lcd = I2C(address=0x27, width=16, rows=2)
        self.assertIsNotNone(lcd)
        mock_smbus.assert_called_once_with(1)

        lcd.display_text("Hello Juan", line=1, align="left")
        lcd.display_text("LCD", line=2, align="center")
        lcd.display_text("LCD Display", line=3, align="right")
        lcd.display_text("4 buses", line=4, align="center")

if __name__ == "__main__":
    unittest.main()
