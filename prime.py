def prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0: 
                return False
        else: 
            return True
    else: 
        return False

print(prime(121))


