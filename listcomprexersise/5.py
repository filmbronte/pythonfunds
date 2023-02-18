rooms = int(input())
free_chairs = 0
game_on = True
for room in range(1, rooms + 1):
    chairs, guests_as_str = input().split()
    guests = int(guests_as_str)

    if guests > len(chairs):
        chairs_needed = guests - len(chairs)
        print(f"{chairs_needed} more chairs needed in room {room}")
        game_on = False
    else:
        free_chairs_by_row = len(chairs) - guests
        free_chairs += free_chairs_by_row

if game_on:
    print(f"Game On, {free_chairs} free chairs left")



