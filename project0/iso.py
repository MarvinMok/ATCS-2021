def isIsomorphic(s,t):
	if len(s) != len(t):
		return False
	else:
		ds = {}
		dt = {}
		for i in range(0, len(t)):
			if s[i] in ds and ds[s[i]] != t[i]: 
				return False
			elif t[i] in dt and dt[t[i]] != s[i]:
				return False
			else:
				ds[s[i]] =  t[i]
				dt[t[i]] = s[i]		
				
		return True

s = input("word1 ")
t = input("word2 ")
print (isIsomorphic(s, t))
