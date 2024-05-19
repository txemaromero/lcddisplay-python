import I2C_LCD_driver, sys
from time import sleep

if len(sys.argv) == 2:
    mylcd = I2C_LCD_driver.lcd()
    mylcd.lcd_display_string(sys.argv[1], 1)

    sleep(1)

    mylcd.lcd_clear()
    mylcd.lcd_display_string("Clear screen", 1)

    sleep(1)

    mylcd.lcd_clear()
