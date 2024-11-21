# if 알고리즘 문제

#문제 : 단어 a의 가운데 글자를 반환하는 함수 코드

#입력 : 문자열을 입력합니다.

#조건 : 단어의 길이가 짝수라면 가운데 두글자를 출력하면 됩니다.

#입력값 1 : "abcde" => c
#입력값 2 : "qwer" => we

#코드를 작성해보세요!
'''
a = input("입력해주세요")

middle = int(len(a)/2) #가운데 값

if len(a)%2 !=0:
   print(a[middle])
else :
   print(a[middle-1:middle+1])
'''



#문제 : 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하세요.

#입력 : 첫째 줄에 A, 둘째 줄에 B를 입력합니다.

#조건 : 다음 세 가지 중 하나를 출력하세요.
#1. A가 B보다 큰 경우에는 '>'를 출력합니다.
#2. A가 B보다 작은 경우에는 '<'를 출력합니다.
#3. A와 B가 같은 경우에는 '=='를 출력합니다.

#제한
#-10,000 <= A, B <= 10,000
'''
A = int(input("A를 입력해주세요 => "))
B = int(input("B를 입력해주세요 => "))

if A>B :
    print(">")
elif A<B :
    print("<")
else :
    print("==")
'''

#문제 : 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D,
#나머지 점수는 F를 출력하는 프로그램을 작성하세요.

#입력 : 첫째 줄에 시험 점수를 입력한다. 0 <= 시험점수 <= 100 (정수)

#출력 : 성적에 따른 등급 A ~ F

score=int(input("시험 점수를 입력하세요 => "))
while True:
    if int(0<= score <=100):
        if score>=90:
            print("A")
        elif score>80:
            print("B")
        elif score>=70:
            print("C")
        elif score>=60:
            print("D")
        else :
            print("F")
    else :
        print("0부터 100까지의 점수를 입력하세요.")
    break
        