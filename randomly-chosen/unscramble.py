import random

seq="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678"

# Obtain the file from:
# https://github.com/DownUnderCTF/Challenges_2023_Public/blob/main/beginner/randomly-chosen/src/output.txt
f = open("output.txt", "r");
scrambled = f.readline()
f.close()

# Brute force possible seed values
# See "2 - Trying everything and seeing what fits"
seeds = []
for x in range(0,1338):
	random.seed(x);
	out = ''.join(random.choices(seq, k=len(seq)*5))
	if [scrambled.find(c) for c in "DUCTF"] == [out.find(c) for c in "abcde"]:
		seeds.append(out)
		print(f"Found Match: {x}")

l = len(seeds)
print(f"{l} Possible seed{'s' if l!=1 else ''}.")

# Reconstruct the Flag
# See "3 - Reconstructing the flag"
if l > 1:
	print(f"More than one seed, cannot solve.")
elif l == 1:
	key = seeds[0]
	original = ""
	for char in seq:
		original += scrambled[key.find(char)]
	print(f"Flag is: {original}")
else:
	print(f"How did we get here?")
