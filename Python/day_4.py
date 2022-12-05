from typing import *

def get_file_content(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        
    return lines

def get_elf_ranges(elf_pair: str):
    ranges = []
    for item in elf_pair.split(','):
        bound = item.split('-')
        ranges.append([int(bound[0]), int(bound[1])])
    
    return ranges

def check_for_elf_pair(elf_pair: List):
    ranges = get_elf_ranges(elf_pair=elf_pair)
    first_pair, second_pair = ranges[0], ranges[1]
    
    if first_pair[0] <= second_pair[0] and first_pair[1] >= second_pair[1]: 
        return True
    elif second_pair[0] <= first_pair[0] and second_pair[1] >= first_pair[1]:
        return True
    else:
        return False

def get_contains_pair_count(lines):
    pair_count = 0
    for elf_pair in lines: 
        if check_for_elf_pair(elf_pair):
            pair_count += 1
    return pair_count 

##### QUESTION TWO #####

def check_for_overlap(elf_pair: List):
    group_IDs = get_elf_ranges(elf_pair=elf_pair)
    first_pair, second_pair = group_IDs[0], group_IDs[1]
    
    first_id_section = [x for x in range(first_pair[0], first_pair[1] + 1)]
    second_id_section = [x for x in range(second_pair[0], second_pair[1] + 1)]
    
    if first_pair[0] in second_id_section or first_pair[1] in second_id_section:
        return True
    elif second_pair[0] in first_id_section or second_pair[1] in first_id_section:
        return True
    else:
        return False

def get_contains_overlap(lines: List[str]) -> int:
    overlap_count = 0
    for section in lines:
        if check_for_overlap(elf_pair=section):
            overlap_count += 1
        
    return overlap_count
    
if __name__ == "__main__":
    contents = get_file_content("day_4_input.txt")
    ans = get_contains_pair_count(contents)
    ## FIRST ANSWER
    print(f'First Part Answer: {ans}')
    
    ## SECOND ANSWER
    other_ans = get_contains_overlap(contents)
    print(f'Second Part Answer: {other_ans}')
    
