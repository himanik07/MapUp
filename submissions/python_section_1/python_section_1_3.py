import json

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    
    for k, v in d.items():
        
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        
        elif isinstance(v, list):
            for i, item in enumerate(v):
                list_key = f"{new_key}[{i}]"
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, list_key, sep=sep).items())
                else:
                    items.append((list_key, item))
        
        else:
            items.append((new_key, v))
    
    return dict(items)

if __name__ == "__main__":
    user_input = input("Enter a nested dictionary (in JSON format): ")

    try:
        nested_dict = json.loads(user_input)
        if not isinstance(nested_dict, dict):
            raise ValueError("The input should be a dictionary.")
        
        flattened = flatten_dict(nested_dict)
        
        print("\nFlattened dictionary:")
        print(json.dumps(flattened, indent=4))
    
    except json.JSONDecodeError:
        print("Invalid JSON format. Please enter a valid nested dictionary.")
    except ValueError as e:
        print(e)
