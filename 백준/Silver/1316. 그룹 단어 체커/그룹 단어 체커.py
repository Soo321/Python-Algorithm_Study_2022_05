## 백준 1316 그룹단어 체커
## 다른 분들의 풀이를 참고했습니다.

n = int(input())
group_word = n

for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            group_word -= 1
            break
print(group_word)
    

