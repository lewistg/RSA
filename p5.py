
def getMultInv(e, modP):
	"""
	Finds the multiplicative inverse of e modP using 
	the table method.
	"""
	
	X = 0
	Y = 1
	D = 2
	K = 3

	divisorTable = [[0, 0, 0, 0] for i in range(2)]
	divisorTable[0][X] = 1
	divisorTable[0][Y] = 0
	divisorTable[0][D] = modP 
	divisorTable[0][K] = None

	divisorTable[1][X] = 0
	divisorTable[1][Y] = 1
	divisorTable[1][D] = e
	divisorTable[1][K] = modP % e

	while True:
		x = divisorTable[0][X] - divisorTable[1][K] * divisorTable[1][X]
		y = divisorTable[0][Y] - divisorTable[1][K] * divisorTable[1][Y]
		d = int(divisorTable[0][D] % divisorTable[1][D])

		if d == 0:
			print "D is " + str(divisorTable[1][D])
			if divisorTable[1][D] == 1:
				eInverse = divisorTable[1][Y]
				if eInverse < 0:
					eInverse += modP
				return (True, eInverse)
			else:
				return (False, 0)

		k = int(divisorTable[1][D] / d)

		# update our working rows
		divisorTable[0] = list(divisorTable[1])
		divisorTable[1][X] = x
		divisorTable[1][Y] = y
		divisorTable[1][D] = d
		divisorTable[1][K] = k

def main():
	print getMultInv(23, 120)

if __name__ == "__main__":
	main()
