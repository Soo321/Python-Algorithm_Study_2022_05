#문제
#양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 예를 들어, d(75) = 75+7+5 = 87이다.
#양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다. 
#예를 들어, 33으로 시작한다면 다음 수는 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51, 다음 수는 51 + 5 + 1 = 57이다. 이런식으로 다음과 같은 수열을 만들 수 있다.
#33, 39, 51, 57, 69, 84, 96, 111, 114, 120, 123, 129, 141, ...
#n을 d(n)의 생성자라고 한다. 위의 수열에서 33은 39의 생성자이고, 39는 51의 생성자, 51은 57의 생성자이다. 
#생성자가 한 개보다 많은 경우도 있다. 예를 들어, 101은 생성자가 2개(91과 100) 있다. 
#생성자가 없는 숫자를 셀프 넘버라고 한다. 
#10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

#출력
#10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

no_maker=[ ]
for i in range(10000):
    no_maker.append(i+1)
 
for i in range(1,10001):
    if i<10:
        yes_maker=i+i
        if yes_maker in no_maker:
            no_maker.remove(yes_maker)
    elif i<100:
        oo_to_list=[int(k) for k in str(i)]
        yes_maker=i+oo_to_list[0]+oo_to_list[1]
        if yes_maker in no_maker:
            no_maker.remove(yes_maker)
    elif i<1000: 
        ooo_to_list=[int(k) for k in str(i)]
        yes_maker=i+ooo_to_list[0]+ooo_to_list[1]+ooo_to_list[2]
        if yes_maker in no_maker:
            no_maker.remove(yes_maker)
    elif i<10000: 
        oooo_to_list=[int(k) for k in str(i)]
        yes_maker=i+oooo_to_list[0]+oooo_to_list[1]+oooo_to_list[2]+oooo_to_list[3]
        if yes_maker in no_maker:
            no_maker.remove(yes_maker)        

for i in range(len(no_maker)):
    print(no_maker[i])

# 생성자를 소거하는 방법이라서 더 직관적으로 코드 해석이 가능한 것 같아요. 깔끔한 코드라 좋았습니다! (최수빈)
