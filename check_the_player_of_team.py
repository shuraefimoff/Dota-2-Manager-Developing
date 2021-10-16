from directory_for_dotamanager import *


def check_the_players_of_team(name_of_team):
    for i in range(1, 6):
        print('pos', i, '-', teams_players[name_of_team][i], 'skill =',
              team_playing[teams_players[name_of_team][i]] + logic[teams_players[name_of_team][i]] + solo_skill[
                  teams_players[name_of_team][i]] + skill_on_his_pose[teams_players[name_of_team][i]])
    return 'Team: ' + name_of_team


team_name = input('Write a team, which players you want to know: ')
print(check_the_players_of_team(team_name))
