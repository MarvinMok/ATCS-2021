def twoSum(nums = [3,2,4], target = 6):
	s = set([])
	i = 0
	while i < len(nums):
		if target - nums[i] not in s:
			s.add(nums[i])
		else:
			return i, nums.index(target - nums[i])
		i += 1
	return (, )

print(twoSum())