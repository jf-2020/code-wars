# 1_alternating_split.py - this program completes the first simple encryption exercise of
#						   the simple encrpytion series. two functions are necessary for this,
#						   namely the encrypt() & decrypt() functions. the idea here is to
#						   from a given plaintext, extract every 2nd character, concatenate
#						   them, and take all the remaining characters, concatenate them, and
#						   to, lastly, concatenate those two concatenated substrings. This
#						   yields the ciphertext. For this particular encoding, an integer will
#						   be given indicating how many times to execute this process.
#
# jf - 7/14

from math import floor

def encrypt(text, n):
	'''
		Inputs:
			text: String
			n: Integer
		Output:
			curr_str: String
	'''

	# handle edge cases
	if not text or n <= 0:
		return text

	curr_str = text
	for _ in range(n):
		curr_str = curr_str[1::2] + curr_str[::2]

	return curr_str

def insert_into(left, right):
	'''
		Inputs:
			left: String
			right: String
		Output:
			out_str: String
	
		Notes:
			This function will take two strings, left and right, and insert the left
			string into the right string every other character at a time. In other
			words, each character of the left string will be inserted, one at a time,
			into the right string in between every character within the right string
			(i.e. starting with the 2nd position in the right string).

			Essentially, this is a helper function to be bootstrapped by the decrypt
			function.
	'''
	left_idx, right_idx = 0, 0
	out_str = ''
	# use a two-pointer method for iterating over both strings concurrently
	for i in range(len(left)+len(right)):
		if i%2 == 0:
			out_str += right[right_idx]
			right_idx += 1
		else:
			out_str += left[left_idx]
			left_idx += 1
	return out_str

def decrypt(encrypted_text, n):
	'''
		Inputs:
			encrypted_text: String
			n: Integer
		Output:
			out_str: String
	'''
	# first, handle the edge cases
	if not encrypted_text or n <= 0:
		return encrypted_text

	# then, essentially, just apply the insert_into() helper function n times
	left_substr = encrypted_text[:floor(len(encrypted_text)/2)] 
	right_substr = encrypted_text[floor(len(encrypted_text)/2):]
	out_str = ''
	for _ in range(n):
		out_str = insert_into(left_substr, right_substr)
		left_substr = out_str[:floor(len(out_str)/2)]
		right_substr = out_str[floor(len(out_str)/2):]
	return out_str

def test_decrypt():
	''' unit test for decrypt() function '''
	tests = [
		[("This is a test!", 0), "This is a test!"],
		[("hsi  etTi sats!", 1), "This is a test!"],
		[("s eT ashi tist!", 2), "This is a test!"],
		[(" Tah itse sits!", 3), "This is a test!"],
		[("This is a test!", 4), "This is a test!"],
		[("This is a test!", -1), "This is a test!"],
		[("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!"],
		[("", 0), ""],
		[(None, 0), None]
	]

	for test in tests:
		print("Testing:", test[0])
		val = decrypt(*test[0])
		print("output:", val)
		print("answer:", test[1])
		print("======================")
		print("Correct ?", val == test[1])
		print("======================\n\n")

def test_insert_into():
	''' unit test for insert_into() function '''
	test = ["hsi  etTi sats!", "This is a test!"]

	print("Testing:", test[0])
	left = test[0][:floor(len(test[0])/2)]
	right = test[0][floor(len(test[0])/2):]
	val = insert_into(left, right)
	print("output:", val)
	print("answer:", test[1])
	print("=====================")
	print("Correct ?", val == test[1])
	print("=====================\n\n")

def test_encrypt():
	''' unit test for encrypt() function '''
	tests = [
		[("This is a test!", 0), "This is a test!"],
		[("This is a test!", 1), "hsi  etTi sats!"],
		[("This is a test!", 2), "s eT ashi tist!"],
		[("This is a test!", 3), " Tah itse sits!"],
		[("This is a test!", 4), "This is a test!"],
		[("This is a test!", -1), "This is a test!"],
		[("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig"],
		[("", 0), ""],
		[(None, 0), None]
	]

	for test in tests:
		print("Testing:", test[0])
		val = encrypt(*test[0])
		print("output:", val)
		print("answer:", test[1])
		print("======================")
		print("Correct ?", val == test[1])
		print("======================\n\n")

if __name__ == "__main__":
	test_encrypt()
	# test_insert_into()
	# test_decrypt()