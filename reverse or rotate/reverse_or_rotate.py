# reverse_or_rotate.py - given a string and an integer, this program will chunk the string
#						 into substrings of the size of said integer, with the final chunk
#						 being ignored if it's less than said size. next, for each such
#						 substring, if itself is an integer AND the sum of the cubes of its
#						 digits is even, then it will reverse that chunk, otherwise it will
#						 rotate it left by one position. then, it'll concatenate all the
#						 subtstrings, returning the result.
#
# jf - 7/15

def get_chunks(s, n):
	'''
		Input:
			s: String
			n: Integer
		Output:
			res: List
	'''
	res = list()

	# handle edge cases
	if not s or n<=0 or n>len(s):
		res.append("")
		return res

	for i, _ in enumerate(range(len(s)//n)):
		res.append(s[i*n:(i+1)*n])
	return res

def get_digits(s):
	'''
		Input:
			s: String
		Output:
			digits: List
	'''
	num = int(s)
	digits = list()
	for _ in range(len(s)):
		digit = num%10
		digits.append(digit)
		num = num//10
	return digits

def is_sum_of_cubes_of_digits_even(s):
	'''
		Input:
			s: String
		Output:
			anonymous: Boolean
	'''
	digits = get_digits(s)
	return sum(digit**3 for digit in digits)%2 == 0

def reverse_or_rotate(s, n):
	'''
		Input:
			s: String
			n: Integer
		Output:
			res: String
	'''
	# first, chunk the input
	chunks = get_chunks(s, n)
	# and check the edge cases,
	if len(chunks)==1 and not chunks[0]:
		return chunks[0]

	# second, loop over chunks, checking whether or not to reverse or rotate
	# substring by given conditions (via helpers)
	res = ''
	for chunk in chunks:
		if is_sum_of_cubes_of_digits_even(chunk):
			res += chunk[::-1]
		else:
			res += chunk[1:] + chunk[0]
	return res

def test_reverse_or_rotate():
	''' unit test for reverse_or_rotate() '''
	tests =	[
		[("1234", 0), ""],
		[("", 0), ""],
		[("1234", 5), ""],
		[("733049910872815764", 5), "330479108928157"],
		[("123456987654", 6), "234561876549"],
		[("123456987653", 6), "234561356789"],
		[("66443875", 4), "44668753"],
		[("66443875", 8), "64438756"],
		[("664438769", 8), "67834466"],
		[("123456779", 8), "23456771"],
		[("", 8), ""],
		[("123456779", 0), "" ],
		[("563000655734469485", 4), "0365065073456944"]
	]

	for test in tests:
		print("Testing:", test[0])
		val = reverse_or_rotate(*test[0])
		print("output:", val)
		print("answer:", test[1])
		print("================================")
		print("Correct ?", val == test[1])
		print("================================\n\n")

def test_get_chunks():
	''' unit test for get_chunks() '''

	tests = [
		[("123456987654", 6), ["123456", "987654"]],
		[("123456987653", 6), ["123456", "987653"]],
		[("66443875", 4), ["6644", "3875"]],
		[("66443875", 8), ["66443875"]],
		[("664438769", 8), ["66443876"]],
		[("123456779", 8), ["12345677"]],
		[("", 8), [""]],
		[("123456779", 0), [""]],
		[("563000655734469485", 4), ["5630", "0065", "5734", "4694"]]
	]

	for test in tests:
		print("Testing:", test[0])
		val = get_chunks(*test[0])
		print("output:", val)
		print("answer:", test[1])
		print("=======================")
		print("Correct ?", val == test[1])
		print("=======================\n\n")

if __name__ == "__main__":
	# test_get_chunks()
	test_reverse_or_rotate()