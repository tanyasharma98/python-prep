# import re
# matches = []
# lst = ["python is good", "python have some features", " python is more is python by use of pycharm"]
# # for i in range(len(lst)):
# #     a = re.findall(pattern="python", string=lst[i])
# #     if a in lst:
# #         pass
# # user = input("search here").lower().strip().split(" ")
# user = input("enter").split(" ")
# count = 0
# for i in lst:
#     a = i.lower().split(" ")
#     matches.append(a)
# print(matches)
# print(len(matches))
# for word in user:
#     print(word)
#     for match in matches:
#         # if word.lower() == match[len]:
#             count += 1
#         print(count)
#
#
#
#     # for j in user:
#     #     if match[i:j] == j:
#     #         count += 1
#     #         print(match[i:j])
#
#         # else:
#         #     continue
#         #
#
# # print(match)
#
#
#     # a = lst[i].lower().split(" ")
#     # print(a)
#     # count = 0
#     # if input("enter word").lower() in a:
#     #     count += 1
#     #     match.append(lst[i])
#     #     print(count)
#     # else:
#
#         # break
#
# # filter_object = filter(lambda a: 'is' in a, lst)
# #
# # # Convert the filter object to list
# # print(list(filter_object))
# ====================================================================================================================
def matchingWord(sentence1, sentence2):
    words1 = sentence1.split(" ")  # This will beak a sentence in a list of word
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':
    # print(matchingWord("python is good", "python have some features"))
    sentences = ["python is good", "python have some features", " python is more is python by use of pycharm"]

    query = input("What you want to search\n")
    scores = [matchingWord(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSenScores = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True) if sentScore[0] !=0]
    # print(sortedSenScores)
    print(f"len(sortedSenScores) result found!")
    for score, item in sortedSenScores:
        print(f"\"{item}\" : with a score of {score}")