heroes = {}

while True:
    commands = input().split()

    if commands[0] == "End":
        break

    elif commands[0] == "Enroll":
        hero_name = commands[1]

        if hero_name not in heroes:
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif commands[0] == "Learn":
        hero_name = commands[1]
        spell_name = commands[2]

        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name].append(spell_name)

    elif commands[0] == "Unlearn":
        hero_name = commands[1]
        spell_name = commands[2]

        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)

print("Heroes:")
for name, spell in heroes.items():
    print(f'== {name}: {", ".join(spell)}')