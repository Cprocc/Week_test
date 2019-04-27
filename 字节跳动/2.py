a = [1,0,0,1,1,0,1,0,1,0]
len_list = [0]*len(a)
parent_list = [0]*len(a)
temp_list = []
for i in range(len(a)):
    t_a = a[:]
    len_list = [0]*len(a)
    if a[i]==0:
        t_a[i]=1
        for j in range(i+1, len(a)):
            tt_a = t_a[:]
            if a[j]==0:
                tt_a[j]=1
                print(tt_a)
                for i in range(len(a)):
                    value = tt_a[i]
                    if tt_a[i]==1:
                        if i-1>=0 and tt_a[i-1]==1:
                            len_list[i] = len_list[i-1]+1
                        else:
                            len_list[i]=1
                temp_list.append(max(len_list))


print(max(temp_list))

