x = int(input("성적을 입력해주세요"))

if x > 89:
    print("A")
elif x <90 and x >= 80:
    print("B")
elif x <80 and x >= 70:
    print("C")
elif x <= 70:
    print("D")