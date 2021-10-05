d = {"Everest": 29029, "K2": 28251, "Lhtose": 27940, "Makalu": 27838, "Cho Oyu": 26864}
print("these are names.")
for n in d.keys():
	print(n)
print("")
print("these are heights.")
for e in d.values():
	print(e)
print("")
print("these are names of mountains and their heights.")
for k, v in d.items():
	print(k + " is " + str(v) + " meters tall.")
