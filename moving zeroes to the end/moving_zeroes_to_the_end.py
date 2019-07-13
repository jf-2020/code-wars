def move_zeros(array):
	# utilized two pointers to solve problem
	idx, count = 0, 0
	# one for counting thru total # elems in arg list
	while count < len(array):
		# the other to keep track of where actual curr idx
		# is for comparing to 0
		if array[idx] == 0:
			# if curr val is 0, then pop off & add to end
			item = array.pop(idx)
			array.append(item)
		else:
			# otherwise, simply bump up the index
			idx += 1
		# and always bump up the count index
		count += 1
	return array

def test():
	tests = [
				([1,2,0,1,0,1,0,3,0,1],[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ]),
				([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9],[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]),
				(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9],["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]),
				(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9],["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]),
				([0,1,None,2,False,1,0],[1,None,2,False,1,0,0]),
				(["a","b"],["a","b"]),
				(["a"],["a"]),
				([0,0],[0,0]),
				([0],[0]),
				([False],[False]),
				([],[])
			]

	# for test in tests:
	# 	print("===testing===")
	# 	print("test[0]:", test[0])
	# 	print(move_zeros(test[0]), "\n")

	print("===testing===")
	print("tests[0][0]:", tests[0][0])
	print(move_zeros(tests[0][0]), "\n")


def main():
	test()

if __name__ == "__main__":
	main()