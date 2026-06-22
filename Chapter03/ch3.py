#연산자(+,-,/,%,**,//)
# print(3 + 2)
# print(3 - 2)
# print(3 * 2)
# print(3 / 2)
# print(3 % 2)
# print('*'*20)
# print(3 // 2)  #1
# print(3 ** 2)  #9

#관계 연산자(< > <= >= == != & |  6<= a<= 10)
# num = 5
# print(2 < num < 10)           #True
# print(not(2 < num < 10))      #False

# print(num>2 and num< 10)      #True
# print(not(num>2 and num< 10)) #False
# print(not(num>2 & num< 10))   #False


# print(num < 2 | num > 10)     #False
# print(num < 2 or num > 10)    #False

# print("*"*10) 
# print(3 > 2)                  #True
# print(3 >= 2)                 #True
# print(3 < 2)                  #False
# print(3 <= 2)                 #False
# print(3 == 2)                 #False
# print(3 != 2)                 #True

#수식 연산자
print((5 + 4) * 2)

#복합 대입 연산자
# num = 10
# num = num+10
# num += 10

# num = num+10
# num += 10

# num = num/10
# num /=10

# num = num**2
# num **= 2

# num = num//2
# num //= 2

# num = num%2
# num %= 2

#print("num = "+str(num)+"")

#숫자 처리함수 abs, pow, max, min, round

# print(abs(-5))
# print(pow(2,3))
# print(2**3)
# print(max(4,3,5,3,6,3,7,3))
# print(min(4,3,5,3,6,3,7,3))
# print(round(3.141592))        #반올림을 첫째자리에서 3
# print(round(3.541592))        #반올림을 첫째자리에서 4
# print(round(3.541592,2))      #반올림을 소수점 2자리까지 표현!



# 모듈을 가져와서 작업
# from math import *

# result  = floor(4.999)
# print(result)

# result= ceil(4.99)
# print(result)

# result = sqrt(16)
# print(result)

#랜덤함수모듈
from random import* #랜덤 모듈에서 사용되어지는 모든 함수 가져오겠다.
# #120~179 (random()*큰값-작은값+1)+작은값)
# for i in range(1,11):
#   print(int(random()*(179-120+1)+120)) # 0.0 < random< 1.0

  #range(1,41) 1부터~40까지 randrange(1,41) : 1~40까지 랜덤으로 출력

for i in range(1,5):
    print(randrange(120,180))









