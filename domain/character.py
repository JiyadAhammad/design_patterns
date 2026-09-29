class Character:
    def __init__(self, name: str, health: int, attack_power: int, heal:int):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.heal = heal


    def describe(self) -> str:
        return f"{self.name} has {self.health} HP and {self.attack_power} ATK"


    def attack(self, target: "Character") -> None:
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

    def increase_health(self,target:"Character")-> None:
        target.health += self.heal
        print(f"{self.name} heals {self.heal}HP health!")
