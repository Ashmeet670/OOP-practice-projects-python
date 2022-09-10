
# A class for making characters in a video game

class Character():

    def __init__(self, type, weapon, health, speed, CanFly):

        self.type = type
        self.weapon = weapon
        self.health = health
        self.speed = speed
        self.CanFly = CanFly


tony = Character(type="player", weapon="repulsor lasers",
                 health="110", speed="125", CanFly=True)
steve = Character(type="player", weapon="disc",
                  health="120", speed="120", CanFly=False)
chris = Character(type="player", weapon="hammer",
                  health="150", speed="150", CanFly=True)
clint = Character(type="player", weapon="bow",
                  health="100", speed="110", CanFly=False)
tom = Character(type="enemy", weapon="Magic staff",
                health="145", speed="115", CanFly=False)

tonyHealth = tony.health
steveSpeed = steve.speed
chrisWeapon = chris.weapon
clintFly = clint.CanFly
tomType = tom.type

print(tonyHealth)
print(chrisWeapon)
print(tom.weapon)
print(tony.weapon)
