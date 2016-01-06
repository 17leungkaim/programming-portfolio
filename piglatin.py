# pig latin translator
# Scope of a variable: When and where a variable exists

vowels = "aeiouyAEIOUY"



def vegas():
	gamble = True
	party = True
	immorality = True

def pigify(word):
	vowels = "aeiouyAEIOUY"
	vpos = 0
	for i in range(len(word)):
		if word[i] in vowels:
				vpos = i
				break

	return word[vpos:] + word[:vpos] + "ay"

def test(a, b):
	print "a is ", a, "b is", b
	
def main():
	while True:
		word = raw_input("Enter a word to translate: ")
		print pigify(word)
		print vowels
		test(12, 17, 13)
		test(12, 17)
		test(12)

	gamble = False
	vegas()
	print "Did you gamble?", gamble

main()
