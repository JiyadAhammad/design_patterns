from domain.character import Character


if __name__ == "__main__":
    hero = Character("Aria", 100, 15,10)
    goblin = Character("Goblin", 30, 5,20)

    thanos = Character("Thanos", 80, 30,25)


    print(hero.describe())
    print(goblin.describe())


    hero.attack(goblin)
    print(goblin.describe())

    goblin.increase_health(goblin)
    print(goblin.describe())

    # ==================================

    print(thanos.describe())
    print(goblin.describe())
    
    
    thanos.attack(goblin)
    print(goblin.describe())
    
    goblin.increase_health(goblin)
    print(goblin.describe())

