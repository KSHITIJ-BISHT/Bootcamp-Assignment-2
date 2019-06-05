
# - Create a list of words present in file
# - Convert all words to uppercase (using map)
# - Remove the words from list which contain 'a' (using filter)
# - Generate a string by concatenating all the words in the final list (using reduce)

import functools
#print words in file
listOfWords=[]
uppercaseList=[]
with open('text.txt','r') as file:
	for line in file:
		for word in line.split():
			if word not in listOfWords:
				listOfWords.append(word)

print("WORDS IN FILE:",listOfWords)

#Convert all words to uppercase (using map)
print()
print("UPPERCASE WORDS LIST:",list(map(lambda word: word.upper() ,listOfWords)))

#removing words having 'a'
print()
print("WORDS WITHOUT 'a':",list(filter(lambda word:'a' not in word,listOfWords)))  

#creating string of words in list
print()
print("STRING OF WORDS:",functools.reduce(lambda firstWord,secondWord:firstWord+secondWord,listOfWords))  

