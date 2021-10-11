r1 = "qwertyuiop"
r2 = "asdfghjkl"
r3 =  "zxcvbnm"
r = None

def findWords(words):
	final = []
	for word in words:
		t = word.lower()
		b = True
		if t[0] in r1:
			r = r1
		elif t[0] in r2:
			r = r2
		else:
			r = r3

		i = 1
		while b and i < len(word):
			if t[i] not in r:
				b = False

			i += 1
		if b:
			final.append(word)
	return final

print(findWords(["Hello","Alaska","Dad","Peace"]))

