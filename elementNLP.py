from elementVariable import elementInfo
def autoCorrect(word,words):
        outputs = []
        correctness = []
        iterations = len(words)
        for x in range(iterations):
            if word.lower() == words[x].lower():
                return(word)
        
        for i in range(iterations):
            y = 0
            wordList = list(word.lower())
            firstLetterOfWord = wordList[0]
            word1 = []
            word1 = list(words[i].lower())
            for j in range(len(wordList)):
                if wordList[j] not in word1:
                    wordList[j] = "-"

            for cancelLoop in range(len(wordList)):
                if wordList[cancelLoop] in word1:
                    character = wordList[cancelLoop]
                    elementCount =  word1.count(character)
                    wordListCount = wordList.count(character)
                    if abs(wordListCount - elementCount) != 0:
                        wordList[cancelLoop] = "-"
            extraDash = 0
            try:
                 while len(wordList) != len(word1):
                         if len(wordList)- len(word1) > 0:
                         
                                wordList.remove("-")
                         elif len(wordList)- len(word1) < 0:
                                 wordList.append("-")
            except ValueError:
                    pass
        
            outputs.append(wordList)
                        
        for q in range(iterations):
            correct = outputs[q].count("-")

            correctness.append(correct)

        lowestNumber = 10000
        testedNumber = 0
        numberOfEqual = 0
        for completeDisaster in range(iterations):
            if correctness[1] == correctness[completeDisaster]:
                numberOfEqual += 1
            if numberOfEqual == 117:
                return("ERROR")

            
        betterCorrectness = correctness
        
        spellingAttempts = []
        sortedCorrect = []
        sortedCorrect = sorted(correctness)
        indexAdd = 0
        acurracies = []
        orderedAcurracies = []
        for zeros in range(iterations):
                orderedAcurracies.append(0)
        for threshHold in range(iterations):
                acurracies.append((1-(outputs[threshHold].count("-")/len(outputs[threshHold])))*100)
        for indexValues in range(iterations):
            for spellingWords in range(iterations):
                if sortedCorrect[indexValues] == correctness[spellingWords]:
                    spellingAttempts.append(words[spellingWords])
                    correctness[spellingWords] = ""
                    break
        for index in range(iterations):
                for secondIndex in range(iterations):
                        if words[index] == spellingAttempts[secondIndex]:
                                orderedAcurracies[secondIndex] = acurracies[index]
                                break
        firstTenLetters = [w[0] for w in spellingAttempts]
        firstTenLetters = firstTenLetters[0:9]
        firstLetterOfWord= firstLetterOfWord.upper()
        if firstLetterOfWord in firstTenLetters:
                
            for whichLetter in range(10):
                if firstLetterOfWord == firstTenLetters[whichLetter]:
                    if orderedAcurracies[whichLetter] >= 60:
                        return(spellingAttempts[whichLetter])
                    
                    else:
                                if orderedAcurracies[0] >= 70:
                                        return(spellingAttempts[0])
                                else:
                                        return("No Word Found")
        if orderedAcurracies[0] >= 70:
                return(spellingAttempts[0])
        else:
                return("No Word Found")
        return("Fail")
