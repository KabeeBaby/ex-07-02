#print('five point one')
numlist = list()

while True:
    sval = input('enter a number: ')
    if sval == 'done' :
        break

    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue

    numlist.append(fval)



print('Maximum is ', max(numlist))

print('Minimum is ', min(numlist))
