import I2C_LCD_driver, os
from time import strftime

hostname = "google.com"
response = os.system("ping -c 1 " + hostname) 

mylcd = I2C_LCD_driver.lcd()

if response == 0: 
    mylcd.lcd_display_string(hostname + " is up!")
else: 
    mylcd.lcd_display_string(hostname + " is down!")
    mylcd.lcd_display_string("Hour: %s" %strftime("%H:%M:%S"), 3)
    mylcd.lcd_display_string("Date: %s" %strftime("%m/%d/%Y"), 4)
