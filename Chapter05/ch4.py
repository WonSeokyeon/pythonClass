#집합(SET)
#중복을 허용하지 않음
my_set = {1,2,3,4,5,5,5,5,5}  #{1, 2, 3, 4, 5}
print(my_set)

my_set2 = {2,3,4,5,6,7}
print(my_set2)   #{2, 3, 4, 5, 6, 7}

#두개의 셋을 합집합
print(my_set| my_set2)          #{1, 2, 3, 4, 5, 6, 7}
print(my_set.union(my_set2))    #{1, 2, 3, 4, 5, 6, 7}


#두개의 셋을 교집합
print(my_set & my_set2)  #{2, 3, 4, 5}
print(my_set .intersection(my_set2))  #{2, 3, 4, 5}


#두개의 셋의 차집합
print(my_set - my_set2)             #{1}
print(my_set .difference(my_set2))  #{1}

#추가기능
my_set3 = {1,2,3,4}
my_set3.add(5)   #{1, 2, 3, 4, 5}
print(my_set3)

#삭제
my_set4 = {"도라지","꿀","감"}
my_set4.remove("꿀")      #{'도라지', '감'}
print(my_set4)



