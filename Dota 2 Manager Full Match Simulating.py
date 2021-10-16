# Dota 2 Manager/Base of Teams/
import random
from directory_for_dotamanager import *

# Команды и их игроки
from typing import Dict, Union, Any, List

def check_the_players_of_team(name_of_team):
    for i in range(1, 6):
        print('pos', i, '-', teams_players[name_of_team][i], 'skill =',
              team_playing[teams_players[name_of_team][i]] + logic[teams_players[name_of_team][i]] + solo_skill[
                  teams_players[name_of_team][i]] + skill_on_his_pose[teams_players[name_of_team][i]])
    return 'Team: ' + name_of_team


print(check_the_players_of_team('depressedteam'))


def player_skill(name_of_player):
    skill_of_player = logic[name_of_player] + skill_on_his_pose[name_of_player] + solo_skill[name_of_player] + \
                      team_playing[name_of_player]
    return name_of_player + ' skill = ' + str(skill_of_player)


print(player_skill('backpack of pain'))


def player_skill_team_playing(name_of_player):
    skill_of_team_playing_player = team_playing[name_of_player]
    return name_of_player + ' skill = ' + str(skill_of_team_playing_player)


print(player_skill_team_playing('backpack of pain'))


def player_solo_skill(name_of_player):
    player_solo_skill_ = solo_skill[name_of_player]
    return name_of_player + ' skill = ' + str(player_solo_skill_)


print(player_solo_skill('backpack of pain'))


def player_skill_on_his_pose(name_of_player):
    player_skill_pose = skill_on_his_pose[name_of_player]
    return name_of_player + ' skill = ' + str(player_skill_pose)


print(player_skill_on_his_pose('backpack of pain'))


def player_logic(name_of_player):
    player_logic_skill = logic[name_of_player]
    return name_of_player + ' skill = ' + str(player_logic_skill)


print(player_logic('backpack of pain'))


def player_team(name_of_player):
    for i in teams_players:
        if name_of_player in teams_players[i]:
            team_squad = teams_players[i]
            for k, v in teams_players.items():
                if v == team_squad:
                    return name_of_player + ' is playing in ' + k


print(player_team('backpack of pain'))


def match_simulating(team_1_name, team_2_name, match_bo):
    team_1 = teams_players[team_1_name]
    team_2 = teams_players[team_2_name]
    team_1_skill = 0
    team_2_skill = 0
    for i in range(1, 6):
        team_1_skill = team_1_skill + logic[team_1[i]] + skill_on_his_pose[team_1[i]] + solo_skill[team_1[i]] + \
                       team_playing[team_1[i]]
        team_2_skill = team_2_skill + logic[team_2[i]] + skill_on_his_pose[team_2[i]] + solo_skill[team_2[i]] + \
                       team_playing[team_2[i]]
    rate_team_1 = 0
    rate_team_2 = 0
    if team_1_skill > team_2_skill:
        rate_team_2 = (team_1_skill / team_2_skill) * 2
        rate_team_1 = (team_2_skill / team_1_skill) * 2
    elif team_2_skill > team_1_skill:
        rate_team_1 = (team_2_skill / team_1_skill) * 2
        rate_team_2 = (team_1_skill / team_2_skill) * 2
    elif team_2_skill == team_1_skill:
        rate_team_1 = 2.20
        rate_team_2 = 2.20
    print('Rate', team_1_name, ':', round(rate_team_1, 2))
    print('Rate', team_2_name, ':', round(rate_team_2, 2))
    chance_for_team_1 = int(round(rate_team_2, 2) * 100)
    chance_for_team_2 = int(round(rate_team_1, 2) * 100)
    print()
    game_point_team_1 = 0
    game_point_team_2 = 0
    match_winner = ''

    def best_player_match():
        poses = [1, 2, 3, 4, 5]
        if flag_winner_team_1:
            pos_1 = logic[teams_players[team_1_name][poses[0]]] + skill_on_his_pose[
                teams_players[team_1_name][poses[0]]] + solo_skill[teams_players[team_1_name][poses[0]]] + \
                    team_playing[teams_players[team_1_name][poses[0]]]
            pos_2 = logic[teams_players[team_1_name][poses[1]]] + skill_on_his_pose[
                teams_players[team_1_name][poses[1]]] + solo_skill[teams_players[team_1_name][poses[1]]] + \
                    team_playing[teams_players[team_1_name][poses[1]]]
            pos_3 = logic[teams_players[team_1_name][poses[2]]] + skill_on_his_pose[
                teams_players[team_1_name][poses[2]]] + solo_skill[teams_players[team_1_name][poses[2]]] + \
                    team_playing[teams_players[team_1_name][poses[2]]]
            pos_4 = logic[teams_players[team_1_name][poses[3]]] + skill_on_his_pose[
                teams_players[team_1_name][poses[3]]] + solo_skill[teams_players[team_1_name][poses[3]]] + \
                    team_playing[teams_players[team_1_name][poses[3]]]
            pos_5 = logic[teams_players[team_1_name][poses[4]]] + skill_on_his_pose[
                teams_players[team_1_name][poses[4]]] + solo_skill[teams_players[team_1_name][poses[4]]] + \
                    team_playing[teams_players[team_1_name][poses[4]]]
            poses_skill = [pos_1, pos_2, pos_3, pos_4, pos_5]
            player_pos = random.choice(poses)
            print('The best player of the match: ', teams_players[team_1_name][player_pos])
        elif not flag_winner_team_1:
            player_pos = random.randint(1, 5)
            print('The best player of the match: ', teams_players[team_2_name][player_pos])

    if match_bo == 1:
        flag_winner_team_1 = True
        for bo1 in range(1):
            match_point_team_1 = 0
            match_point_team_2 = 0
            minutes = 0
            flag = True
            while flag:
                points_team_1 = random.randint(1, chance_for_team_1)
                points_team_2 = random.randint(1, chance_for_team_2)
                minutes += 20
                print(minutes, 'Minutes')
                print('//////////////////////////////////////////////////////////')

                print('"', team_1_name, '"', 'Points: ', points_team_1, ' ', '"', team_2_name, '"', 'Points: ',
                      points_team_2)
                if points_team_1 > points_team_2:
                    match_point_team_1 += 1
                    print(team_1_name, 'won this 20 minutes period')
                elif points_team_2 > points_team_1:
                    match_point_team_2 += 1
                    print(team_2_name, 'won this 20 minutes period')
                elif points_team_2 == points_team_1:
                    print('Both teams played very good in this 20 min')
                if match_point_team_1 == 2 or match_point_team_2 == 2:
                    print()
                    if match_point_team_1 > match_point_team_2:
                        print(team_1_name, ' Won ')
                        game_point_team_1 += 1
                    elif match_point_team_2 > match_point_team_1:
                        print(team_2_name,
                              ' Won ')
                        game_point_team_2 += 1
                        flag_winner_team_1 = False
                    flag = False
                print('//////////////////////////////////////////////////////////')
            best_player_match()


    elif match_bo == 2:
        for bo2 in range(2):
            flag_winner_team_1 = True
            match_point_team_1 = 0
            match_point_team_2 = 0
            minutes = 0
            flag = True
            while flag:
                points_team_1 = random.randint(1, chance_for_team_1)
                points_team_2 = random.randint(1, chance_for_team_2)
                minutes += 20
                print(minutes, 'Minutes')
                print('//////////////////////////////////////////////////////////')

                print('"', team_1_name, '"', 'Points: ', points_team_1, ' ', '"', team_2_name, '"', 'Points: ',
                      points_team_2)
                if points_team_1 > points_team_2:
                    match_point_team_1 += 1
                    print(team_1_name, 'won this 20 minutes period')
                elif points_team_2 > points_team_1:
                    match_point_team_2 += 1
                    print(team_2_name, 'won this 20 minutes period')
                elif points_team_2 == points_team_1:
                    print('Both teams played very good in this 20 min')
                if match_point_team_1 == 2 or match_point_team_2 == 2:
                    print()
                    if match_point_team_1 > match_point_team_2:
                        print(team_1_name, ' Won ')
                        game_point_team_1 += 1
                    elif match_point_team_2 > match_point_team_1:
                        print(team_2_name,
                              ' Won ')
                        game_point_team_2 += 1
                    flag = False
                print('//////////////////////////////////////////////////////////')
            best_player_match()

    elif match_bo == 3:
        for bo3 in range(3):
            flag_winner_team_1 = True
            match_point_team_1 = 0
            match_point_team_2 = 0
            minutes = 0
            flag = True
            while flag:
                points_team_1 = random.randint(1, chance_for_team_1)
                points_team_2 = random.randint(1, chance_for_team_2)
                minutes += 20
                print(minutes, 'Minutes')
                print('//////////////////////////////////////////////////////////')

                print('"', team_1_name, '"', 'Points: ', points_team_1, ' ', '"', team_2_name, '"', 'Points: ',
                      points_team_2)
                if points_team_1 > points_team_2:
                    match_point_team_1 += 1
                    print(team_1_name, 'won this 20 minutes period')
                elif points_team_2 > points_team_1:
                    match_point_team_2 += 1
                    print(team_2_name, 'won this 20 minutes period')
                elif points_team_2 == points_team_1:
                    print('Both teams played very good in this 20 min')
                if match_point_team_1 == 2 or match_point_team_2 == 2:
                    print()
                    if match_point_team_1 > match_point_team_2:
                        print(team_1_name, ' Won ')
                        game_point_team_1 += 1
                    elif match_point_team_2 > match_point_team_1:
                        print(team_2_name,
                              ' Won ')
                        game_point_team_2 += 1
                    flag = False
                print('//////////////////////////////////////////////////////////')
            best_player_match()
            print(team_1_name, '', game_point_team_1, ':', game_point_team_2, '', team_2_name)
            print()
            if game_point_team_1 == 2 or game_point_team_2 == 2:
                break
        print(team_1_name, '', game_point_team_1, ':', game_point_team_2, '', team_2_name)
        if game_point_team_1 > game_point_team_2:
            match_winner = team_1_name
            print(match_winner, ' Win')
        elif game_point_team_2 > game_point_team_1:
            match_winner = team_2_name
            print(match_winner, ' Win')
        elif game_point_team_1 == game_point_team_2:
            print('Draw')
        return 'Congratulations' + ' ' + match_winner

    if match_bo == 5:
        for bo5 in range(5):
            flag_winner_team_1 = True
            match_point_team_1 = 0
            match_point_team_2 = 0
            minutes = 0
            flag = True
            while flag:
                points_team_1 = random.randint(1, chance_for_team_1)
                points_team_2 = random.randint(1, chance_for_team_2)
                minutes += 20
                print(minutes, 'Minutes')
                print('//////////////////////////////////////////////////////////')
                print('"', team_1_name, '"', 'Points: ', points_team_1, ' ', '"', team_2_name, '"', 'Points: ',
                      points_team_2)
                if points_team_1 > points_team_2:
                    match_point_team_1 += 1
                    print(team_1_name, 'won this 20 minutes period')
                elif points_team_2 > points_team_1:
                    match_point_team_2 += 1
                    print(team_2_name, 'won this 20 minutes period')
                elif points_team_2 == points_team_1:
                    print('Both teams played very good in this 20 min')
                if match_point_team_1 == 2 or match_point_team_2 == 2:
                    print()
                    if match_point_team_1 > match_point_team_2:
                        print(team_1_name, ' Won ')
                        game_point_team_1 += 1
                    elif match_point_team_2 > match_point_team_1:
                        print(team_2_name,
                              ' Won ')
                        game_point_team_2 += 1
                    flag = False
                print('//////////////////////////////////////////////////////////')
            best_player_match()
            if game_point_team_1 == 3 or game_point_team_2 == 3:
                break
    print(team_1_name, '', game_point_team_1, ':', game_point_team_2, '', team_2_name)
    if game_point_team_1 > game_point_team_2:
        match_winner = team_1_name
        print(match_winner, ' Win')
    elif game_point_team_2 > game_point_team_1:
        match_winner = team_2_name

        print(match_winner, ' Win')
    elif game_point_team_1 == game_point_team_2:
        print('Draw')
    return 'Congratulations' + ' ' + match_winner


team1 = input()
team2 = input()
bo_maps = int(input())

print(match_simulating(team1, team2, bo_maps))
print('///////////////////////////////////////////////')
print('///////////////////////////////////////////////')
print('///////////////////////////////////////////////')
print('///////////////////////////////////////////////')
print('///////////////////////////////////////////////')
print('///////////////////////////////////////////////')
print('///////////////////////////////////////////////')
