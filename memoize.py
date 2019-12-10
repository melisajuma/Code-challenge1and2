# from prime import prime


def prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0: 
                return False
        else: 
            return True
    else: 
        return False

def memoize(callback):
    cache={}
    def caching(num):
        if num in cache.keys():
            return cache[num]
        cache[num]=callback(num)
        return cache[num]
    return caching

p = memoize(prime)
print(p(4))