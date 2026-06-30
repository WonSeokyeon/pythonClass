# 다중 상속

#일반 유닛(지상 공격력 0)
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print(f"{self.name}은 체력 :{self.hp} 이동속도: {self.speed} 유닛으로 생성되었습니다")
nurse1 =  Unit("간호사1", 40, 5)
nurse2 =  Unit("간호사2", 40, 5)

#공격력있는 유닛 (상속)
class AttackUnit(Unit):
    #생성자
    def __init__(self, name, hp, speed, damage):
       #super().__init__(name, hp, speed)  다중 상속이슈발생됨으로 사용하지마랏!
        Unit.__init__(self,name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print(f"{self.name}이 현재체력: {self.hp}  {location}방향으로 {self.speed}로 공격력{self.damage} 공격중임.")

  # 상대방의 공격력을 받게 되었을때 처리하는 함수: damage
    def damaged(self, damage):
        print(f"{self.name}이 상대방의 공격{damage}을 받았습니다.")
        self.hp = self.hp - damage
        if self.hp <= 0: 
            print(f"{self.name}은 파괴 되었습니다.")
        else:
            print(f"{self.name}은 체력이 {self.hp}가 남아 있습니다.")

#공중 유무 유닛(공중을 진행 할 수 있는 체크)C
class Flayable:
    def __init__(self, flyint_speed):
        self.flyint_speed =  flyint_speed
    #멤버함수
    def fly(self, location):
        print (f"{self.flyint_speed}이 {location}방향으로 날아가고있습니다.")
#다중상속 (지상공격 유닛, 공중 유뮤)
class FlayableAttackUnit(AttackUnit, Flayable):
    def __init__(self, name, hp, speed, damage, flyint_speed ):
        AttackUnit.__init__(self.name, hp, speed,damage)
        Flayable.__init__(self, flyint_speed)
        