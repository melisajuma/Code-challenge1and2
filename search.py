def search(list,num):
    if num in list:
        return list.index(num)
    else:
        return -1

print(search([3,34,2,1,2,5,7,2],2))