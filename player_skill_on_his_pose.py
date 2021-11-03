from directory_for_dotamanager import *


def player_skill_on_his_pose(name_of_player):
    player_skill_pose = skill_on_his_pose[name_of_player]
    return '"' + name_of_player + '"' + ' skill on his pose = ' + str(player_skill_pose)


name_player = input('Player, which skill on his pose you want to know: ')
print(player_skill_on_his_pose(name_player))
