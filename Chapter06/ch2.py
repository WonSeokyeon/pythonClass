#for
# list = [1,3,5,7,9]
# #반복문 1
# for no in list:
#   print(format(no),end=" ")
# print("")
# #반복문2
# list = [1,3,5,7,9]
# for no in [1,3,5,7,9]:
#   print(format(no),end=" ")
# print("")
#   #반복문3
# for no in range(10,0,-2):
#   print(no,end=" ")
# print("")
# #반복문4
# order = ["중국집","자장면","탕수육"]
# for data in order:
#   print(data,end=" ")

#   #반복문 5(한줄 for 문 list comprehension)
# students = [1,2,3,4,5]
# #students = [11,12,13,14,15]
# print("")
# students = [no * 10+100 for no in students ]
# print(students)


# menu = ["닭갈비","햄버거","국밥"]
# menu1 = [len(data) for data in menu]
# print(menu1)

# like_Subject = ["java", "python", "html","javascript", "spring boot"]
# print(like_Subject)
# like_Subject1 = [ Subject.upper()  for Subject in like_Subject]
# print(like_Subject1)

#반복문 6 
# Count = 0
# exitFlag = False
# while not exitFlag:
#   Count += 1
#   print("Count = {}".format(Count))
#   if Count>=100:
#     exitFlag=True

#반복문 7 변수 in []

data_list = [1,2,3,4,5]
no= int(input("숫자를 입력하세요"))
# for i in data_list : 
#   if no == i :
#     print(" 있어요" )
#     break
#   else:
#     print("없어요")  

if no in data_list:
  print("있어요")
else:
  print("없어요")