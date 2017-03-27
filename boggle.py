from nltk.corpus import words
import copy

board = []
dictionary = words.words()
combined = "\t".join(words.words())
answers = set()

def makeBoard():
	for r in range(5):
		board.append([])
		line = input()
		for c in line.split(" "):
			board[r].append(c)
	return board

def isValidWord(word):
	return word in dictionary

def dictContains(word):
	return word in combined

def getWords(i, j, word, tmpBoard):
	word += tmpBoard[i][j]
	if(not dictContains(word)):
		return
	if(isValidWord(word) and len(word) >= 4):
		if(word not in answers):
			answers.add(word)
			print(str(len(answers)) + ". " + word)
	tmpBoard[i][j] = "0"
	for k in [-1, 0, 1]:
		for l in [-1, 0, 1]:
			if(i+k <= 4 and i+k >= 0 and j+l <= 4 and j+l >= 0 and tmpBoard[i+k][j+l].isalpha()):
				getWords(i+k, j+l, word, copy.deepcopy(tmpBoard))

if __name__ == "__main__":
	makeBoard()
	print("\n")
	complete = 0
	for i in range(5):
		for j in range(5):
			getWords(i, j, "", copy.deepcopy(board))
			complete += 1
			print("~"+ str(int(complete/25 * 100)) + "% Complete")
	print("\nOrdered:")
	i = 0
	for word in sorted(answers):
		i += 1
		print(str(i) + ". " + word)
