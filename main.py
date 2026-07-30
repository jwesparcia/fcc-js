def number_pattern(n):    
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n <= 0:
        return'Argument must be an integer greater than 0.'
    else:
        numbers = []
        for i in range(1,n+1):
            numbers.append(str(i))
        return ' '.join(numbers)
            

print(number_pattern(4))


    
