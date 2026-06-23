# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com 
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver 
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성 (nav) (5) 
# (1) (!)
# 예) 생성된 비밀번호 : nav51!

# 입력받을 사이트 주소
url = "http://naver.com"
print("url")


address=url.replace("http://","") # https 공백으로 변경
print(address)
find1= address.find(".") #.을 찾는다
print(find1)
address= address[:find1] #앞부터 .까지 구한다. 
print(address)
password = address[0:3] +str(len(address))+str(address.count("e")) +"!"
print(f"비번은{password}")
