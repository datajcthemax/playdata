# 메뉴보여주기
# 메뉴 보내주세요 이름:가격
# 개수선택
# 계산 전 메뉴 확인
"""
1. 메뉴 수집
2. 메뉴를 관리하는 파일(이름, 가격, 개수)
3. 주문 ( 각 메뉴 주문 받기, 몇잔 정하기)
4. 확인
"""
menu = {
    "바닐라 라떼":4000,
    "자몽허니블랙티":6400,
    # "망고바나나":5000,
    # "카라멜 마끼아또":5500,
    # "에스프레소":5000,
    # "제주유기녹차":7000,
    # "딸기 라떼":6000,
    # "딸기케잌":10000,
    # "밀크티" :7000
}
order = {} # 메뉴이름, 수량
           # {"밀크티":3}
# 주문 받기
# print(menu.keys())
# print(list(menu.keys())[0])
# 주문받기
menu_list = list(menu.keys())
print("스타벅스 키오스크에 오신것을 환영합니다")
num = input("%s는 몇잔 주문하시겠어요?"%menu_list[0])
order[menu_list[0]]=int(num)
num = input("%s는 몇잔 주문하시겠어요?"%menu_list[1])
order[menu_list[1]]=int(num)
# 계산
# menu key를 가져옴
# 그 값(개별 가격)을 받아옴
# order에서도 값(수량)을 가져옴
# 계산 -> 마무리
price_0 = menu[menu_list[0]] # 4000
amount_0 = order[menu_list[0]]
total_0 = price_0*amount_0
# 계산 전 메뉴확인
print("주문하신 내용은 아래와 같습니다")
print(f"{menu_list[0]} 가격 : {price_0} :  수량 {amount_0} : 총합 {total_0}")
price_1 = menu[menu_list[1]] # 4000
amount_1 = order[menu_list[1]]
total_1 = price_1*amount_1
# 계산 전 메뉴확인
print(f"{menu_list[1]} 가격 : {price_1} :  수량 {amount_1} : 총합 {total_1}")
# 전체 금액
print("전체 금액 : ", total_0+total_1)
pass