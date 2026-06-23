# 문자열에서 자주 사용하는 방법 : Slicing[], find(), count(),upper(), lower(), isupper(), islower(), replace()

#문자열
# message= " 파이썬을 공부하고 있습니다."
# print(message,type(message))


# message2 ="""파이썬을
# 공부
# 하고 있습니다."""
# print(message2,type(message2))


#슬라이싱 [](배열첨자)

# jimin = "990829-1550823"
# print("사용자 성별번호출력: ",jimin[7])
# print("사용자 연도: ",jimin[0:2])
# print("사용자 월: ",jimin[2:4])
# print("사용자 월: ",jimin[4:6])
# print("사용자 생년월일: ",jimin[0:6])
# print("사용자 생년월일: ",jimin[:6])
# print("사용자 뒷자리: ",jimin[-7:])
# print("사용자 뒷자리 검증번호 이전: ",jimin[7:-1])
# print("주민번호 사이즈:",len(jimin))

#반복문을 이용해서 한자리씩 출력하시오. 단 '-'은생략하시오
# for i in range(0,len(jimin)):
#   if jimin[i] == "-":
#     continue
#   print(jimin[i],end=" ")

#문자열 처리함수

# message = "Python is Amazing"
# print(message.lower())       #소문자 출력 (python is amazing)
# print(message.upper())       #대문자 출력 (PYTHON IS AMAZING)
# print(message.isupper())     #False
# print(message[0].isupper())  #True
# print(message[1:3].isupper())  #False
# print(message[1:3].islower())  #True
# #replace ****문자열에서 필요한 영역을 다른글로 교체가 가능
# print(message.replace("Python","Java"))  


#find , index 차이점체크
#Find 진행에서 찾는것이 없으면 -1,다음문장으로 실행한다.
#index 진행에서 찾는것이 없으면  ValueError 발생시키고, 다음문장으로 실행하지 않는다.
#index 개념보다는 fid

# message = "Python is Amazing"
# findindex  =message.find("n")
# print(findindex)   #5

# findindex2  = message.find("n",findindex+1)
# print(findindex2)  #15

# findindex3= message.find("is")
# print(findindex3)  #7

# findindex4= message.find("kim")
# print(findindex4)  #-1
# print("Hello")

# message = "Python is Amazing"
# findindex  =message.index("n")
# print(findindex)   #5

# findindex2  = message.index("n",findindex+1)
# print(findindex2)  #15

# findindex3= message.index("is")
# print(findindex3)  #7

# findindex5 = message.index("n", 6,-1)
# findindex5 = message.find("n", 6,-1)
# print(findindex5)

# findindex4= message.index("wsy") # 찾지 못하면 valueError발생되어 그위치 멈추고 다음문장 미실행
#  print(findindex4)  #ValueError
# print("Hello")

# message = "Python is Amazing"
# print(message.count("n"))      #2
# print(message.count("k"))      #0
# print(len(message))            #17


#문자열 포맷 방식

# print("Java"+"Python")  #JavaPython
# print("Java","Python")  #Java Python 
# age= 20
# print("나는 %d살 입니다." %age)
# like = "파이썬"
# print("나는 %s을 좋아합니다. "%like)
# gread = "A"
# print("Java언어의 점수는 %c 등급입니다."%gread)
# score = 95.50
# print("Java언어의 점수는 %.2f 등급입니다."%score)
# falg = True
# print("나는 Java언어를 좋아하는것은 %s 입니다."%falg)

# #두가지 이상 포맷
# fruit1= "수학"
# fruit2= "참외"
# print("나는 좋아하는 과일은 %s과 %s 입니다."%(fruit1, fruit2))

# age= 20
# print("나는 {}살 입니다." .format(age))
# like = "파이썬"
# print("나는 {}을 좋아합니다. ".format(like))
# gread = "A"
# print("Java언어의 점수는 {} 등급입니다.".format(gread))
# score = 95.50
# print("Java언어의 점수는 {} 등급입니다.".format(score))
# falg = True
# print("나는 Java언어를 좋아하는것은 {} 입니다.".format(falg))

# #두가지 이상 포맷
# fruit1= "수학"
# fruit2= "참외"
# print("나는 좋아하는 과일은 {}과 {}입니다.".format(fruit1, fruit2))
# print("나는 좋아하는 과일은 {1}과 {0}입니다.".format(fruit1, fruit2))



age= 20
print(f"나는 {age}살 입니다.")
like = "파이썬"
print(f"나는 {like}을 좋아합니다. ")
gread = "A"
print(f"Java언어의 점수는 {gread} 등급입니다.")
score = 95.50
print(f"Java언어의 점수는 {score} 등급입니다.")
falg = True
print(f"나는 Java언어를 좋아하는것은 {falg} 입니다.")

#두가지 이상 포맷
fruit1= "수학"
fruit2= "참외"
print(f"나는 좋아하는 과일은 {fruit1}과 {fruit2}입니다.")
print(f"나는 좋아하는 과일은 {fruit2}과 {fruit1}입니다.")


#탈출문자\n \t\b\r\'\"

print("파이썬 \n 자바")
print("파이썬 \t 자바")
print("파이썬 \b 자바")
print("파이썬 \r 자바")
print("파이썬보다 \"자바\"가 더 좋아요")
print("파이썬보다 \'자바\'가 더 좋아요")
print("D:\\JAVA_TEST_Git\\.metadata\\.mylyn")






