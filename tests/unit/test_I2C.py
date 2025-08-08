import unittest
from unittest.mock import patch, MagicMock
from src.RPiLCD import I2C

class testI2C(unittest.TestCase):
    @patch('src.RPiLCD.I2CRasp.SMBus') 
    def test_init(self, mock_smbus):
        mock_bus_instance = MagicMock()
        mock_smbus.return_value = mock_bus_instance

        i2c = I2C(address=0x27, width=16, rows=2)
        self.assertIsNotNone(i2c)
        mock_smbus.assert_called_once_with(1)

if __name__ == "__main__":
    unittest.main()
