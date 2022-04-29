# =============================================Search Engine===============================================

def scoreMatch(search, sentence):
    score = 0
    search = search.strip().split()
    sentence = sentence.strip().split()
    for word1 in search:
        for word2 in sentence:
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == '__main__':
    list1 = ["This is a string ", "PYTHON got you a string", "string is a string", "never use ",
             "string is a character", "python", "Soup bowl dance", "dance", "dim dong"]
    match = input("Enter Your Search")
    findScore = [scoreMatch(match, sentence) for sentence in list1]
    # print(findScore)
    scoreSentence = [score for score in sorted(zip(findScore, list1), reverse=True) if score[0] != 0]
    print(f"{len(scoreSentence)} results found!")
    # print(scoreSentence)
    for score, item in scoreSentence:
        print(f" \"{item}\": with a score of {score}")

"""    -------------------------------------Mine--------------------
import re
list1 = ["This is a string ", "PYTHON got you a string", "string is a string", "never use ",
               "string is a character", "python", "Soup bowl dance", "dance", "dim dong"]
    match = input("Enter Your Search")
match = match.split()
count = 0
for i in list1:
    sop = i
    for j in match:
        x = j.isupper()
        y = j.islower()
        z = j.capitalize()
        # if string is in searched in upper case ,
        # we convert it into lower & capitalize form then we will check if its present of not
        if x is True:
            # upper case
            if re.findall(j, i):
                print(i)
            # lower case
            else:
                j = j.lower()
                if re.findall(j, i):
                    print(i)
                else:
                    # capitalize case
                    j = j.capitalize()
                    if re.findall(j, i):
                        print(i)
# For lower case we Perform same steps
        if y is True:
            # lower case
            if re.findall(j, i):
                print(i)
            # upper case
            else:
                j = j.upper()
                if re.findall(j, i):
                    print(i)
                else:
                    # capitalize case
                    j = j.capitalize()
                    if re.findall(j, i):
                        print(i)
# For Capitalize case we Perform same steps
        if j == z:
            # Capitalize case
            if re.findall(j, i):
                print(i)
            # lower case
            else:
                a = j.lower()
                if re.findall(a, i):
                    print(i)
                else:
                    # upper case
                    j = j.upper()
                    if re.findall(j, i):
                        print(i)
"""
