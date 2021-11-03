from directory_for_dotamanager import *
from check_player_in_team import player_team

def player_average_skill(name_of_player):
    skill_of_player = (logic[name_of_player] + skill_on_his_pose[name_of_player] + solo_skill[name_of_player] + \
                      team_playing[name_of_player])/4
    return '"'+player_team(name_of_player)+'"'+','+'"'+name_of_player+'"' + ' average skill = ' + str(skill_of_player)


player_name = input('Name of player, which you want to check his average skill: ')

print(player_average_skill(player_name))
