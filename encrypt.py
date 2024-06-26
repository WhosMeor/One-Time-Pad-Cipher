import alphabet as a

def encrypt(st, key):
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
		out += alphabet[(nText[i] + kText[i]) % a.length(alphabet)]
	return out;
