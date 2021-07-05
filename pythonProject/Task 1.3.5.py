from random import randint

roll = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0 }

for i in range (1000):
    roll_sum = randint(0,10)
    n = roll.get(roll_sum) +1
    roll[roll_sum] = n
    print(roll_sum)
print (roll)