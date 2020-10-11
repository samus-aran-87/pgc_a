# fibonacci_cache = {}

# def fibonacci(n):
#     # If we have cached the value, then return it

#     if n in fibonacci_cache:
#         return fibonacci_cache[n]

#     # Complete the NTh term
#     if n in [1,2]:
#         value = 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)
    
#     # Cache the value and return it
#     fibonacci_cache[n] = value
#     return value
 

# for n in range(1,10):
#     print(f"{n} : {fibonacci(n)}")


from functools import lru_cache

# @lru_cache(maxsize = 1000)
@lru_cache()
def fibonacci(n):
    if type(n) != int :
        raise TypeError("n must be a positive integer")
    if n < 1: 
        raise ValueError("n must be a positive integer")
        
    if n in [1, 2]:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,101):
    print(f"{n} : {fibonacci(n)}")

# for n in range(1,501):
#     print(fibonacci(n+1)/fibonacci(n))
