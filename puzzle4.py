file = open('/home/roland/projects/advent/puzzle4.data', 'r')
Lines = file.readlines()
file.close()


clearedNewline = []

for line in Lines:
    line = line.replace('\n', '')
    clearedNewline.append(line)

check = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

splitData = []

passport = []
for line in clearedNewline:
    if line != '':
        line = line.split(' ')
        passport.append(line)
    else:
        splitData.append(passport)
        passport = []
splitData.append(passport)

def flatten(A):
    rt = []
    for i in A:
        if isinstance(i,list): rt.extend(flatten(i))
        else: rt.append(i)
    return rt

flattenData = []
for p in splitData:
    flattenData.append(flatten(p))


passports = []
for p in flattenData:
    newp = []
    for i in p:
        i = i[0: 3:] + i[len(i)::]
        newp.append(i)
    passports.append(newp)

counter = 0
for p in passports:
    if((set(p) & set(check)) == set(check)):
        counter = counter + 1

print(counter)
