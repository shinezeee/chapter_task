
#재고추가하기
fish_bread = input("붕어빵의 종류를 선택하세요 (팥붕어빵, 슈크림붕어빵, 초코붕어빵)")
add_count = int(input("붕어빵의 개수를 입력하세요 : "))
stock = {
    "팥붕어빵" : 10,
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5
}

stock[fish_bread] += add_count
print(f'{fish_bread}을 {add_count}개 채웠습니다. 현재 재고는 {stock[fish_bread]}개 입니다.')


