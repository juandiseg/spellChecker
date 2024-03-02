import numpy as np

def getDatasetClassifiedByLength(path:str ="dataset.txt"):
    f = open(path, "r")
    mainDic = {}
    for word in f.read().split(","):
        word = word.strip(" ")
        wordLength = len(word)
        if wordLength > 1:
            if wordLength not in mainDic:
                mainDic[wordLength] = []
            mainDic[wordLength].append(word)
    return mainDic

def getLowestLeftUp(matrix, row, column):
    lowest = matrix[row, column-1]
    up = matrix[row-1, column]
    if up < lowest:
        lowest = up
    leftup = matrix[row-1, column-1]
    if leftup < lowest:
        lowest = leftup
    return lowest

def calculateDistanceTwoWords(str1:str, str2:str):
    matrix = np.empty([len(str1)+1, len(str2)+1], dtype=int)
    for i in range(len(str2)+1) :
        matrix[0, i] = i
    for i in range(len(str1)+1) :
        matrix[i, 0] = i
    for row in range(1, len(str1)+1):
        for column in range(1, len(str2)+1):
            min = getLowestLeftUp(matrix, row, column)
            if str2[column-1] == str1[row-1]:
                matrix[row, column] = min
            else:
                matrix[row, column] = min + 1
    return matrix[len(str1), len(str2)]

class spellChecker:
    def __init__(self):
        self.dataset = getDatasetClassifiedByLength()

    def isSpelledCorrectly(self, word:str):
        return word in self.dataset[len(word)]
    
    def getSpellingSuggestions(self, misspelledWord:str):
        suggestions = []
        lengthWordToFix = len(misspelledWord)
        for length in lengthWordToFix-1, lengthWordToFix, lengthWordToFix+1:
            for word in self.dataset[length]:
                result = calculateDistanceTwoWords(word, misspelledWord)  
                if result < 3:
                    if result == 0:
                        return [f'"{word}" is spelled correctly.', ]
                    suggestions.append(f"{word} \t(Dist. {result})")
        return suggestions

if __name__ == '__main__':
    checker = spellChecker()
    word = "wrlod"
    print(checker.isSpelledCorrectly(word))
    for suggestion in checker.getSpellingSuggestions(word):
        print(suggestion)