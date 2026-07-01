while True:
  try:
    num1 =  int(input("number1 >>"))
    num2 =  int(input("number2 >>"))
    #print (f"{num1}/{num2} = {num1/num2}")
    print("{0} / {1} = {2:.2f}".format(num1, num2, num1/num2))
  except ValueError:
    print("정신차려! 숫자 잘봐랏!")
    continue
  except Exception as e:
    print(e)
    continue
  finally:
    print("flnally")
  break 
print("종료")



while True:
  try:
    num1 =  int(input("number1 >>"))
    num2 =  int(input("number2 >>"))
    #조건을 설정 두수는 0보다 크고, 10보다 작거나 같으면 실행, 다르면 예외처리 발생
    if (0<num1 <=10) and (0<num2<=10) : 
       print("{0} / {1} = {2:.2f}".format(num1, num2, num1/num2))
    else:
      raise ValueError 
  except ValueError:
    print("정신차려! 숫자 잘봐랏!")
    continue
  except Exception as e:
    print(e)
    continue
  finally:
    print("flnally")
  break 
print("종료")


class SpecicaClass():
  def __init__(self):
    print("생성자가 발생하였습니다.")
  def __str__(self):
    return "내가만들고 싶은 문자열을 만들어서 전송합니다."
 
sc = SpecicaClass()
print(sc)

