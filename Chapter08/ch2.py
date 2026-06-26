# 파일입출력 데이터베이스 => 파일에 저장가져오고, 저장하고, 삭제하고, 수정하고
#파일에서 "w" : 저장, 일기 "r", 추가 "a", 
#score.txt파일을 utf8
# file_handle = open("score.txt", "w", encoding="utf8")
# print("국어 : 100",file=file_handle)
# print("영어 : 90",file=file_handle)
# print("수학 : 70",file=file_handle)
# file_handle.close()


# #sore.txt 추가 기능을 설정해서 객체를 생성해야된다.
# file_handle =open("score.txt", "a", encoding="utf8")
# print("자바 : 100",file=file_handle)
# print("파이썬 : 90",file=file_handle)
# file_handle.close()

#sore.txt 추가 기능을 설정해서 객체를 생성해야된다.
# file_handle =open("score.txt", "a", encoding="utf8")
# #write() 기능은 /n라인 기능은 없다
# file_handle.write("HTML : 100 \n")
# file_handle.write("CSS : 100 \n")
# file_handle.close()

#파일에서 "r": 읽어옴
# file_handle =open("score.txt", "r", encoding="utf8")
# print(file_handle.read())
# file_handle.close()


# file_handle =open("score.txt", "r", encoding="utf8")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# file_handle.close()

# file_handle =open("score.txt", "r", encoding="utf8")
# exitFlag = False
# while  not exitFlag:
#   line = file_handle.readline()
#   #EOF 이면 line은 false
#   if line:
#    print(line, end="")
#   else:
#     exitFlag = True

# file_handle.close()

file_handle =open("score.txt", "r", encoding="utf8")
# list=  file_handle.readlines()
# file_handle.close()

#print(list, type(list))

for data in list:
  print(data, end="")