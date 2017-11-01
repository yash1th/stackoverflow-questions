class Enemy:
 health_points = 5
 _foo__is_dead = False

 def set_hp(self,points_to_set):
    if self._foo__is_dead == False:
        self.health_points = points_to_set
    else:
        print("Enemy is already dead")

 def attack(self):
    print("Hit confirmed")
    self.health_points -= 1

    if self.health_points <= -1:
        self._foo__is_dead = true

    print(self._foo__is_dead)
    print(self.health_points)

    if (self.health_points <= -1 and self._foo__is_dead  == False):
        print("Enemy Terminated")
    else:
        print("Enemy is  dead")

 #Connected to pydev debugger (build 172.3968.37)
 #Enter hit points for first enemy14
 #Hit confirmed
 #False
 #13


 def reveal_hp(self):
    if self._foo__is_dead == False:
        print(self.health_points, " health points remaining")
    else:
        print("Enemy is already dead")


first_enemy = Enemy()

try:
 one_hp = int(input("Enter hit points for first enemy"))
except ValueError or one_hp > 100:
 print("Enter only numerical values and less than 100")
 exit(0)

first_enemy.set_hp(one_hp)
first_enemy.attack()
first_enemy.reveal_hp()


try:
 one_hp = int(input("Enter hit points for first enemy"))
except ValueError or one_hp > 100:
 print("Enter only numerical values and less than 100")
 exit(0)

first_enemy.set_hp(one_hp)
first_enemy.attack()
first_enemy.reveal_hp()


# you need to change the if condition as,

#     if self.health_points >= 0 and self._foo__is_dead  == False:
#         print("Enemy Terminated")
#     else:
#         print("Enemy is  dead")

# `self.health_points`