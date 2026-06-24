# Quiz) 게임에서 플레이어가 얻은 점수들을 가진 scores 리스트가 있다. 가장 높은 점
# 수를 찾는 프로그램을 작성해 보세요. scores = [120, 150, 180, 200, 170] 
# 힌트) max_score 변수를 하나 생성해 준다.
# 실행결과
# 최고점수 : 200

scores = [120, 150, 180, 200, 170]
max_score= scores[0]
for score in scores:
  if max_score<score:
    max_score=score

print(f"최고점수 : {max_score}")