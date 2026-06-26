# Quiz) "리그 오브 레전드" 게임에서 세명의 팀원이 얻은 골드량을 매개변수로 
# 받아, 팀의 평균 골드 획득량을 계산하는 함수 cal_average_gold를 정의하고 사용해 보세요.
# cal_average_gold(12000, 15000, 18000)

def cal_average_gold(*no):
  avg = sum(no)/len(no)
  print(int(avg))
cal_average_gold(12000,15000,18000)


# Quiz) "리그 오브 레전드" 게임에서 특정 챔피언의 킬(kill), 데스(death), 어시스
# 트(assist) 수치를 매개변수로 받아, KDA(Kill-Death-Assist) 비율을 계산하는 함수 
# cal_kda를 정의하고 사용해 보세요.
# 힌트) (Kill + Assist)/(Death) 
# cal_kda(10, 2, 7)
# 실행결과
# 8.5

# def cal_kda(kill, death, assist):
#   return (kill +assist) / (death)

# kda = cal_kda(10, 2, 7)
# print("비율 계산 :",  format(kda))

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중 : 각 개인의 키에 적당한 체중
# (성별에 따른 공식) 
# 남자 : 키(m) x 키(m) x 22 
# 여자 : 키(m) x 키(m) x 21
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
# 함수명 : std_weight
# 전달값 : 키(height), 성별(gender) 
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
# (출력 예제) 
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.



def std_weight(height , gender):
  height1 = height/100  #m로 변경해야됨
  if gender  == "남자" or gender  == "남" :
    return height1 *height1 *22
  elif gender  =="여자" or gender == "여":
    return height1 *height1 *21
  else:
    return 0

height =  int (input("키를 입력해주세요(cm)"))
gender = input("성별을 입력해주세요")

weight =  std_weight(height , gender)  
print(f"키{height}cm {gender}의 표준체중은 {weight:.2f}kg")