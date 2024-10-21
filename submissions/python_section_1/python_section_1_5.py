import re

def find_all_dates(text):
    patterns = [
        r'\b\d{2}-\d{2}-\d{4}\b',  # dd-mm-yyyy
        r'\b\d{2}/\d{2}/\d{4}\b',  # mm/dd/yyyy
        r'\b\d{4}\.\d{2}\.\d{2}\b'  # yyyy.mm.dd
    ]
    
    combined_pattern = '|'.join(patterns)
    
    matches = re.findall(combined_pattern, text)
    
    return matches

text = input()
output = find_all_dates(text)
print(output) 
