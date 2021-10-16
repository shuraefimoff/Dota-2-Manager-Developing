from directory_for_dotamanager import *


def player_logic(name_of_player):
    player_logic_skill = logic[name_of_player]
    return '"' + name_of_player + '"' + ' logic = ' + str(player_logic_skill)


name_player = input('Player, which logic you want to know: ')
print(player_logic(name_player))
