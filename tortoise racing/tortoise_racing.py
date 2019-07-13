# tortoise_racing.py - given v1, v2 & g (a lead distance for object 1), at what time (hrs, mins, secs)
#					   will object 2 pass object 1?
#
# jf - 7/13

def race(v1, v2, g):
	'''
		Inputs:
			v1: Integer
			v2: Integer
			g: Integer
		Output:
			out: List of three Integers
	'''

	if v1 > v2:
		return None
	else:
		d1, d2 = g, 0
		secs = 0
		s1, s2 = v1/(60**2), v2/(60**2)
		while d1 > d2:
			secs += 1
			d1, d2 = d1 + s1, d2 + s2
		mins = secs//60
		hrs = mins//60
		mins = mins%60
		secs = secs%60 - 1
		if secs == -1:
			secs = 0
		out = [hrs, mins, secs]
		return out

def test():
	''' unit test for race() '''
	tests = [
		[[720, 850, 70], [0, 32, 18]],
		[[80, 91, 37], [3, 21, 49]],
		[[80, 100, 40], [2, 0, 0]]
	]

	for test in tests:
		print("Testing:", test[0])
		val = race(*test[0])
		print("time:", val)
		print("=============\n\n")

if __name__ == "__main__":
	test()