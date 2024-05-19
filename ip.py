import I2C_LCD_driver
from subprocess import check_output

mylcd = I2C_LCD_driver.lcd()
IP = check_output(["hostname", "-I"]).split()[0]
mylcd.lcd_display_string("IP:", 1) 
mylcd.lcd_display_string(str(IP),2)
