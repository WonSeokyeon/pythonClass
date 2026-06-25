#파이썬 리스트 

#리스트 (추가 : append, 삽입 : insert,  삭제 :  pop, 수정 :  ~~[index])
# 위치 (find(), index(), 카운트 :  count())

# subway = [10 ,20 , 30]
# subway.append(40)         #추가 [10, 20, 30, 40]
# subway.insert(1,100)      #삽입 [10 , 100 , 20, 30, 40]
# value =subway.pop()       #제거40 [10, 100, 20, 30]
# subway[0]= 200            #수정 [ 200, 100, 20, 30] 
# indexValue =  subway.index(100) #검색1 [200, 100, 20 , 30]
# subway.append(100)              #추가 [ 200, 100, 20, 30, 100]
# countValue = subway.count(100)  #카운트2
# subway.clear()                  #전체 삭제[]
# print(subway)

# subway = ['감자' ,'수박' , '참외']
# subway.append('오이')         #추가['감자', '수박', '참외', '오이']
# print(subway)
# subway.insert(1,'옥수수')      #삽입 ['감자', '옥수수', '수박', '참외', '오이']
# print(subway)
# subway.pop()      #제거 ['감자', '옥수수', '수박', '참외']
# print(subway)
# subway[0]='돼지감자'      #수정['돼지감자', '옥수수', '수박', '참외']
# print(subway)
# indexVluse =  subway.index('옥수수')   #검색 1
# print(indexVluse)
# conuntVluse =  subway.count('옥수수')   #검색 1
# print(conuntVluse)
# subway.clear()

#정렬sort()과 역정렬reverse()
#원본에다 정렬 진행


# subway = [90,10 ,20 , 30, 40, 60]
# subway.sort()
# print(subway)
# subway.reverse()
# print(subway)

#깊은복사 진행 후 정렬! 
#깊은복사 리스트 = sorted(원본리스트)
# subway = [90,10 ,20 , 30, 40, 60]
# print(subway)
# newsubway = sorted(subway)
# print(subway)
# print(newsubway)

#리스트 합집함(extend)
mixList1 = [0,True,"밥",[1,2,3,4]]
mixList2 = [30, False,'수박']
print(mixList1)
print(mixList2)
mixList1.extend(mixList2)
print(mixList1)