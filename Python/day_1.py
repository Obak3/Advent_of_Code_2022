def get_file_content(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        
    return lines
   
    
def create_calorie_counts(other):
    calorie_counts = []
    elf_val = 0
    for i, elf in enumerate(other):
        if len(elf) > 1:
            elf_val += int(elf)
        elif len(elf) == 1:
            calorie_counts.append(elf_val)
            elf_val = 0
    return calorie_counts
    

if __name__ == "__main__":
    filename = "day_1_input.txt"
    values = get_file_content(filename=filename)
    baskets = create_calorie_counts(values)
    ans = max(baskets)
    # First answer 
    print(ans)
    # Second answer
    print(sum(baskets[-3:]))
