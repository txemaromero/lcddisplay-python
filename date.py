import I2C_LCD_driver
from time import strftime, sleep

mylcd = I2C_LCD_driver.lcd()
while True:
    mylcd.lcd_display_string("Hour: %s" %strftime("%H:%M:%S"), 1)
    mylcd.lcd_display_string("Date: %s" %strftime("%m/%d/%Y"), 2)

    sleep(1)
