import re
def group_by_length(strings):
    grouped_strings = {}
    
    for string in strings:
        string = string.strip()  
        length = len(string)
        
        
        if length not in grouped_strings:
            grouped_strings[length] = []
        grouped_strings[length].append(string)
    
    return dict(sorted(grouped_strings.items()))

if __name__ == "__main__":
    user_input = input("Enter a list of strings").strip()

    input_strings = re.split(r'[^a-zA-Z]+', user_input)
    
    input_strings = list(filter(None, input_strings))
    
    output = group_by_length(input_strings)
    print(output)
