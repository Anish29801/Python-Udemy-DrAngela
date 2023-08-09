
StudentScores ={
    "Harry" : 81,
    "Ron" : 72,
    "Granger" : 99,
    "Longbottom" : 80,
    "Darco" : 77
}

def Grader(Name,Score):
    if (Score >= 91):
        print (Name +" Outstanding")
    elif(Score >= 90 or Score< 80):
        print (Name +" Can Exceed")
    elif(Score >= 80 or Score< 71):
        print (Name +" Acceptable")
    else:
        print (Name +" Failed")

for item in StudentScores:
    Grader(item,StudentScores[item])
