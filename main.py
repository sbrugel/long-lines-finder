maxChars = int(input('Enter max amount of acceptable characters: '))
fname = input('Enter file to check: ')

f = open(fname, "r")
lines = f.readlines()

count = 0
for line in lines:
    count += 1
    if (len(line) > maxChars):
        print('Line ' + str(count) + ' is more than ' + str(maxChars) + ' characters long')
        print('Line contents are: ' + line + '\n')