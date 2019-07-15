# playing_with_passphrases.py - this prgm will transform a given input string (also, an integer is
#								given as well), using the following rules:
#									1. for each letter, perform an alphabetic shift by the given
#									integral amount.
#									2. replace each digit by it's digit complement to 9 (i.e. if
#									it's 7 then 7 -> 2, which is 9-7).
#									3. don't transform (other than perhaps its position within the
#									passphrase) any nonalphabetic or nondigit characters.
#									4. lowercase each odd position letter &, likewise, uppercase
#									each even position character.
#									5. lastly, reverse the entire transformed passphrase.
#
# jf - 7/15

from string import ascii_letters as letters
from string import digits

def play_pass(s, n):
	'''
		Input:
			s: String
			n: Integer
		Output:
			res: String
	'''
	# handle edge cases
	if not s or n<0:
		return s

	# handle the first transformation
	res = rotate_by_n(s, n)
	# then the second transformation
	res = digit_complement(res)
	# then the fourth transformation
	res = lower_odd_and_upper_even(res)
	# lastly, return the string reversed
	return res[::-1]

def lower_odd_and_upper_even(s):
	'''
		Input:
			s: String
		Output:
			res: String
	'''
	# handle edge case
	if not s:
		return s

	res = ''
	for i in range(len(s)):
		# if it's not a letter, skip it
		if s[i] not in letters:
			res += s[i]
		else:
			# if position is even, make it uppercase
			if i%2 == 0:
				res += s[i].upper()
			# otherwise, it's odd, so make it lowercase
			else:
				res += s[i].lower()
	return res

def digit_complement(s):
	'''
		Input:
			s: String
		Output:
			res: String
	'''
	# handle edges case:
	if not s:
		return s

	res = ''
	for char in s:
		if char not in digits:
			res += char
		else:
			res += str(9-int(char))
	return res

def rotate_by_n(s, n):
	'''
		Input:
			s: String
			n: Integer
		Output:
			res: string
	'''
	# handle edge cases
	if not s or n<=0:
		return s

	res = ''
	for char in s:
		if char not in letters:
			res += char
		else:
			# get ascii value
			ascii_value = ord(char)
			# handle whether lower or upper
			if ascii_value >= ord('a'):
				# then, it's lowercase
				ascii_value -= ord('a')
				# rotate
				ascii_value = (ascii_value + n) % 26
				# readjust to appropriate ascii position
				ascii_value += ord('a')
			else:
				# otherwise, it's uppercase
				ascii_value -= ord('A')
				# rotate
				ascii_value = (ascii_value + n) % 26
				# readjustto appropriate ascii position
				ascii_value += ord('A')
			res += chr(ascii_value)
	return res

def test_lower_odd_and_upper_even():
	''' unit test for lower_odd_and_upper_even() '''
	
	tests = [
		['abc', 'AbC'],
		['', ''],
		['ABC', 'AbC'],
		['aBCdEFgh', 'AbCdEfGh']
	]

	for test in tests:
		print("Testing:", test[0])
		val = lower_odd_and_upper_even(test[0])
		print("output:", val)
		print("answer:", test[1])
		print("=======================")
		print("Correct ?", val == test[1])
		print("=======================\n\n")

def test_rotate_by_n():
	'''unit test for rotate_by_n() '''

	tests = [
		[('abc',3), 'def'],
		[('Z', 26), 'Z'],
		[('aBc', 3), 'dEf'],
		[('', 10), ''],
		[('abc', 0), 'abc'],
		[('abc', -1), 'abc'],
		[('abc abc abc', 3), 'def def def'],
		[('aBc DeF!/3', 5), 'fGh IjK!/3']
	]

	for test in tests:
		print("Testing:", test[0])
		val = rotate_by_n(*test[0])
		print("output:", val)
		print("answer:", test[1])
		print("=========================")
		print("Correct ?", val == test[1])
		print("=========================\n\n")

def test_play_pass():
	''' unit test for play_pass() '''

	tests = [
		[("BORN IN 2015!", 1), "!4897 Oj oSpC"],
		[("I LOVE YOU!!!", 1), "!!!vPz fWpM J"],
		[("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2),
			"4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO"],
		[('I LOVE YOU!!!', 0), '!!!uOy eVoL I']
	]

	for test in tests:
		print("Testing:", test[0])
		val = play_pass(*test[0])
		print("output:", val)
		print("answer:", test[1])
		print("=======================================================")
		print("Correct ?", val == test[1])
		print("=======================================================\n\n")

if __name__ == "__main__":
	# test_rotate_by_n()
	# test_lower_odd_and_upper_even()
	test_play_pass()