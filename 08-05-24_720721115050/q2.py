#Convert the roman to integers

def Convert_to_int(s: str):
    sym={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    total=0
    for i in range(len(s)-1):
        if sym[s[i]]<sym[s[i+1]]:
            total-=sym[s[i]]
        else:
            total+=sym[s[i]]
    return total+sym[s[-1]]

# Use case 1
print("Usecase 1:")
s1='III'
print(Convert_to_int(s1))

#Use case 2:
print("Use case 2:")
s2="LVIII"
print(Convert_to_int(s2))

#Use case 3:
print("Use case 3:")
s3="MCMXCIV"
print(Convert_to_int(s3))