import alphabet as a

def decrypt(st, key):
	if len(st) != len(key):
		return "Text and Key have to be the same length."
	alphabet = a.alpha()
	nText = []
	kText = []
	for i in range(len(st)):
		nText.append(alphabet.index(st[i].lower()))
		kText.append(alphabet.index(key[i].lower()))
	out = ""
	for i in range(len(nText)):
		op = (nText[i] - kText[i])
		if op < 0:
			x = a.length(alphabet) + op
		else:
			x = op % a.length(alphabet)
		out += alphabet[x]
	return out;
