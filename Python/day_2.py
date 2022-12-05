from typing import List

def get_file_content(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        
    return lines

def get_choice_value(match: str, choice_values):
    return choice_values.get(match[2])
    
def score_turn(winning_combinations: List[str], draw_combos: List[str], match, choice_values) -> int:
    if match in winning_combinations:
        return (6 + get_choice_value(match, choice_values))
    elif match in draw_combos:
        return (3 + get_choice_value(match, choice_values))
    else:
        return (0 + get_choice_value(match, choice_values))
    
def calculate_total_score(winning_combinations, drawing_combinations, hand_values, lines) -> int:
    score = 0
    for match in lines:
        turn_score = score_turn(winning_combinations, drawing_combinations, match.strip(), hand_values)
        score += turn_score
    
    return score

#########################################
######    Second Question ###############
#########################################

def get_rigged_matchup(match, outcomes: List[str], hand_values):
    opponent_choice = match[0]
    for outcome in outcomes:
        if opponent_choice in outcome:
            return hand_values.get(outcome[2]) 


def get_match_score(match, desired_outomes, hand_values, outcomes):
    match_outcome = match[2]
    
    # Need to lose
    if match_outcome == 'X':
        match_score = desired_outcomes.get(match_outcome)
        losing_matchups = outcomes.get('losing_combinations')
        rigged = get_rigged_matchup(match, losing_matchups, hand_values=hand_values)
        match_score += rigged
        return match_score
    
    # Need to tie 
    elif match_outcome == 'Y': 
        match_score = desired_outcomes.get(match_outcome)
        draw_matchups = outcomes.get('drawing_combinations')
        rigged = get_rigged_matchup(match, draw_matchups, hand_values=hand_values)
        match_score += rigged 
        return match_score
    
    # Need to win
    elif match_outcome == 'Z':
        match_score = desired_outcomes.get(match_outcome)
        winning_matchups = outcomes.get('winning_combinations')
        rigged = get_rigged_matchup(match, winning_matchups, hand_values=hand_values)
        match_score += rigged 
        return match_score
    
    
def calculate_strategy_outcome(turns: List[str], desired_outcomes: dict, hand_values, outcomes): 
    total_score = 0
    for match in turns:
        match_score = get_match_score(match.strip(), desired_outcomes, hand_values, outcomes)
        total_score += match_score
       
    return total_score

 
if __name__ == "__main__":
    filename = "day_2_input.txt"
    
    # Define the strings that would make up losing combinations
    outcomes =  {
        "winning_combinations" :['A Y', 'B Z', 'C X'],
        "drawing_combinations" : ['A X', 'B Y', 'C Z'],
        "losing_combinations" : ['A Z', 'B X', 'C Y']
    }
    
    hand_values = {'X': 1,
                   'Y': 2,
                   'Z': 3}
    
    turns = get_file_content(filename=filename)
    
    ''' 
    FIRST QUESTION ANSWER 
    score = calculate_total_score(winning_combinations, drawing_combinations, hand_values, turns)
    print(score)
    '''
    
    desired_outcomes  = {'X': 0,
                         'Y': 3,
                         'Z': 6} 
    
    foo = calculate_strategy_outcome(turns, desired_outcomes, hand_values, outcomes)
    print(f"THE GAME??? {foo}")
    
