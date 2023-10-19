import random

def createText(file):
	f=open(file,'r')
	text=f.read()
	f.close()
	return text

def getKgram(text, first, k):
	return text[first:first+k]
	
def buildMarkovModel(text, k):
	m = {}
	for n in range(len(text)-k):
		t = {text[n+k]: 1}
		if getKgram(text, n, k) in m:
			if text[n+k] in m[getKgram(text, n, k)]:
				m[getKgram(text, n, k)][text[n+k]] += 1
			else:
				m[getKgram(text, n, k)][text[n+k]] = 1
		else:
			m[getKgram(text, n, k)] = t
	return m
#builds Markov dictionary 

def buildMarkovModelRecursive(m, text, first, k):
	if first+k+1 > len(text):
		return m
	t = {text[first+k]: 1}
	if getKgram(text, first, k) in m:
		if text[first+k] in m[getKgram(text, first, k)]:
			m[getKgram(text, first, k)][text[first+k]] += 1
		else:
			m[getKgram(text, first, k)][text[first+k]] = 1
	else:
			m[getKgram(text, first, k)] = t
	return buildMarkovModelRecursive(m, text, first+1, k)
#builds Markov dictionary recursively as long as the text length doesn't exceed max recursive depth
	

def nextCharacterFrequency(m, kgram, c):
	if not(kgram in m):
		return 'no  such kgram'
	elif not(c in m[kgram]):
		return 0
	else:
		return m[kgram][c]
# c is the character, m is the Markov dictionary, kgram is the text segment

def randomCharacter(m, kgram):
	characters = []
	if not(kgram in m):
		return 'no  such kgram'
	for c in m[kgram]:
		for n in range(nextCharacterFrequency(m, kgram, c)):
			characters += [c]
	return random.choice(characters)
	
def generateRandomText(file, n, k):
	text = ''
	m = buildMarkovModel(createText(file),k)
	seed = random.choice(list(m))
	for i in range(n):
		c = randomCharacter(m, seed)
		text += c
		seed = seed[1:len(seed)] + c
	return text
# n is the character length of generated text, k is the length of the text segments (specificity)
	
	
	
