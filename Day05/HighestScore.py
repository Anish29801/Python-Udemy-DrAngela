def HighestScore(scores):
    maxScore = scores[0]
    for i in range(len(scores)):
        if(maxScore < scores[i]):
            maxScore = scores[i]
    return maxScore


scores = [78,65,89,86,55,91,64,89]

print(HighestScore(scores))
        