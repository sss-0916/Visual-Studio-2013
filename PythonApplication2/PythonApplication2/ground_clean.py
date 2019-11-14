import math

#for y in range(120):
#    z = 3.365579 * math.pow(10, -12) * math.pow(y, 6) - \
#        9.493974 * math.pow(10, -9) * math.pow(y, 5) + \
#        1.079795 * math.pow(10, -5) * math.pow(y, 4) - \
#        6.407496 * math.pow(10, -3) * math.pow(y, 3) + \
#        2.11638 * math.pow(y, 2) - \
#        3.752817 * math.pow(10, 2) * y + 29193.08
#    print(z)

#for y in range(120):
#    print(math.pow(10, -12) * math.pow(y, 6))

y = 300

z = 3.365579 * math.pow(10, -12) * math.pow(y, 6) - \
    9.493974 * math.pow(10, -9) * math.pow(y, 5) + \
    1.079795 * math.pow(10, -5) * math.pow(y, 4) - \
    6.407496 * math.pow(10, -3) * math.pow(y, 3) + \
    2.11638 * math.pow(y, 2) - \
    3.752817 * math.pow(10, 2) * y + 29193.08

print(z)