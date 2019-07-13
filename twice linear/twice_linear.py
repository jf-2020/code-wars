def dbl_linear(n):
	u, count = [0], 0
	while len(u) < 2*n:
		# print("len(u):", len(u))
		x = u[count]
		# print("x:", x)
		if 2*x+1 not in u:
			# print("appending 2x+1:", 2*x+1)
			u.append(2*x + 1)
		if 3*x+1 not in u:
			# print("appending 3x+1:", 3*x+1)
			u.append(3*x + 1)
		# print("index:", count)
		count += 1
		# print()
	# return sorted(u)
	u.sort()
	return u, u[n+1]

def main():
	tests = [10, 20, 30, 50]
	for test in tests:
		print("testing:", test)
		ret_val = dbl_linear(test)
		print("u:", ret_val[0])
		print("u[" + str(test) + "]:", ret_val[1])
		print()

if __name__ == "__main__":
	main()