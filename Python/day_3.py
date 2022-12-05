from iteration_utilities import grouper

def get_file_content(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        
    return lines

def get_priority_value(item, ascii_lowercase, ascii_uppercase):
    if item in ascii_lowercase:
        return ascii_lowercase.index(item) + 1
    else:
        return ascii_uppercase.index(item) + 27

def get_duplicate_item(bag, ascii_lowercase, ascii_uppercase):
    half_idx = int(len(bag)/2)
    first_bag, second_bag = bag[half_idx:], bag[:half_idx] 
    
    for item in first_bag:
        if item in second_bag:
            return get_priority_value(item, ascii_lowercase, ascii_uppercase)

def get_priority_sum(rucksacks, ascii_lowercase, ascii_uppercase):
    cur_sum = 0
    for bag in rucksacks:
        priority_count = get_duplicate_item(bag, ascii_lowercase, ascii_uppercase)
        print(priority_count)
        cur_sum += priority_count
        
    return cur_sum 

########################
### Second Question ####
########################

def sanitize_lines(lines):
    return [i.strip() for i in lines]

def read_in_elf_groups(filename):
    groups = []
    with open(filename, 'r') as infile:
        for lines in grouper(infile, 3, ''):
            groups.append(sanitize_lines(lines))
    return groups 

'''
Imagine I reused the 'get priority_value' function again here
'''

def get_shared_item(group, ascii_lowercase, ascii_uppercase):
    # Sort the groups from smallest to lowest to reduce complexity
    group = sorted(group, reverse=True) 
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return get_priority_value(item, ascii_lowercase, ascii_uppercase)
    
def get_group_priority(groups, ascii_lowercase, ascii_uppercase):
    cur_sum = 0
    for group in groups:
        priority_count = get_shared_item(group, ascii_lowercase, ascii_uppercase)
        cur_sum += priority_count
        
    return cur_sum 


if __name__ == "__main__":
    filename = "day_3_input.txt"
    
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ####################
    ## FIRST QUESTION ##
    #################### 
    '''
    rucksacks = get_file_content(filename=filename)
    
    priority_sum = get_priority_sum(rucksacks=rucksacks,
                                    ascii_lowercase=ascii_lowercase,
                                    ascii_uppercase=ascii_uppercase)
    print(priority_sum)
    '''
    
    #####################
    ## SECOND QUESTION ##
    ##################### 
    
    groups = read_in_elf_groups(filename=filename)
    print(get_group_priority(groups, ascii_lowercase, ascii_uppercase))
