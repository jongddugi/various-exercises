#palindrome(회문): 알파벳 순서를 뒤집어도 같은 문자열이 나오는 문자열 
# ex) 기러기 토마토 
def solution(string) :
    reverse_str = string[::-1] # list 뒤집기
    answer = string ==reverse_str
    return answer

answer1 = solution('madamimadam')
print(f'answer1 = {answer1}') # True
answer2 = solution("Madam, I'm Adam")
print(f'answer2 = {answer2}') # False


#=================================================
#ex1)
#=================================================
string = "Mandam , I'm Adam"
result = string.lower()
alphabets = "abcdefghijklmnopqrstuvwxyz"
array = []
for c in result :
    if c in alphabets :
        array.append(c)
print(array)
print()

#=================================================
#ex1-1)
#=================================================

string = "Madam, I'm Adam"
result = string.replace(' ', '')
print(result)
print()
#=================================================
#ex1-2)
#=================================================
def solution(string) :
    string= string.replace(' ', '')
    string = string.lower()
    print(f"string = {string}")
    reverse_str = string[::-1]
    answer=string == reverse_str
    return answer
answer1 = solution("Madamimadam")
print(f"answer1 = {answer1}")
answer2 = solution("Madam, I'm Adam")
print(f"answer2 = {answer2}")
print()

#=================================================
#ex1-3)
#=================================================
string = "Madam, I'm Adam"
result = string.lower()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
array = []
for c in result :
    if c in alphabets:
        array.append(c)
print(array)
result = ''.join(array)#array문자열에 공백을 넣어서 합치겠다 
result2 = '-'.join(array) # array 문자열에 -를 넣어서 합치겠다
print(result)
print(result2)

#=================================================
#ex1-4)
#=================================================
def solution(string) :
    print(f'string before: {string}')
    string= string.replace(' ', '')
    string = string.lower()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    array = [c for c in string if c in alphabets]
    string = ''.join(array)
    print(f"string after: {string}")
    reverse_str = string[::-1]
    answer = string ==reverse_str
    return answer

answer = solution("Madam, I'm Adam")
print(f"answer = {answer}")
