def prime(num):
    if num > 1:
        for i in range(2,6):
            if (num % i) == 0: 
                return False
        else: 
            return True
    else: 
        return False

print(prime(121))


