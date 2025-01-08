

player_stats = { 'eden': 
                {'points': 25, 
                 'rebounds': 10,
                 'assists': 5 },
                 'roy': 
                 {'points': 33, 
                 'rebounds': 4,
                 'assists': 8   
                 }
                }

for player, stat in player_stats.items():
    print("Player: " + player.title() + "\nPoints Scored: " + str(stat['points'])
          + "\nRebounds: " + str(stat['rebounds'])
          + "\nAssists: " + str(stat['assists']))