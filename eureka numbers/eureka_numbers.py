# eureka_numbers.py - given an inclusive range of integers, find all such integers for which
#					  the sum of their consecutive digits (from most significant down to least
#					  significant) raised to consecutive integral powers, starting with 1, is
#					  equal to the original integer itself --> that is, find all such integers
#					  that're so-called Eureka numbers.
#
# jf - 7/14

def sum_dig_power(a,b):
	'''
		Inputs:
			a: Integer
			b: Integer
		Output:
			res: List
	'''
	res = list()
	for num in range(a, b+1):
		# first, pick off the digits
		curr_num, digits = num, list()
		while curr_num > 0:
			digits.append(curr_num%10)
			curr_num = curr_num//10
		digits.reverse()
		
		# second, get the relevant sum of powered digits
		dig_sum = 0
		for idx, digit in enumerate(digits):
			dig_sum += digit**(idx+1)

		# lastly, add to the list if it's equal to the original int in question
		if dig_sum == num:
			res.append(num)

	return res

def test():
	''' unit test for sum_dig_power() '''
	tests = [
		[(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9]],
		[(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]],
		[(10, 89), [89]],
		[(10, 100),	[89]],
		[(90, 100),[]],
		[(89, 135), [89, 135]]
	]

	for test in tests:
		print("Testing:", test[0])
		val = sum_dig_power(*test[0])
		print("output:", val)
		print("answer:", test[1])
		print("======================")
		print("Correct ?", val==test[1])
		print("======================\n\n")

if __name__ == "__main__":
	test()