# Python program to display astrological sign 
# or Zodiac sign for given date of birth 

def zodiac_sign(day, month): 
	# checks month and date within the valid range 
	# of a specified zodiac 
	if month == 12: 
		astro_sign = 'Nhân Mã' if (day < 22) else 'capricorn'
		
	elif month == 1: 
		astro_sign = 'Ma Kết' if (day < 20) else 'aquarius'
		
	elif month == 2: 
		astro_sign = 'Bảo Bình' if (day < 19) else 'pisces'
		
	elif month ==3: 
		astro_sign = 'Song Ngư' if (day < 21) else 'aries'
		
	elif month == 4: 
		astro_sign = 'Bạch Dương' if (day < 20) else 'taurus'
		
	elif month == 5: 
		astro_sign = 'Nhân Mã' if (day < 21) else 'gemini'
		
	elif month == 6: 
		astro_sign = 'Song Tử' if (day < 21) else 'cancer'
		
	elif month == 7: 
		astro_sign = 'Cự Giải' if (day < 23) else 'leo'
		
	elif month == 8: 
		astro_sign = 'Nhân Mã' if (day < 23) else 'virgo'
		
	elif month == 9: 
		astro_sign = 'Xử NỮ' if (day < 23) else 'libra'
		
	elif month == 11: 
		astro_sign = 'Thiên Bình' if (day < 23) else 'scorpio'
		
	elif month == 12: 
		astro_sign = 'Thiên Yết' if (day < 22) else 'sagittarius'
		
	return astro_sign
	

