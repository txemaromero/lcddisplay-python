import I2C_LCD_driver, sys

if len(sys.argv) == 2:
	mylcd = I2C_LCD_driver.lcd()
	mylcd.lcd_display_string(sys.argv[1], 1)
	print(sys.argv[1])
