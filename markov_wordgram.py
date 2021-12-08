import random
#the main algorithm that will run the game
def Markov(sample, length):
    for i in enumerate(sample):
        try:
            ngrams[i[1]].append(sample[i[0]+1])
        except KeyError:
            ngrams[i[1]] = []
            try:
                ngrams[i[1]].append(sample[i[0]+1])
            except IndexError:
                continue
    currentgram = random.choice(sample)
    result = currentgram
    for i in range(length):
        poss = ngrams[currentgram]
        nexT = random.choice(poss)
        result += ' '+nexT
        currentgram = random.choice(ngrams[result.split()[-1]])
    return result

if __name__ == '__main__':
    path=input("Path: ").replace('"','')
    with open(path) as f:
        wordList = f.read().lower().split()
        f.close()
    print(Markov(wordList,random.choice(range(10,50))))
