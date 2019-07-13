# convert_from_base64.py - given an input string, encoded in base64, the prgm will convert back
#						   into its original unencoded ASCII string
#
# jf - 7/13

def from_base_64(s):
	'''
		Input:
			s: String
		Output:
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

	# invert base64 alphabet mapping
	d = {value: key for key, value in d.items()}

	# first, get list of decimal values to convert to binary from b64 string via reverse lookup
	dec_vals = list()
	for char in s:
		dec_vals.append(d[char])

	# second, convert each such decimal into binary and concatenate to overall working binary
	# string
	t = ''
	for dec in dec_vals:
		# pad with leading 0s, if necessary
		q = bin(dec)[2:]
		while len(q) < 6:
			q = '0' + q
		t += q

	# lastly, convert each byte to ASCII, building out the final, decoded string
	out = ''
	for i in range(len(t)//8):
		curr_byte = t[i*8:(i+1)*8]
		curr_sum = 0
		for idx, bit in enumerate(curr_byte):
			curr_sum += (2**(7-idx)) * int(bit)
		out += chr(curr_sum)

	# and then return the final string
	return out

def test():
	''' unit test for from_base_64() '''

	tests = [
		["this is a string!!","dGhpcyBpcyBhIHN0cmluZyEh"],
		["this is a test!","dGhpcyBpcyBhIHRlc3Qh"],
		["now is the time for all good men to come to the aid of their country.","bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
		["1234567890  ", "MTIzNDU2Nzg5MCAg"],
		["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
		["the quick brown fox jumps over the white fence. ","dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
		["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4","ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
		["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna","VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
		["TVRJek5EVTJOemc1TUNBZyAg","VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"]
	]

	for count, t in enumerate(tests):
		print("==========Test " + str(count) + "===========")
		print("encoded:", t[1])
		val = from_base_64(t[1])
		print("decoded:", val)
		print("===========================")
		print("Correct?", val == t[0])
		print("===========================\n\n")

if __name__ == "__main__":
	test()