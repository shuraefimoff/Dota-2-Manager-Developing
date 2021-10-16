from directory_for_dotamanager import *


def player_team(name_of_player):
    for i in teams_players:
        if name_of_player in teams_players[i]:
            team_squad = teams_players[i]
            for k, v in teams_players.items():
                if v == team_squad:
                    return name_of_player + ' is playing in ' + k
