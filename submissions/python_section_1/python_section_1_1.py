import ast
def reverse(lst,n):
    result=[]
    for i in range (0,len(lst),n):
        group=[]
        for j in range(min(n,len(lst)-i)):
            group.insert(0,lst[i+j])
        result.extend(group)
    return result
if __name__=="__main__":
    inp=input("Enter input")
    lst_in,n_in=inp.split(',n=')
    lst=ast.literal_eval(lst_in.strip())
    n=int(n_in.strip())
    result=reverse(lst,n)
    print(result)