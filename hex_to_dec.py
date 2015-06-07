import os

def toDec(hexN):
	hexO = "0x" + hexN
	return int(hexO, 16)

if __name__ == '__main__':
	hex = ["9f", "11", "cc", "c0ffee"]

	for h in hex:
		print(toDec(h))

