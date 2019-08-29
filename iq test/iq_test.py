# iq_test.py - given a string of ints, this prgm will compute which of said ints
#			 is of different parity than the rest, returning the resultant index
#			 + 1
#
# jf - 8/29

# assume given string of ints has already been parsed into arr of valid ints
def iq_test(arr):
	'''
	input:
		arr -> List of ints
	output:
		res -> Tuple of ints
	'''

	#############
	# can use bitwise and to test whether or odd. if odd '&'ed with 1,
	# then 1, else 0
	#############

	# store current parity -> to use either 0,1 w/0 == even & 1 == odd
	curr = 0
	# running sum
	total = 0
	# parity
	parity = ''
	# the result
	res = (0, 0)

	# if arr has 2 or less elems, then just return...for now (TODO)
	if len(arr) < 3:
		return res

	# then, first three elements will yield overall parity
	for i in range(3):
		curr = arr[i] & 1
		total += curr	

	# parity is even if either 0 or 1
	if total == 0 or total == 1:
		parity = 'e'
	# otherwise it's odd for 2 or 3
	else:
		parity = 'o'

	print("\ntotal:", total)
	print("parity:", parity, "\n")

	# now iterate over and yield first result with doesn't correspond with
	# the parity
	for idx, i in enumerate(arr):
		curr = i & 1
		if parity == 'e':
			if not curr:
				continue
			else:
				res = (idx + 1, i)
				break
		elif parity == 'o':
			if curr == 1:
				continue
			else:
				res = (idx + 1, i)
				break

	return res

def parse_input(ipt):
	'''
	input:
		ipt -> String of ints
	output:
		res -> List of ints

	'''
	res = [int(e) for e in ipt.split(' ')]
	return res

def test():
	tests = [
			("2 4 7 8 10", 3), 
			("1 2 2", 1), 
			('49 3 19 43 43 46 3 7 19 7 23 27 51 5 41 31 43 1 15 41 21 7 41 41 51 1 23 25 21 17 39', 6)
	]

	for test in tests:
		print("============================")
		print("-> Testing:", test)
		curr_test = parse_input(test[0])
		print("calling: iq_test(" + str(curr_test) +  ")")
		res = iq_test(curr_test)
		print("answer:", res)
		print("-> Correct:", res[0] == test[1])
		print()

if __name__ == "__main__":
	test()