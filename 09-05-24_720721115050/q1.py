# Valid Paranthesis

def valid_paranthesis(l: list):
    stack=[]
    pairs={
            "(":")",
            '{':"}",
            "[":"]"
        }
    for i in l:
        if i in pairs:
            stack.append(i)
        elif len(stack)==0 or i!=pairs[stack.pop()]:
            return False
    return len(stack)==0

# Use case 1:
print("Use Case 1:")
l="()"
print(valid_paranthesis(l))

# Use case 2:
print("Use Case 2:")
l2="()[]{}"
print(valid_paranthesis(l2))

# Use case 3:
print("Use Case 3:")
l3="(]"
print(valid_paranthesis(l3))