import math
def nearest_square(n):
    
    #If n is positive the square of integral part of square root will give the answer
    if n>0:
        i=int(math.sqrt(n))
        return (i*i)

    # If n negative then the closest solution will be zero
    else:
        return 0

nearest_square.__doc__ = """
    This function finds the nearest perfect square number which is less than or equal to the number. """
