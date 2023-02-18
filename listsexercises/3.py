cards = input().split()

terminated = False
first_team_sent_players = []
second_team_sent_players = []

for card in cards:
    if card in first_team_sent_players or card in second_team_sent_players:
        continue

    teams = card.split("-")
    team_name = teams[0]
    player = int(teams[1])

    if team_name == 'A':
        first_team_sent_players.append(card)
    else:
        second_team_sent_players.append(card)

    if len(first_team_sent_players) > 4 or len(second_team_sent_players) > 4:
        terminated = True
        break

initial_player_count = 11
print(f"Team A - {initial_player_count - len(first_team_sent_players)}; Team B - {initial_player_count - len(second_team_sent_players)}")

if terminated:
    print("Game was terminated")






