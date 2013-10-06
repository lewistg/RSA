from Crypto.Util import number

def getMultInv(e, modP):
	"""
	Returns tuple of (true, n) where true indicates that the numbers are
	relatively prime and n which is the multiplicative inverse of e mod p.
	Otherwise (false, 0) is returned.
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
	divisorTable[1][K] = modP / e

	while True:
		x = divisorTable[0][X] - divisorTable[1][K] * divisorTable[1][X]
		y = divisorTable[0][Y] - divisorTable[1][K] * divisorTable[1][Y]
		d = divisorTable[0][D] % divisorTable[1][D]
		n = divisorTable[0][D] / divisorTable[1][D]
		assert((x * modP + y * e) == d)

		if d == 0:
			if divisorTable[1][D] == 1:
				eInverse = divisorTable[1][Y]
				if eInverse < 0:
					eInverse += modP
				return (True, eInverse)
			else:
				return (False, 0)

		k = long(divisorTable[1][D] / d)

		# update our working rows
		divisorTable[0] = list(divisorTable[1])
		divisorTable[1][X] = x
		divisorTable[1][Y] = y
		divisorTable[1][D] = d
		divisorTable[1][K] = k
		
def modExp(g, s, p):
	"""
	Calculates s^g mod p
	"""
	lowBit = 0x1 
	result = 1
	base = g 
	while s > 0:
		if (s & lowBit) == 1:
			result = (result * base) % p
		s = s >> 1
		base = (base * base) % p
		
	return result

def main():
	#print getMultInv(23, 120)
	#print getMultInv(15, 26)
	e = 65537
	p = 0
	q = 0 
	phiOfN = 0
	while True:
		p = number.getStrongPrime(512)
		q = number.getStrongPrime(512)
		phiOfN = (p - 1)*(q - 1)
		if getMultInv(e, phiOfN)[0]:
			break
	n = p * q

	multInv = getMultInv(e, phiOfN)
	assert(multInv[0])
	d = multInv[1]

	m = 245678
	print m
	print modExp(modExp(m, e, n), d, n)

if __name__ == "__main__":
	main()
