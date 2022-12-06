def get_file_content(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        
    return lines

def is_unique(char_array):
    return len(set(char_array)) == len(char_array)

def get_character_count(signal, arr_len):
    for i, val in enumerate(signal):
        if i >= arr_len:
            sub_arr = signal[i - arr_len:i]
            if is_unique(sub_arr):
                return i
       
    
if __name__ == "__main__":
    # Return the index of the last item in the first unique 
    jumbled_signal = get_file_content('day_6_input.txt')
    ans = get_character_count(jumbled_signal[0], 4)
    # First Answer
    print(ans)
    # Second Answer
    other_ans = get_character_count(jumbled_signal[0], 14)
    print(other_ans)
    
