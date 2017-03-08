from random import randint
from random import choice

score_table = {'1/8': {}, '1/4': {}, '1/2': {}, 'final': {}}
teams = ['Team1', 'Team2', 'Team3', 'Team4', 'Team5', 'Team6', 'Team7', 'Team8',
         'Team9', 'Team10', 'Team11', 'Team12', 'Team13', 'Team14', 'Team15', 'Team16']
winners_table = {'1/8': [], '1/4': [], '1/2': [], 'final': []}
number_of_pairs = {'1/8': 8, '1/4': 4, '1/2': 2, 'final': 1}


def pairing(teams_list, stage):
    teams_list_copy = list(teams_list)
    for pair_number in range(number_of_pairs[stage]):
        team_1 = teams_list_copy.pop(randint(0, len(teams_list_copy) - 1))
        team_2 = teams_list_copy.pop(randint(0, len(teams_list_copy) - 1))
        team_1_score = randint(1, 10)
        team_2_score = randint(1, 10)
        if team_1_score == team_2_score:
            if choice([team_1, team_2]) == team_1:
                team_1_score += 1
            else:
                team_2_score += 1
        score_table[stage][(team_1, team_2)] = (team_1_score, team_2_score)

        if team_1_score > team_2_score:
            winners_table[stage].append(team_1)
        else:
            winners_table[stage].append(team_2)


def table_printing_by_stages(table):
    stage_print('1/8', table)
    stage_print('1/4', table)
    stage_print('1/2', table)
    stage_print('final', table)


def stage_print(stage, table):
    print(stage)
    for pair, score in table[stage].items():
        print(pair, '-', score)


def print_team_games(table, team):
    print('1/8')
    print(return_team_game_in_stage(table, '1/8', team))
    print('1/4')
    print(return_team_game_in_stage(table, '1/4', team))
    print('1/2')
    print(return_team_game_in_stage(table, '1/2', team))
    print('final')
    print(return_team_game_in_stage(table, 'final', team))


def return_team_game_in_stage(table, stage, team):
    for pair, score in table[stage].items():
        if team in pair:
            return str(pair) + '-' + str(score)
    else:
        return 'This team has no gaems in this stage, m8'

pairing(teams, '1/8')
pairing(winners_table['1/8'], '1/4')
pairing(winners_table['1/4'], '1/2')
pairing(winners_table['1/2'], 'final')

print('----------------------------')
table_printing_by_stages(score_table)
print('----------------------------')

print()
print('----------------------------')
input_team = input('Enter the team name: ')
print_team_games(score_table, input_team)
print('----------------------------')
