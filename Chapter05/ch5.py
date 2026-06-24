#자료구조의 변경

# set-> list 변경

meun = {"햄버거"," 콜라","감자튀김"}
print(meun, type(meun)) #{' 콜라', '감자튀김', '햄버거'} <class 'set'>

meun =list(meun)
print(meun, type(meun))  #[' 콜라', '감자튀김', '햄버거'] <class 'list'>
#list = > tuple

meun =tuple(meun)
print(meun, type(meun))  #(' 콜라', '감자튀김', '햄버거') <class 'tuple'>


meun= set(meun)
meun2= ("햄버거"," 콜라","감자튀김","햄버거")
print(meun2)
meun2 =set(meun2)
print(meun2, type(meun2))  #{'감자튀김', '햄버거', ' 콜라'} <class 'set'>




