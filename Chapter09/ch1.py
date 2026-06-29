#클래스 설계(스타크래프트)
#클래스명 Unit, 멤버 변수 :  이름 name , 체력 hp, 공격력 demage, 스피드 speed

class Unit:
  #생성자
   def __init__(self,name, hp, speed):
      self.name = name
      self.hp =  hp
      self.speed = speed
      print(f"유닛 이름 : {self.name} 체력 {self.hp}, 속도 : {self.speed} 생성완료")

#클래스명은 AttackUnit, 멤버 변수 :  name, hp, damage, speed
class AttackUnit :
   def __init__(self, name, hp, damege, speed):
      self.name = name
      self.hp = hp
      self.damege = damege
      self.speed = speed
      print(f"유닛 이름 : {self.name} 체력 {self.hp}, 공격력 : {self.damege} ,속도 : {self.speed} 생성완료")

#멤버 함수(공격)
   def attack(self, location):
      print(f"{self.name}이 {location}시 방향으로 공격력:{self.damege}으로 실행하고있습니다.")

  #멤버 함수(공격 당하기)
   def damege(self, damega):
    print(f"{self.name}상대방으로부터 공격력{damega}으로 공격을 받고있습니다.")
    self.hp= self.hp-damega
    print(f"{self.name}공격을 받아서 남아있는 체력{self.hp}입니다.")
    if self.hp <=0:
        print(f"{self.name}유닛은 파괴되었습니다.")

#보병1 
soldier1 = AttackUnit("보병",40,5,10)
soldier2 = AttackUnit("보병",40,5,10)
soldier3 = AttackUnit("보병",40,5,10)
soldier4 = AttackUnit("보병4",40,5,10)
tank1 = AttackUnit("탱크",150,35,20)
tank2 = AttackUnit("탱크",130,35,20)
tank3 = AttackUnit("탱크",140,35,20)

#보병1 공격(10시방향으로 )
# soldier1.attack(10)
# soldier2.attack(10)
# soldier3.attack(10)
# tank1.attack(10)
# tank2.attack(10)

#배열관리
attacklist = []
attacklist.append(soldier1)
attacklist.append(soldier2)
attacklist.append(soldier3)
attacklist.append(tank1)
attacklist.append(tank2)

#for unit in attacklist :
#   unit.attack(10)

# for unit in attacklist:
#   unit.damege(20)

#날아 다니면서 공격하기 유닛
# 사용되는 객체가 자신만의 멤버 변수를 추가하면 자기 자신에만 해당됨
#같은 클래스 다른 유닛에는 적용되지 않음
airunit1 =  AttackUnit("전투기",200,30,40)
soldier4 = AttackUnit("보병4",40,5,10)
airunit1.fly = True
if airunit1.fly == True:
   print(f"{airunit1.name} {airunit1.hp} {airunit1.damege}{airunit1.speed} 공중 유닛 :  {airunit1.fly}")

# if soldier4.fly == True:
#    print(f"{soldier4.name} {soldier4.hp} {soldier4.damege} {soldier4.speed}")
# else:
#    print(f"{soldier4.name} {soldier4.hp} {soldier4.damege} {soldier4.speed}")
   


