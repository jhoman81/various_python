"""choose a number, reverse its digits and add it to the original. If the sum is not a palindrome (which means, 
	it is not the same number from left to right and right to left), repeat this procedure."""

import sys

def reverseNum(number):
	reversedN = str(number)[::-1]
	newRev = int(reversedN)
	tester = number + newRev
	print(str(number) + " + " + str(newRev) + " = " + str(tester))
	if str(tester) == str(tester)[::-1]:
		print(tester)
	else:
		reverseNum(tester)


if __name__ == '__main__':
	test_cases = open(sys.argv[1], 'r')

	for test in test_cases:
		reverseNum(test)

	test_cases.close()
