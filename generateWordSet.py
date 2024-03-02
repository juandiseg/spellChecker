def generateDataset():
    # Uncomment next 2 lines to install "words" under the "Corpora" tab
    #import nltk
    #nltk.download()
    ## When done close the downloader
    from nltk.corpus import words
    word_list = words.words()
    f = open("dataset.txt", "w")
    for word in word_list:
        if len(word) != 1:
            f.write(f"{word}, ")
    f.close()

def getDataset(path:str ="dataset.txt"):
    f = open(path, "r")
    return [word.strip(" ") for word in f.read().split(",") if len(word) > 1]

if __name__ == '__main__':
    generateDataset()