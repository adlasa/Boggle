from nltk.corpus import words
import pygtrie as trie

print('Loading...')
board = []
combined = trie.CharTrie()
for w in words.words():
    combined[w] = True
answers = set()


def makeBoard():
    for r in range(5):
        board.append([])
        line = raw_input()
        for c in line.split(" "):
            board[r].append(c)
    return board


def getWords(i, j, word, tmpBoard):
    word += tmpBoard[i][j]
    if(not combined.has_subtrie(word) and not combined.has_key(word)):
        return
    if(combined.has_key(word) and len(word) >= 4):
        if(word not in answers):
            answers.add(word)
    tmpLetter = tmpBoard[i][j]
    tmpBoard[i][j] = "0"
    for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
            if(i + k <= 4 and i + k >= 0 and j + l <= 4 and j + l >= 0 and tmpBoard[i + k][j + l].isalpha()):
                getWords(i + k, j + l, word, tmpBoard)
    tmpBoard[i][j] = tmpLetter


if __name__ == "__main__":
    print("Please input board")
    makeBoard()
    print("\n")
    for i in range(5):
        for j in range(5):
            getWords(i, j, "", board)
    print('Found ' + str(len(answers)) + ' words\n')
    for word in sorted(answers):
        print(word)
