from itertools import permutations

file = open("dict.txt","r")
dict = []

for word in file:
    # print("{}".format(word.strip()))
    dict += [word.strip()]

def perms(scramble):
    perm = permutations(scramble)
    list = [''.join(i) for i in perm]
    return(list)


permutations = perms(input("enter a scrambled word: "))

# print("here's all it's permutations: {}".format(p))

matches = []

for perm in permutations:
    for word in dict:
        if(perm == word):
            matches += [perm]

print(matches)