#숫자 자료형
# print(5)
# print(-5)
# print(3.141592)
# print(-3.141592)

#숫자 자료형 연산(+,-,*,/,%,//)
#연산식 순서 (최고, 단항, 이항(산술,쉬프트, 비교, 논리(비트, 일반)),삼항, 치환, 컴마)
# print(5+5)
# print(6/4) #1.5
# print(2*8)
# print(6%4) #2
# print(6//4) #몫(1)
# print(4*(6/3)) #연산 우선순위 ()


#문자열 자료형

# print("여름과일"+"수박")         #문자열 + 문자열 => 문자열
# print("당신의 나이는" + str(23)) #문자열 + str(숫자형) => 문자열
# print(int("54")+24)              #int(문자열) +숫자형=> 계산가능 
# print("&"*10)                    #&&&&&&&&&&
# print ('오렌지','토마토')        #오렌지 토마토
# print ('파이썬 ')                #파이썬
# print ("오늘은 정말로 공부를 열심히 했습니다.")  


#boolean 형
# print(10>5)
# print(10<5)
# print(True)
# print(False)
# print(not(10>5))

#변수(변하는 값을 메모리 저장해서 다음에 사용할 수 있도록 활용)
#전역변수,지역변수


# print("홍길동씨 당신이 좋아흐는 동물은 무었입니까?")
# print("내가 좋아하는 동물은 강아지입니다. 그리고 이름은 해피입니다.")
# print("해피의 나이는 4살입니다. 산책을 좋아합니다.")

# name = "쿠마"
# animal= "멧돼지"
# animalName = "해피"
# animalAge = 4
# animlaHobby = "산책"

# print(name+"씨 당신이 좋아하는 동물은 무엇입니까?")
# print("내가 좋아하는 동물은 "+animal+"입니다. 그리고 이름은 "+animalName+"입니다.")
# print(""+animalName+"의 나이는 "+str(animalAge)+"살입니다. "+animlaHobby+"을 좋아합니다.")

#문자열 => 숫자형으로 변환
# print(int("3")+int("4"))
# print(float("3.5")+4.2) #int("3.5")로 변경시 에러 발생
# #print(int("3.5"))
# print(int(3.5))
#print(int("삼")) ValueError

#type 확인
# print(type(3))       #<class 'int'>
# print(type("3"))     #<class 'str'>
# print(type('a'))     #<class 'str'>
# print(type(3.5))     #<class 'float'>
# print(type(True))    #<class 'bool'>
# print(type(str(3)))  #<class 'str'>

# #변수(조심해야할 부분) = 상수에 의해서 결정된다.
# age = 10
# print(type(age))  #<class 'int'>
# age =  age>20
# print(type(age))  #<class 'bool'>

#주석
#한줄 주석 #을 활용

#여러줄 주석
"""
print ("여기있는 모든 내용은 주석 처리된다.")

"""

'''
print ("여기있는 모든 내용은 주석 처리된다.")

'''


