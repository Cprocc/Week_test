def count_factors(num_intput):
    if num_intput == 1:
        return 1
    num_facotrs = 2
    search = int(num_intput / 2)
    i = 2
    while (i <= search):
        if (num_intput % i == 0):
            if (num_intput / i > i):
                num_facotrs += 2
            elif (num_intput / i == i):
                num_facotrs+=1;
        else:
            break
    i += 1
    return num_facotrs


print(count_factors(10))
print(count_factors(2))