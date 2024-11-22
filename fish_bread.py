
#재고추가하기

stock = { #붕어빵 종류별 재고
        "팥붕어빵": 10,
        "슈크림붕어빵" : 8,
        "초코붕어빵" : 5 }
fish_bread_num = { #붕어빵 번호 => 이름 매칭
        '1':"팥붕어빵",
        '2':"슈크림붕어빵",
        '3':"초코붕어빵" }

# 입력 받기 
while True :
    fish_bread = input("붕어빵의 종류 선택 (1:팥붕어빵, 2:슈크림붕어빵, 3:초코붕어빵) : ")

    if fish_bread in fish_bread_num : # 목록중에 있는지 확인하기 = 유효키인지 확인
            choice_bread = fish_bread_num[fish_bread] #fish_bread_num['1']= "팥붕어빵" 으로 변환 
                                             #이유 : stock 에는 "팥붕어빵"으로 되어있으니 변환해아함
            #맞으면 개수 입력하는 창 나오기
            add_count = int(input("추가 수량 : "))
            stock[choice_bread] += add_count
            print(f'{choice_bread}을 {add_count}개 채웠습니다. 현재 재고는 {stock[choice_bread]}개 입니다.')
    else :
        print('잘못된 입력입니다. 1, 2, 3 중에 선택하세요')


