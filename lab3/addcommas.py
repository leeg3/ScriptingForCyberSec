INPUT = 'utccodes.txt'
OUTPUT = 'codes.txt'

f = open(INPUT, 'r')
timezones = f.readlines()
f.close()

f = open(OUTPUT, 'w')

for file in timezones:
    temp = file.rstrip('\n')
    f.write('"' + temp + '"' + ',')
f.close()
