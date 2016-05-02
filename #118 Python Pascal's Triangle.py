#118 Pascal's Triangle

def new_list(last_line):
    last_num=len(last_line)
    next_num=last_num+1
    next_line=[1]*next_num
    for i in range(next_num):
        if i==0: 
            next_line[i]=1
        elif i==next_num-1:
            next_line[i]=1
        else:
            next_line[i]=last_line[i-1]+last_line[i]
    return next_line

def generate_tri(num):
    tri=list()
    tri.append([1])
    if num==1:
        return tri
    else:
        for i in range(num-1):
            tri.append(new_list(tri[i]))
        return tri

number_of_layer=raw_input("The Number of Layer of Pascal's Triangle: ")
print generate_tri(int(number_of_layer))
