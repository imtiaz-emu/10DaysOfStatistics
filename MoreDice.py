def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


dice = [1,2,3,4,5,6]
tossed_dice = []
count = 0

for roll1 in dice:
    for roll2 in dice:
        tossed_dice.append((roll1, roll2))
        if(roll1 != roll2):
            if((roll1 + roll2) == 6):
                count += 1


fraction = gcd(len(tossed_dice), count)

print((count//fraction), '/', (len(tossed_dice)//fraction))

