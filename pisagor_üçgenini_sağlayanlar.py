def pisagor(a, b):
    pisagor_list=list()
    for i in range(a, b):
        for j in range(a, b):
            c=(i**2+j**2)**0.5
            if c == int(c):
                pisagor_list.append([i, j, int(c)])
    return pisagor_list


baslangic = int(input("araligin baslangic degerini girin:"))
bitis=int(input("araligin bitis degerini girin:"))
for i in pisagor(baslangic, bitis):
    print(i)
