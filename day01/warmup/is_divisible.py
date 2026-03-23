def is_divisible(n:int, d: int)->bool:
        """Checks if n is evenly divisible by d."""
        if d==0:
            raise ZeroDivisionError("Divisor 'd' can not be )")
        return n%d == 0

print(is_divisible(10,2)) # True
print(is_divisible(10,3)) # False
print(is_divisible(10,0)) # throw error
    
    