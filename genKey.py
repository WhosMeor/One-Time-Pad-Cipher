import math, random
import alphabet as a

def genKey(n):
	alphabet = a.alpha()
	out = ""
	for i in range(n):
		out += alphabet[math.floor(random.randint(0, a.length(alphabet)-1))]
	return out
