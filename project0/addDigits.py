def addDigits(num = 38):
	if num < 10:
		return num
	else:
		return addDigits(sum(divmod(num, 10)))


print(addDigits())