#딕션너리(KEY : value)

#key 중복 허용하지 않음,  Value값은 중복 허용
# cabinet = {3: '푸', 100 : '피그렛', 3:'수푸',4:'피그렛'}  #{3: '수푸', 100: '피그렛', 4: '피그렛'}
# print(cabinet)
# cabinet[5] = '쿠우'                                       #추가 {3: '수푸', 100: '피그렛', 4: '피그렛', 5: '쿠우'}
# del cabinet[5]                                            #삭제 {3: '수푸', 100: '피그렛', 4: '피그렛'}
# cabinet[4] = "피글32"                                     #수정 {3: '수푸', 100: '피그렛', 4: '피글32'}
# print(3 in cabinet)                                       #수정 True
# print('피글32'  in cabinet)
# print(cabinet)

# #KEY, values, items값 가져오는 방법
# cabinet = {3: '푸', 100 : '피그렛', 3:'수푸',4:'피그렛'} 
# print(cabinet.keys())           #dict_keys([3, 100, 4])
# print(cabinet.values())         #dict_values(['수푸', '피그렛', '피그렛'])
# print(cabinet.items())          #dict_items([(3, '수푸'), (100, '피그렛'), (4, '피그렛')])



#for문 출력
cabinet = { 100 : '피그렛', 3:'수푸',4:'피그렛'} 
keyList = cabinet.keys()
for  key in keyList:
  print(cabinet[key])

  cabinet.clear()
  print(cabinet)


