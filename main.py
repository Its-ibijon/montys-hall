import random

doors = ['deathA', 'life', 'deathB']

runs = 0

no_switch_wins = 0
switch_wins = 0

def switch_sim():
    data = ['deathA', 'deathB', 'life']
    con_item = random.choice(doors)
    if con_item == 'deathA':
        data.remove('deathB')
    elif con_item == 'life':
        data.remove(random.choice(['deathA', 'deathB']))
    elif con_item == 'deathB':
        data.remove('deathA')
    data.remove(con_item)
    if data[0] == 'deathA' or data[0] == 'deathB':
        return False
    elif data[0] == 'life':
        return True

def no_switch_sim():
    con_item = random.choice(doors)
    if con_item == "life":
        return True
    elif con_item == "deathA" or con_item == "deathB":
        return False

for i in range(0, 999999):
    runs += 1
    if no_switch_sim():
        no_switch_wins += 1
    if switch_sim():
        switch_wins += 1


print(f'Number of Runs: {runs}')

print(f'Number of Wins [No Switch]: {no_switch_wins}')
print(f'Win Probability [No Switch]: {no_switch_wins/runs*100}%')

print(f'Number of Wins [Switch]: {switch_wins}')
print(f'Win Probability [Switch]: {switch_wins/runs*100}%')
