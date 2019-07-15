# data_reverse.py - given a list of bits, whose total length is a multiple of 8, this prgm
#					will reverse the order of said bits by byte with its symmetric position
#					on the opposite end of the bit list.
#
# jf - 7/15

def reverse_bytes(l):
	'''
		Input:
			l: List
		Output:
			res: List
	'''
	# recursive implementation
	if len(l) <= 8:
		return l
	else:
		return l[-8:] + reverse_bytes(l[8:len(l)-8]) + l[:8]

def test_reverse_bytes():
	''' unit test for reverse_bytes() '''
	data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
	data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
	data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
	data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]

	tests = [(data1, data2), (data3, data4)]

	for test in tests:
		print("Testing:", test[0])
		val = reverse_bytes(test[0])
		print("output:", val)
		print("answer:", test[1])
		print("=====================================================")
		print("Correct ?", val == test[1])
		print("=====================================================\n\n")

if __name__ == "__main__":
	test_reverse_bytes()