import I2C_LCD_driver, sys
from time import sleep 

if len(sys.argv) == 2:
    mylcd = I2C_LCD_driver.lcd()
    while True:
        mylcd.lcd_display_string(sys.argv[1], 1)
        sleep(3)
        mylcd.lcd_clear()
        sleep(3)
