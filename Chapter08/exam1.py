# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다. 보고서
# 는 항상 아래와 같은 형태로 출력되어야 합니다.----
# X 주차 주간보고 
# 부서 : 
# 이름 : 
# 업무 요약 :
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
import pickle 
for i in range(1,51):
  file_name = f"{i}주차.txt"
  with open (file_name,"w",encoding="utf-8") as data_handel:
    data_handel.write("부서 : \n")
    data_handel.write("이름 : \n")
    data_handel.write("업무 요약 : \n")

print("1~50주까지 주간보고 템플릿 완료했습니다.")


# with open ("data.text","w",encoding="utf-8") as data_handle:
#   data_handle.write("자바")
#   data_handle.write("파이썬")
#   data_handle.write("스프링")