from directory_for_dotamanager import *


def player_solo_skill(name_of_player):
    player_solo_skill_ = solo_skill[name_of_player]
    return '"'+name_of_player+'"' + ' solo skill = ' + str(player_solo_skill_)


name_player = input('Player, which solo skill you want to know: ')

print(player_solo_skill(name_player))
