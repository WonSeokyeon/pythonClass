#피클(pickle)

import  pickle

#pickle 파일저장
#binary 파일로 저장할때는 encoding방식이 필요
# profile_handle = open ("profile.pickle", "wb")
# profile_dic={"이름":"wsy","나이":35, "취미": ["먹고","놀기","자기"]}
# #우리가 프로그램에서 사용했던, 맵구조(dictionary) 다시 사용하기 위해서 피클 파일에 저장

# pickle.dump(profile_dic,profile_handle)
# # for key, item in profile_dic.items():
# #   print(key,item)
# # print(profile_dic, type(profile_dic))
# # profile_handle.close()

# pickle  파일을 다시 가져와서 프로그램 사용하기 기능
# profile_handle = open ("profile.pickle", "rb")
# list_dic=pickle.load(profile_handle)
# profile_handle.close()
# for key,value in list_dic.items() :
#   print(key,value)

#파일 한번에 열고 자동으로 닫기 with문(자바 )
# with open ("profile.pickle", "rb") as profile_handle:
#   list_dic = pickle.load(profile_handle)
#   for k,v in list_dic.items() :
#     if k =="취미":
#       for data in v:
#         print("{}={}".format(k,data))
#     print(k,v)


#일반 파일을 with처리하는 방식()
# with open ("data.text","w",encoding="utf-8") as data_handle:
#   data_handle.write("자바")
#   data_handle.write("파이썬")
#   data_handle.write("스프링")

with open ("data.text","r",encoding="utf-8") as data_handle:
  print(data_handle.read())

