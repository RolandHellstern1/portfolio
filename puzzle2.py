from operator import xor

file1 = open('/home/roland/projects/advent/puzzle2.data', 'r')
Lines = file1.readlines()
file1.close()

valid = 0
valid1 = 0

for line in Lines:

    s = line.split(" ")
    s[0] = s[0].split("-")
    s[2] = s[2].replace('\n', '')
    s[1] = s[1].replace(':', '')
    count = s[2].count(s[1])



    if count >= int(s[0][0]) and count <= int(s[0][1]):
        valid = valid +1

print(valid)


for line in Lines:
    s = line.split(" ")
    s[0] = s[0].split("-")
    s[2] = s[2].replace('\n', '')
    s[1] = s[1].replace(':', '')

    if xor(bool(s[2][int(s[0][0])-1] == s[1]), bool(s[2][int(s[0][1])-1] == s[1])):
        valid1 = valid1 + 1



print(valid1)
