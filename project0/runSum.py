def runSum(nums):
	l = []
	s = 0
	for n in nums:
		s += n
		l.append(s)
	return l