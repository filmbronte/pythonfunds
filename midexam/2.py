import math

command = input().split(">>")
initial_tax = 0
total_tax = 0
tax_increase = 0
cost_to_collect = 0

for el in command:
    car_type, years, kilometers = el.split()
    years = int(years)
    kilometers = int(kilometers)

    if car_type == "family":

        initial_tax = 50
        x = abs(math.floor(kilometers / 3000))
        tax_increase = 12 * x
        total_tax = tax_increase + (50 - years * 5)
        print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")
        cost_to_collect += total_tax

    elif car_type == "heavyDuty":

        initial_tax = 80
        x = abs(math.floor(kilometers / 9000))
        tax_increase = 14 * x
        total_tax = tax_increase + (80 - years * 8)
        print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")
        cost_to_collect += total_tax

    elif car_type == "sports":

        initial_tax = 100
        x = abs(math.floor(kilometers / 2000))
        tax_increase = 18 * x
        total_tax = tax_increase + (100 - years * 9)
        print(f"A {car_type} car will pay {total_tax:.2f} euros in taxes.")
        cost_to_collect += total_tax

    else:
        print("Invalid car type.")


print(f"The National Revenue Agency will collect {cost_to_collect:.2f} euros in taxes.")

