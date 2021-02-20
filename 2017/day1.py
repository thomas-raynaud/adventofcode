def getSumDigits(d1, d2):
    sumDigits = (int(d1) if d1 == d2 else 0)
    return sumDigits

input = open('input.txt', 'r').read().replace('\n', '')

index = 0
total_step1 = 0
total_step2 = 0
while(index < len(input)):
    total_step1 += getSumDigits(input[index], input[(index + (len(input) / 2)) % len(input)])
    total_step2 += getSumDigits(input[index], input[(index + 1) % len(input)])
    index += 1
print 'Total step 1: ', total_step1
print 'Total step 2:', total_step2
