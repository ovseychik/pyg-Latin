"""the rules of Pyg Latin are: you take a word, move the first letter of
it to the end and add suffix 'ay'"""

def pyg_latin():

	pyg = "ay"
	original_word = raw_input("Type a word:")

	if len(original_word) > 0 and original_word.isalpha():
		word = original_word.lower()
		first_letter = word[0]
		capital_first = word[1].capitalize()
		pyg_word = capital_first + word[2:len(word)] + first_letter + pyg
		print pyg_word
	else: 
		print "Something's wrong"
	pyg_latin()
		
pyg_latin()
