from smbus import SMBus
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ALIGN_OPTIONS = {
    'left': 'ljust',
    'right': 'rjust',
    'center': 'center'
}

CLEAR_DISPLAY = 0x01
ENABLE_BIT = 0b00000100
LINES = {
    1: 0x80,
    2: 0xC0,
    3: 0x94,
    4: 0xD4
}

LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00

class I2C:
    def __init__(self, address, width, rows, bus=1, backlight=True):
        """Inicializa el LCD con la dirección I2C, dimensiones y retroiluminación."""
        self.address = address
        self.bus = SMBus(bus)
        self.width = width
        self.rows = rows
        self.backlight_status = backlight
        self.delay = 0.0005

        self.initialize_display()

    def update_config(self, address=None, bus=None, width=None, rows=None, backlight=None):
        """Permite cambiar las variables de configuración del LCD."""
        if address is not None:
            self.address = address
        if bus is not None:
            self.bus = SMBus(bus)
        if width is not None:
            self.width = width
        if rows is not None:
            self.rows = rows
        if backlight is not None:
            self.backlight_status = backlight

        self.initialize_display()

    def initialize_display(self):
        """Envía comandos de inicialización al LCD."""
        init_commands = [0x33, 0x32, 0x06, 0x0C, 0x28, CLEAR_DISPLAY]
        for cmd in init_commands:
            self.write(cmd)
            sleep(self.delay)

    def _write_byte(self, byte):
        """Escribe un byte en el bus con el modo de habilitación activado."""
        try:
            self.bus.write_byte(self.address, byte)
            self.bus.write_byte(self.address, (byte | ENABLE_BIT))
            sleep(self.delay)
            self.bus.write_byte(self.address, (byte & ~ENABLE_BIT))
            sleep(self.delay)
        except Exception as e:
            logger.error(f"Error al escribir byte: {e}")

    def write(self, byte, mode=0):
        """Escribe un comando o dato al LCD, considerando el estado de retroiluminación."""
        backlight_mode = LCD_BACKLIGHT if self.backlight_status else LCD_NOBACKLIGHT
        self._write_byte(mode | (byte & 0xF0) | backlight_mode)
        self._write_byte(mode | ((byte << 4) & 0xF0) | backlight_mode)

    def display_text(self, text, line=1, align='left'):
        """Muestra texto en una línea específica con el alineamiento indicado."""
        if line not in LINES:
            raise ValueError("Número de línea no válido. Debe ser 1, 2, 3 o 4.")
        
        if not isinstance(self.width, int) or self.width <= 0:
            raise ValueError("Ancho inválido para la pantalla LCD.")
        
        if not isinstance(self.rows, int) or self.rows <= 0:
            raise ValueError("Número de filas inválido para la pantalla LCD.")

        self.write(LINES[line])
        aligned_text = getattr(text[:self.width], ALIGN_OPTIONS.get(align, 'ljust'))(self.width)

        for char in aligned_text:
            self.write(ord(char), mode=1)

    def toggle_backlight(self, turn_on=True):
        """Activa o desactiva la retroiluminación del LCD."""
        self.backlight_status = turn_on
        self.write(0x00)

    def _split_text(self, text):
        """Divide el texto para que quepa en líneas, intentando romper en espacios."""
        words = text.split(' ')
        lines = []
        current_line = ''

        for word in words:
            if len(current_line) + len(word) + 1 <= self.width:
                current_line += ' ' + word if current_line else word
            else:
                lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)
        return lines

    def clear(self):
        """Limpia la pantalla del LCD."""
        self.write(CLEAR_DISPLAY)
        sleep(self.delay)