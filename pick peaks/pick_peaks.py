# pick_peaks.py - this prgm will find all local maxima (i.e. peaks) of a given input
#				  array of ints. first & last values can't be maxima and it'll take care
#				  of potential plateaus (i.e. saddle points).
#
# jf - 7/15

def pick_peaks(arr):
	'''
	Input:
		arr: List
	Output:
		res: Dictionary
	'''
	res = {'pos': list(), 'peaks': list()}

	# handle edge cases
	if not arr:
		return res

	for idx, num in enumerate(arr[1: len(arr)-1]):
		prev_val, next_val = arr[idx], arr[idx+2]
		#first, check if it's a valid peak
		if num>prev_val and num>next_val:
			res['pos'].append(idx+1)
			res['peaks'].append(num)
		# check if num <= next_val, in which case we must examine whether or not it's
		# a plateau
		elif num>prev_val:
			# if indeed it's less than the next_val, then it's not a peak
			if num<next_val:
				continue
			# otherwise, check whether or not it's a plateau
			else:
				if not is_plateau(arr[idx+1:]):
					# then add it to the list of peaks
					res['pos'].append(idx+1)
					res['peaks'].append(num)
				else:
					# otherwise, it is a plateau, so continue
					continue
	return res

def is_plateau(lst):
	'''
	Input:
		lst: List
	Output:
		res: Boolean
	'''
	num = lst[0]
	for val in lst[1:]:
		if num == val:
			# still within a potential plateau, so move to next value
			continue
		elif num > val:
			# it's not a peak
			return False
		else:
			# num < value, which means it is a plateau
			return True
	# if made through entire array, then we will call it an edge plateau
	return True

def test_pick_peaks():
	''' unit test for pick_peaks() '''

	tests = [
		[[1,2,3,6,4,1,2,3,2,1], {"pos":[3,7], "peaks":[6,3]}],
		[[3,2,3,6,4,1,2,3,2,1,2,3], {"pos":[3,7], "peaks":[6,3]}],
		[[3,2,3,6,4,1,2,3,2,1,2,2,2,1], {"pos":[3,7,10], "peaks":[6,3,2]}],
		[[2,1,3,1,2,2,2,2,1], {"pos":[2,4], "peaks":[3,2]}],
		[[2,1,3,1,2,2,2,2], {"pos":[2], "peaks":[3]}]
	]

	for test in tests:
		print("Testing:", test[0])
		val = pick_peaks(test[0])
		pos, peaks = test[1]['pos'], test[1]['peaks']
		print("output:", val)
		print("answer:", test[1])
		print("====================================")
		print("Correct ?", val['pos'] == pos and val['peaks'] == peaks)
		print("====================================\n\n")

if __name__ == "__main__":
	test_pick_peaks()