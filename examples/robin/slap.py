import random
def coin_toss():
    """ Simulates a coin toss """
    first = random.randint(1,2)
    print("Player " + str(first) + " goes first")
    return first

def use_slap(attacks, damage, opp_health):
    """ Returns the result of using a slap """
    if attacks == 0:
        return attacks, opp_health
    else:
        return attacks - 1, max(opp_health - damage, 0)

def status(turn, opponent, health):
    """ Returns the result of a regular slap """
    print(turn + " has slapped " + opponent + ". " + opponent + " has " + str(health) + " HP left.")  

def victory(winner, loser):
    """ Prints out a victory for the winning player. """
    print(winner + " has slapped " + loser + " silly and wins!")

def slap_fight(app1, app2):
    """ Return the result of a slap fight between 2 compeitors 
    Keyword arguments:
    app1 -- Player 1 and stats
    app2 -- Player 2 and stats
    """
    player_1, player_2 = app1['Name'], app2['Name']
    p1_health, p2_health = int(app1['Health']), int(app2['Health'])
    p1_curr_attacks, p2_curr_attacks = int(app1['Attacks']), int(app2['Attacks'])
    p1_max_attacks, p2_max_attacks = p1_curr_attacks, p2_curr_attacks
    p1_damage, p2_damage = int(app1['Damage']), int(app2['Damage'])
    curr_turn = 1
    #print(player_1 + " VS " + player_2 + '... BEGIN!!!')
    print("Round " + str(curr_turn))
    first = coin_toss()
    if first == 1:
        while p1_health > 0 and p2_health > 0:
            curr_turn += 1
            print("Round " + str(curr_turn))
            while p1_curr_attacks > 0 or p2_curr_attacks > 0:
                if p1_curr_attacks > 0:
                    p1_curr_attacks, p2_health = use_slap(p1_curr_attacks,p1_damage,p2_health)
                    status(player_1, player_2, p2_health) 
                    if p2_health <= 0:
                        break
                if p2_curr_attacks > 0:
                    p2_curr_attacks, p1_health = use_slap(p2_curr_attacks,p2_damage,p1_health)
                    status(player_2, player_1, p1_health)
                    if p1_health <= 0:
                        break
            p1_curr_attacks, p2_curr_attacks = p1_max_attacks, p2_max_attacks
    else:
        while p1_health > 0 and p2_health > 0:
            curr_turn += 1
            print("Round " + str(curr_turn))
            while p1_curr_attacks > 0 or p2_curr_attacks > 0:
                if p2_curr_attacks > 0:
                    p2_curr_attacks, p1_health = use_slap(p2_curr_attacks,p2_damage,p1_health)
                    status(player_2, player_1, p1_health)
                    if p1_health <= 0:
                        break
                if p1_curr_attacks > 0:
                    p1_curr_attacks, p2_health = use_slap(p1_curr_attacks,p1_damage,p2_health)
                    status(player_1, player_2, p2_health)
                    if p2_health <= 0:
                        break
            p1_curr_attacks, p2_curr_attacks = p1_max_attacks, p2_max_attacks
    if p1_health <= 0:
        victory(player_2, player_1)
        return 2
    else:
        victory(player_1, player_2)
        return 1