import itertools

def unique_permutations(arr):
    unique_perms = set(itertools.permutations(arr))
    return [list(perm) for perm in unique_perms]

if __name__ == "__main__":
    input_str = input("Enter a list of integers: ")
    
    arr = list(map(int, input_str.strip('[]').split(',')))
    
    perms = unique_permutations(arr)
    
    print("Unique permutations:")
    print("[")
    for perm in perms:
        print(f"    {perm},")
    print("]")
