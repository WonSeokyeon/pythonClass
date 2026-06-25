#함수

#함수 선언
def open_func():
  print("함수 시작입니다,")

def add_func():
  print("덧셋음 구하는 함수 입니다.")
  return (nu)


#함수 기본값 설정
def profile(name, age=30, main="자바"):
  print("나의 이름은 :{}, 나이는 {}, 주전공은 {}".format(name,age,main))

profile("꿀꿀")

#가변인자
# def new_profile(name, age, lang1, lang2, lang3):
#   print(name, age, lang1,lang2,lang3)

def new_profile2(name, age, *lang):
  print(name, age)
  for lan in lang:
    print("{}".format(lang),end=" ")
print("*"*10)
new_profile2("wsy",30,"C")