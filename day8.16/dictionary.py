# text = "The policeman whose name is JOHN is going to the doughtnut store" + \
#     "JAMES aka doughnut master greeted JOHN and spoke to JOHN"
# words = text.split(' ')
# answer = {}
# for word in words:
#     if word.upper() == word:
#         answer[word] +=1
# print(answer) # error 이유는 
# # answer = {} 빈 dictionary이기 때문입니다.
#===========================================================================================
#오류수정
#===========================================================================================
text = "The policeman whose name is JOHN is going to the doughtnut store" + \
    "JAMES aka doughnut master greeted JOHN and spoke to JOHN"
words = text.split(' ')
answer = {}
for word in words:
    if word.upper() == word:
        if word in answer:
            answer[word] +=1
        else:
            answer[word] =1
print(answer)
#===========================================================================================
#깔끔하게 변경
#===========================================================================================
from collections import defaultdict
d = defaultdict(lambda: 0)

d[3] +=1
print(d[3])
print()
#===========================================================================================
#text index에서 어디에 등장하는지 측정
#===========================================================================================
text = "The policeman whose name is JOHN is going to the doughtnut store" + \
    "JAMES aka doughnut master greeted JOHN and spoke to JOHN"
words = text.split(' ')

from collections import defaultdict
answer = defaultdict(lambda: [])

for i, word in enumerate(words):
    if word.upper() == word:
        answer[word].append(i)
print(dict(answer))