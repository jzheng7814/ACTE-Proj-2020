def remove_index(s1, ind):
    return s1[:ind] + s1[ind + 1:]

def same_indices(s1, s2):
    for i, j, k in zip(s1, s2, range(len(s1))):
        if i == j: yield k

def reduced_str(s1 : str, s2 : str):
    subtract = 0
    for i in same_indices(s1, s2):
        s1 = remove_index(s1, i - subtract)
        s2 = remove_index(s2, i - subtract)
        subtract += 1

    for i, j in zip(range(len(s1)), range(len(s2))):
        if i < len(s2) - 1 and s2[i + 1] == s1[i]:
            s2 = remove_index(s2, i)
            return reduced_str(s1, s2)
        elif (i < len(s1) - 1) and s1[i + 1] == s2[i]:
            s1 = remove_index(s1, i)
            return reduced_str(s1, s2)
    
    return s1, s2

def same_factor(s1, s2):
    same = 0
    for i, j in zip(s1, s2):
        same += ord(i) - ord(j)
    return same + abs(len(s1) - len(s2))

with open(r'C:\Users\jerry\txtfiles\in.txt') as infile:
    for i in infile:
        try:
            print(same_factor(*reduced_str(*i.split())))
        except:
            print(-5)
