# 표준 입출력 기능

#input 입력받은 값은 무조건 문자열이다.

# num = input("당신이 좋아하는 숫자입력>>")
# print(num,type(num))  #17 <class 'str'>

# falg= input("당신은 여행을 좋아하시나요(True/False)>>")
# print(falg, type(falg))  #네 <class 'str'>

# gender= input("당신을 성별을 입력해주세요(F/M)>>")
# print(gender, type(gender))  #f <class 'str'>

#문자열 => 숫자형(int,float) 숫자형, 부울형  => 문자열(str)

#당신의 나이를 받아서 출력하는 프로그램

# age = int(input("당신의 나이는??"))
# print(age,type(age))  #50 <class 'int'>
# # print("당신의 나이는"+str(age)+"입니다")
# print("당신의 나이는 {} 입니다".format(age))
# print(f"당신의 나이는 {age} 입니다")


#출력관련된 기능

# print("파이썬"+"자바" ,end="")

# print("파이썬"+"자바" ,end="?")
# print("파이썬","자바")
# print("파이썬","자바","자바스크립트",sep=" , ") #파이썬 , 자바 , 자바스크립트


#표준화면출력(기본print), 표준에러 출력
#import sys
# print("파이썬","자바",sep=",",file=sys.stdout)
# print("파이썬","자바",sep=",",file=sys.stderr)

# scores = {"수학": 100, "영어" : 80," 국어" : 70}
# print(scores, type(scores))

# for key in scores.keys():
#   print("key ={}".format(key))

# for value in scores.values():
#   print("value ={}".format(value))


# for key,value in scores.items():
#   print("key = {},valu={}".format(key,value))


#출력화면 서식적용2 (3자리로 맞춰주고 빈공간은 0으로 생성)
# for i in range(1,21): #(1~20)
#   print(f"num : " +str(i).zfill(3)) 


#출력화면 서식적용2 format형식

# print("{}".format(100))
# print("{0}".format(100))
# print("{0} {1}".format(100,200))
# print("{1} {0}".format(100,200))

# print("{0: >10}".format(100))   #       100
# print("{0:_>10}".format(100))   #_______100
# print("{0:_>+10}".format(100))  #______+100
# print("{0:_>+10}".format(-100)) #______-100


# print("{0:,}".format(10000000000)) #10,000,000,000(3자리마다 , 찍어줌)
# print("{0:+,}".format(10000000000)) #+10,000,000,000(3자리마다 , 찍어줌)
# print("{0:+,}".format(-10000000000)) #-10,000,000,000(3자리마다 , 찍어줌)

# print("{0:>+30,}".format(10000000000)) #               +10,000,000,000
# print("{0:_>+30,}".format(10000000000)) #_______________+10,000,000,000


print("{0:f}".format(95.7857)) #95.780000
print("{0:.2f}".format(95.7847)) #95.79
print("{0:10.2f}".format(95.7847)) #95.79