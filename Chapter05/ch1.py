#파이썬 리스트 

subway = [10 ,20 , 30]
subway.append(40)         #추가 [10, 20, 30, 40]
subway.insert(1,100)      #삽입 [10 , 100 , 20, 30, 40]
value =subway.pop()       #제거40 [10, 100, 20, 30]
subway[0]= 200            #수정 [ 200, 100, 20, 30] 
indexValue =  subway.index(100) #검색1 [200, 100, 20 , 30]
subway.append(100)              #추가 [ 200, 100, 20, 30, 100]
countValue = subway.count(100)  #카운트2
subway.clear()                  #전체 삭제[]
print(subway)
