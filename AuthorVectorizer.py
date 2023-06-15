#!/usr/bin/env python
import sys

#clean up the rest of this script to work with python 3


def getFileContents(fileName):
    fileContents = ""
    try:
        file = open(fileName, "r")
        fileContents = file.read()
        file.close()
    except IOError:
        print("Error: File not found")
    return fileContents


def getSentenceFromContents(fileContents):
    """ generated source for method getSentenceFromContents """
    result = []
    last = 0
    for i in range(len(fileContents)):
        if fileContents[i:i + 1] == "." or fileContents[i:i + 1] == "?" or fileContents[i: i + 1] == "!":
            result.append(fileContents[last + 1:i])
            last = i
        i += 1
    return result


def frequency(words, word):
    """ generated source for method frequency """
    counter = 0
    for test in words:
        if word == test:
            counter += 1
    return counter


def getUniqueWords(words):
    """ generated source for method getUniqueWords """
    # fill result arraylist with all unique strings in Arraylist words
    result = []
    for word in words:
        if result != word:
            result.append(word)
    return result


def getWordsFromSentence(sentence):
    """ generated source for method getWordsFromSentence """
    result = []
    splitSentence = sentence.split(" ")
    for i in range(len(splitSentence)):
        cleaned = clean(splitSentence[i])
        if len(cleaned) > 0:
            result.append(cleaned)
        i += 1
    return result


def computerAverageWordLength(words):
    """ generated source for method computerAverageWordLength """
    counter = 0
    for word in words:
        counter += len(word)
    return (1.0 * counter) / len(words)


def computeDifferentWordRatio(words):
    """ generated source for method computeDifferentWordRatio """
    # compute ratio of unique words to total words
    uniqueWords = getUniqueWords(words)
    return (1.0 * len(uniqueWords)) / len(words)


def computeHapaxLegomenaRatio(words):
    """ generated source for method computeHapaxLegomenaRatio """
    # compute ratio of words that appear only once to total words
    uniqueWords = getUniqueWords(words)
    counter = 0
    for word in uniqueWords:
        if frequency(words, word) == 1:
            counter += 1
    return (1.0 * counter) / len(words)


def getPhrasesFromSentence(sentence):
    """ generated source for method getPhrasesFromSentence """
    result = []
    last = 0
    for i in range(len(sentence)):
        if sentence[i:i + 1] == "," or sentence[i: i + 1] == ";" or sentence[i:i + 1] == ":":
            result.append(sentence[last + 1: i])
            last = i
    result.append(sentence[last])
    return result


def computeSentenceComplexity(sentences):
    """ generated source for method computeSentenceComplexity """
    # compute average number of phrases per sentence
    counter = 0
    for sentence in sentences:
        counter += len(getPhrasesFromSentence(sentence))
    return (1.0 * counter) / len(sentences)


def computeAverageWordsPerSentence(sentences):
    """ generated source for method computeAverageWordsPerSentence """
    # compute average number of words per sentence
    counter = 0
    for sentence in sentences:
        counter += len(getWordsFromSentence(sentence))
    return (1.0 * counter) / len(sentences)


def clean(word):
    """ generated source for method clean """
    word = word.lower()
    if len(word) == 0:
        return ""
    while PUNCTUATION.index(word[0:1]) != -1:
        word = word[1:]
        if len(word) == 0:
            return ""
    while PUNCTUATION.index(word[-1:]) != -1:
        word = word.substring(0, len(word) - 1)
    return word


""" generated source for class AuthorVectorizer """
PUNCTUATION = "'!\",;:.-?)([]<>*#\n\t\r "
VOWELS = "aeiouy"
authors = []


def run():
    """ generated source for method run """
    loadAuthorSignatures()
    fileName = input("Enter file name: ")
    fileContents = getFileContents(fileName)
    sentences = getSentenceFromContents(fileContents)
    words = []
    words = getAllWordsFromSentences(sentences)
    print("Sentences====" + str(len(sentences)))
    print("Words====" + str(len(words)))
    print()
    a = computerAverageWordLength(words)
    print("    Avg Word Length = " + str(a))
    b = computeDifferentWordRatio(words)
    print("    Diff word Ratio = " + str(b))
    c = computeHapaxLegomenaRatio(words)
    print("    Hapax legomanana ratio = " + str(c))
    d = computeAverageWordsPerSentence(sentences)
    print("    Avg words per sentence = " + str(d))
    e = computeSentenceComplexity(sentences)
    print("    Sentence complexity = " + str(e))
    unknownAuthor = AuthorSignature("unknown", a, b, c, d, e)
    print()
    champName = ""
    champScore = sys.maxsize
    for author in authors:
        score = author.distanceTo(unknownAuthor)
        if score < champScore:
            champScore = score
            champName = author.__name__
        print(author.__name__ + ": " + score)
    print()
    print("Predicted author = " + champName)


def loadAuthorSignatures():
    """ generated source for method loadAuthorSignatures """
    authors.append(AuthorSignature("Agatha Christie", 4.40212537354, 0.103719383127, 0.0534892315963, 10.0836888743, 1.90662947161))
    authors.append(AuthorSignature("Alexandre Dumas", 4.38235547477, 0.049677588873, 0.0212183996175, 15.0054854981, 2.63499369483))
    authors.append(AuthorSignature("Brothers Grimm", 3.96868608302, 0.0529378997714, 0.0208217283571, 22.2267197987, 3.4129614094))
    authors.append(AuthorSignature("Charles Dickens", 4.34760725241, 0.0803220950584, 0.0390662700499, 16.2613453121, 2.87721723105))
    authors.append(AuthorSignature("Douglas Adams", 4.33408042189, 0.238435104414, 0.141554321967, 13.2874354561, 1.86574870912))
    authors.append(AuthorSignature("Emily Bronte", 4.35858972311, 0.089662598104, 0.0434307152651, 16.1531664212, 2.93439550141))
    authors.append(AuthorSignature("Fyodor Dostoevsky", 4.34066732195, 0.0528571428571, 0.0233414043584, 12.8108273249, 2.16705364781))
    authors.append(AuthorSignature("James Joyce", 4.52346300961, 0.120109917189, 0.0682315429476, 10.9663296918, 1.79667373227))
    authors.append(AuthorSignature("Jane Austen", 4.41553119311, 0.0563451817574, 0.02229943808, 16.8869087498, 2.54817097682))
    authors.append(AuthorSignature("Lewis Caroll", 4.22709528497, 0.111591342227, 0.0537026953444, 16.2728740581, 2.86275565124))
    authors.append(AuthorSignature("Mark Twain", 4.33272222298, 0.117254215021, 0.0633074228159, 14.3548573631, 2.43716268311))
    authors.append(AuthorSignature("Sir Arthur Conan Doyle", 4.16808311494, 0.0822989796874, 0.0394458485444, 14.717564466, 2.2220872148))
    authors.append(AuthorSignature("William Shakespeare", 4.16216957834, 0.105602561171, 0.0575348730848, 9.34707371975, 2.24620146314))
    authors.append(AuthorSignature("J. D. Salinger", 3.9578280567537507, 0.06198963674344158, 0.027657958275684326, 10.057571623465211, 1.6180081855388813))


def getAllWordsFromSentences(sentences):
    """ generated source for method getAllWordsFromSentences """
    result = []
    for sentence in sentences:
        a = getWordsFromSentence(sentence)
        for word in a:
            result.append(word)
    return result

    # calculation Methods


class AuthorSignature(object):
    """ generated source for class AuthorSignature """
    #  declare private instance variables here
    authorName = str()
    avgWordLength = float()
    differentWordRatio = float()
    hapaxRatio = float()
    avgWordsPerSentence = float()
    avgPhrasesPerSentence = float()

    def __init__(self, authorName, avgWordLength, differentWordRatio, hapaxRatio, avgWordsPerSentence,
                 avgPhrasesPerSentence):
        """ generated source for method __init__ """
        self.authorName = authorName
        self.avgWordLength = avgWordLength
        self.differentWordRatio = differentWordRatio
        self.hapaxRatio = hapaxRatio
        self.avgWordsPerSentence = avgWordsPerSentence
        self.avgPhrasesPerSentence = avgPhrasesPerSentence
        self.WEIGHT = [11.0, 33.0, 50.0, 0.4, 4.0]

    def distanceTo(self, a):
        """ generated source for method distanceTo """
        unknownSet = a.getSignatureSet()
        thisSet = self.getSignatureSet()
        sum = 0.0
        i = 0
        while i < 5:
            sum += abs(thisSet[i] - unknownSet[i]) * self.WEIGHT[i]
            i += 1
        return sum

    def euclideanDistanceTo(self, a):
        """ generated source for method euclideanDistanceTo """
        unknownSet = a.getSignatureSet()
        thisSet = self.getSignatureSet()
        sum = 0.0
        i = 0
        while i < 5:
            sum += pow(thisSet[i] - unknownSet[i], 2) * self.WEIGHT[i]
            i += 1
        return pow(sum, 0.5)

    def getName(self):
        """ generated source for method getName """
        return self.authorName

    def getAvgWordLength(self):
        """ generated source for method getAvgWordLength """
        return self.avgWordLength

    def getDifferentWordRatio(self):
        """ generated source for method getDifferentWordRatio """
        return self.differentWordRatio

    def getHapaxRatio(self):
        """ generated source for method getHapaxRatio """
        return self.hapaxRatio

    def getAvgWordsPerSentence(self):
        """ generated source for method getAvgWordsPerSentence """
        return self.avgWordsPerSentence

    def getAvgPhrasesPerSentence(self):
        """ generated source for method getAvgPhrasesPerSentence """
        return self.avgPhrasesPerSentence

    def getSignatureSet(self):
        """ generated source for method getSignatureSet """
        result = [self.avgWordLength, self.differentWordRatio, self.hapaxRatio, self.avgWordsPerSentence,
                  self.avgPhrasesPerSentence]
        return result


if __name__ == '__main__':
    run()