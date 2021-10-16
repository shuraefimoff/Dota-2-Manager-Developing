from directory_for_dotamanager import *


def player_skill_team_playing(name_of_player):
    skill_of_team_playing_player = team_playing[name_of_player]
    return '"'+name_of_player+'"' + ' team playing skill = ' + str(skill_of_team_playing_player)


name_player = input('Player, which team playing skill you want to know: ')
print(player_skill_team_playing(name_player))
