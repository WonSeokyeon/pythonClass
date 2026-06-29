# 일반 유닛 (부모 클래스)
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

# 공격 유닛 (자식 클래스) - Unit을 상속받음
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        # 부모 생성자 호출
        Unit.__init__(self, name, hp, speed)
        self.damage = damage  # 유닛 고유의 '공격력' 수치 저장
        print(f"유닛 이름 : {self.name} 체력 {self.hp}, 공격력 : {self.damage}, 속도 : {self.speed} 생성완료")

    # 공격하는 행동
    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]")

    # 💡 피격당하는 행동 (메서드 이름을 take_damage로 명확하게 변경!)
    def take_damage(self, damage_amount):
        print(f"{self.name} : 상대방으로부터 공격력 {damage_amount}으로 공격을 받고 있습니다.")
        
        # 체력 감소 계산
        self.hp -= damage_amount
        print(f"{self.name} : 공격을 받아서 남아있는 체력은 {self.hp}입니다.")
        
        # 파괴 여부 확인
        if self.hp <= 0:
            print(f" {self.name} 유닛은 파괴되었습니다.")        

# 유닛 생성
soldier1 = AttackUnit("보병1", 40, 5, 10)
soldier2 = AttackUnit("보병2", 40, 5, 10)
soldier3 = AttackUnit("보병3", 40, 5, 10)
soldier4 = AttackUnit("보병4", 40, 5, 10)
tank1 = AttackUnit("탱크1", 150, 35, 20)
tank2 = AttackUnit("탱크2", 130, 35, 20) # tank2도 리스트에 넣으려 하셨던 것 같아 아래에서 수정했습니다.

# 리스트에 유닛 추가
attack_unit = [] # nuit 오타 수정
attack_unit.append(soldier1)
attack_unit.append(soldier2)
attack_unit.append(soldier3)
attack_unit.append(soldier4)
attack_unit.append(tank1)
attack_unit.append(tank2) 

print("\n--- 전체 유닛 공격 명령 ---")
# 💡 반복문에서 클래스 이름이 아닌 '메서드'를 호출합니다.
for unit in attack_unit:
    unit.attack("1시")


#5개의 유닛을 반복문을 이용해서 공격 받기 처리
for unit in attack_unit:
    unit.take_damage(10)

#상속(어버라이딩과 다형성 구현 이 가장 중요한 개념)