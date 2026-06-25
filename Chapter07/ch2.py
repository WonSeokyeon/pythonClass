#전역 변수, 지역변수

#카센터 데이터 충 갯수
#전역변수
car_total = 100

def rent(rentCount):
  #지역변수
  global car_total
  car_total = 200
  if car_total>rentCount:
    car_total = car_total-rentCount
    print("렌트할 {}대입니다 렌트 가능한 차 갯수 {}입니다.".format(rentCount,car_total))
  else:
    print("차가 없네요 다시 이용해주세요")
rent(10)
print(car_total)
