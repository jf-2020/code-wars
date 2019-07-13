# convert_to_base64.py - given an input string, s, the prgm converts to a base64 encoded
#						 ASCII string via the non-padded encoding method. it assumes that
#						 all input strings are of byte count multiples of 6, so that no
#						 special processing is necessary for final bytes.
#
# jf - 7/13

def to_base_64(s):
	''' 
		Input::
			s: String
		Output::
			out: String
	'''

	####################
	### BASE 64 ALPHABET
	####################
	d = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'N',
        14: 'O',
        15: 'P',
        16: 'Q',
        17: 'R',
        18: 'S',
        19: 'T',
        20: 'U',
        21: 'V',
        22: 'W',
        23: 'X',
        24: 'Y',
        25: 'Z',
        26: 'a',
        27: 'b',
        28: 'c',
        29: 'd',
        30: 'e',
        31: 'f',
        32: 'g',
        33: 'h',
        34: 'i',
        35: 'j',
        36: 'k',
        37: 'l',
        38: 'm',
        39: 'n',
        40: 'o',
        41: 'p',
        42: 'q',
        43: 'r',
        44: 's',
        45: 't',
        46: 'u',
        47: 'v',
        48: 'w',
        49: 'x',
        50: 'y',
        51: 'z',
        52: '0',
        53: '1',
        54: '2',
        55: '3',
        56: '4',
        57: '5',
        58: '6',
        59: '7',
        60: '8',
        61: '9',
        62: '+',
        63: '/'
	}
	####################
	####################
	####################

	# first, convert the input string into its binary string equivalent
	t = ''
	for char in s:
		q = bin(ord(char))[2:]
		# pad the most significant bit(s) if necessary
		if len(q) < 8:
			while len(q) < 8:
				q = '0' + q
		t += q
	# t now contains the binary string equivalent of the given input string

	# next, loop thru the binary string in 6-bit increments, converting the underlying
	# binary repr into its decimal equivalent. keep track of these conversions, in order,
	# in a list, because they will be used as lookups in the base64 alphabet mapping.
	b64_vals = list()
	for i in range(len(t)//6):
		curr_str = t[i*6:(i+1)*6]
		## get the decimal value as stated above
		curr_sum = 0
		for idx, bit in enumerate(curr_str):
			curr_sum += (2**(5-idx)) * int(bit)
		## as well, keep track, in order, of said values
		b64_vals.append(curr_sum)
	# b64_vals now has all the indices to be used as lookups into the base64 alphabet

	# lastly, build out the base64 encoded string via successive lookups into alphabet
	out = ''
	for val in b64_vals:
		out += d[val]

	# and return it
	return out

def test():
	''' unit test for to_base_64() '''

	tests = [
		["this is a string!!","dGhpcyBpcyBhIHN0cmluZyEh"],
		["this is a test!","dGhpcyBpcyBhIHRlc3Qh"],
		["now is the time for all good men to come to the aid of their country.","bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
		["1234567890  ", "MTIzNDU2Nzg5MCAg"],
		["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
		["the quick brown fox jumps over the white fence. ","dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
		["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4","ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
		["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna","VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
		["TVRJek5EVTJOemc1TUNBZyAg","VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"],
		['0UKGc7Gfr2w', 'MFVLR2M3R2ZyMnc']
	]

	for count, t in enumerate(tests):
		print("==========Test " + str(count) + "===========")
		print("input:", t[0])
		val = to_base_64(t[0])
		print("output:", val)
		print("===========================")
		print("Correct?", val == t[1])
		print("===========================\n\n")

if __name__ == "__main__":
	test()