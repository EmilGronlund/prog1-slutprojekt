import random
import time

attacks = [
    {
        "name": "Kick👟",
        "damage": 5,
        "cost": 0
    },
    {
        "name": "Boost🔋",
        "boosting": 5,
        "cost": 0
    },
    {
        "name": "Punch🥊",
        "damage": 10,
        "cost": 10
    },
    {
        "name": "Heal💊",
        "healing": 10,
        "cost": 10
    },
    {
        "name": "Stab🔪",
        "damage": 20,
        "cost": 20
    }
]

enemy_attacks = [
    {
        "name": "Stomp👣",
        "damage": 5
    },
    {
        "name": "Bite🦷",
        "damage": 10
    },
    {
        "name": "Club Strike💢",
        "damage": 20
    }
]

boss_attacks = [
    {
        "name": "Tail Whip🐉",
        "damage": 5
    },
    {
        "name": "Fire Breath🔥",
        "damage": 10
    },
    {
        "name": "Meteorite💥",
        "damage": 20
    }
]

while True:
    hp_player = 100
    hp_enemy = 100
    energy_player = 0

    while hp_player > 0 and hp_enemy > 0:

        print(f"Energy: {energy_player}⚡")

        try:
            choice = int(input(
                            "1 - Kick👟     (0⚡)\n"
                            "2 - Boost🔋    (0⚡)\n"
                            "3 - Punch🥊    (10⚡)\n"
                            "4 - Heal💊     (10⚡)\n"
                            "5 - Stab🔪     (20⚡)\n"
                            "Choose an attack: "
                            ))
            if choice < 1 or choice > 5:
                print("Invalid input❌ You must choose an integer between 1 - 5.")
                continue

        except ValueError:
            print("Invalid input❌ You must choose an integer between 1 - 5.")
            continue

        attack = attacks[choice - 1]

        if energy_player < attack["cost"]:
            print("You cannot afford that attack❌")
            continue

        energy_player -= attack["cost"]

        if attack["name"] == "Heal💊":
            if hp_player < 100:
                hp_player += attack["healing"]
                print()
                print(f"You used {attack['name']} and healed {attack['healing']} HP!")
            else:
                energy_player += 10
                print("You cannot heal when your HP is full❌")
                continue

        elif attack["name"] == "Boost🔋":
            energy_player += attack["boosting"]
            print()
            print(f"You used {attack['name']} and received +5 energy!⚡")

        else:
            critical_hit = random.randint(1, 6)
            if critical_hit == 6:
                hp_enemy -= attack["damage"] + 5
                print()
                print(f"Critical hit!💥 You used {attack['name']} and the monster took {attack['damage']} + 5 damage.")
            else:
                hp_enemy -= attack["damage"]
                print()
                print(f"You used {attack['name']} The monster took {attack['damage']} damage.")

        if hp_enemy > 0:
            enemy_attack = random.choice(enemy_attacks)

            critical_hit = random.randint(1, 6)
            if critical_hit == 6:
                hp_player -= enemy_attack["damage"] + 5
                print(f"Critical hit!💥 The monster used {enemy_attack['name']} and you took {enemy_attack['damage']} + 5 damage.")
            else:
                hp_player -= enemy_attack["damage"]
                print(f"The monster used {enemy_attack['name']} You took {enemy_attack['damage']} damage.")

        print(f"Your HP: {hp_player}/100❤️  | Monster HP: {hp_enemy}/100❤️\n")
        energy_player += 10
        time.sleep(1)

    if hp_player > 0:
        print("You defeated the monster!🏆")
        question = input("Do you want to proceed to the final boss fight?🕹️ (j/n): ").lower()
        if question == "n":
            print("Session terminated.👾")
            break
        else:
            while True:
                hp_player = 100
                hp_boss = 100
                energy_player = 0

                while hp_player > 0 and hp_boss > 0:

                    print(f"Energy: {energy_player}⚡")

                    try:
                        choice = int(input(
                                        "1 - Kick👟     (0⚡)\n"
                                        "2 - Boost🔋    (0⚡)\n"
                                        "3 - Punch🥊    (10⚡)\n"
                                        "4 - Heal💊     (10⚡)\n"
                                        "5 - Fireball🔥 (20⚡)\n"
                                        "Choose an attack: "
                                        ))
                        if choice < 1 or choice > 5:
                            print("Invalid input❌ You must choose an integer between 1 - 5.")
                            continue

                    except ValueError:
                        print("Invalid input❌ You must choose an integer between 1 - 5.")
                        continue

                    attack = attacks[choice - 1]

                    if energy_player < attack["cost"]:
                        print("You cannot afford that attack❌")
                        continue

                    energy_player -= attack["cost"]

                    if attack["name"] == "Heal💊":
                        hp_player += attack["healing"]
                        print()
                        print(f"You used {attack['name']} and healed {attack['healing']} HP!")

                    elif attack["name"] == "Boost🔋":
                        energy_player += attack["boosting"]
                        print()
                        print(f"You used {attack['name']} and received +5 energy!⚡")

                    else:
                        critical_hit = random.randint(1, 6)
                        if critical_hit == 6:
                            hp_boss -= attack["damage"] + 5
                            print()
                            print(f"Critical hit!💥 You used {attack['name']} and the dragon took {attack['damage']} + 5 damage.")
                        else:
                            hp_boss -= attack["damage"]
                            print()
                            print(f"You used {attack['name']} The dragon took {attack['damage']} damage.")

                    if hp_boss > 0:
                        boss_attack = random.choice(boss_attacks)

                        critical_hit = random.randint(1, 6)
                        if critical_hit == 6:
                            hp_player -= boss_attack["damage"] + 5
                            print(f"Critical hit!💥 The dragon used {boss_attack['name']} and you took {boss_attack['damage']} + 5 damage.")
                        else:
                            hp_player -= boss_attack["damage"]
                            print(f"The dragon used {boss_attack['name']} You took {boss_attack['damage']} damage.")

                    print(f"Your HP: {hp_player}/100❤️  | Dragon HP: {hp_boss}/100❤️\n")
                    energy_player += 10
                    time.sleep(1)

                if hp_player > 0:
                    print("You defeated the dragon!🏆")
                    question = input("Do you want fight the dragon again?🕹️  (j/n): ")
                    if question == "n":
                        print("Session terminated.👾")
                        break
                    else:
                        continue

                else:
                    print("You died...💀")
                    question = input("Do you want fight the dragon again?🕹️  (j/n): ").lower()
                    if question == "n":
                        print("Session terminated.👾")
                        break
                    else:
                        continue

    else:
        print("You died...💀")
        question = input("Do you want to try again?🕹️  (j/n): ").lower()
        if question == "n":
            print("Session terminated.👾")
            break
        else:
            continue
