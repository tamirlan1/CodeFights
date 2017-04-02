def wordLadder(beginWord, endWord, wordList, ladder=[], shortest = 100000000000):
	# global ladder, shortest
	if not ladder:
		ladder.append(beginWord)

	if beginWord == endWord:
		print ladder
		return len(ladder)

	for i in wordList:
		if onediff(beginWord, i) and not i in ladder:
			# print ladder, i
			ladder.append(i)
			a = wordLadder(i, endWord, wordList, ladder, shortest)
			if a != 0 and shortest > a:
				shortest = a
			ladder.pop()
			# print beginWord, i
	if shortest != 100000000000:
		return shortest

	return 0

def onediff(w1, w2):
	if len(w1) != len(w2):
		return False

	c = 0
	for i in range(len(w1)):
		if w1[i] != w2[i]:
			c += 1

	if c == 1:
		return True

	return False

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log"]

# print wordLadder(beginWord, endWord, wordList)