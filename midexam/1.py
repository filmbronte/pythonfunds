needed_exp = float(input())
battles_count = int(input())

exp_received = 0
count = 0
isCollected = False
for i in range(1, battles_count + 1):
    count += 1
    exp_earned = float(input())

    if i % 3 == 0:
        exp_earned += exp_earned * 0.15

    if i % 5 == 0:
        exp_earned -= exp_earned * 0.1

    if i % 15 == 0:
        exp_earned += exp_earned * 0.05

    exp_received += exp_earned

    if exp_received > needed_exp:
        isCollected = True
        break

exp_left = abs(needed_exp - exp_received)
if isCollected:
    print(f"Player successfully collected his needed experience for {count} battles.")
else:
    print(f"Player was not able to collect the needed experience, {exp_left:.2f} more needed.")


