def isValid(s =  "(]"):
	openP = []
	dOpen = { '(' : ')', '[': ']', '{': '}' }
	close = ')}]'
	for ch in s:
		if ch in dOpen.keys():
			openP.append(ch)
		elif ch in close:
			if not openP:
				return False
			if dOpen[openP.pop()] != ch:
				return False
	if openP: 
		return False
	else:
		return True

print(isValid())

