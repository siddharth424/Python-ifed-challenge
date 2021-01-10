import math
def nearest_square(n):

    if n>0:
        i=int(math.sqrt(n))
        return (i*i)
    else:
        return 0
