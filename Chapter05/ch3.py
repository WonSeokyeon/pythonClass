#튜플

menu= ("피자", "회덥밥", "우동")
# print(menu,type(menu))
# print(menu[0])
# print(menu[1])
# print(menu[2])
#menu[2] = '짱깨'    #추가불가
#menu[2] = '회덥밥'    #수정불가

#추가하는 방법 튜플+()

menu=menu+("돈까스",)
print(menu)

#튜플을 변수에 저장하는 방법
name, age, hobby = ("꿀꿀이","10", "코딩")
print(name, age, hobby)