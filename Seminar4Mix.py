# Перемешать список заданыый произвольно. [2,5,7,8] to [2,7,5,8]

import random
list = [2,5,7,8]

i = random.randint(0,len(list))
print(list[i:len(list):1] + list[0:i:1])