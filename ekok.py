def asal_mi(a):
    sayac = 0
    i = 1

    if a == 1:
        return False
    else:
        while i < a+1:
            if a%i == 0:
                sayac += 1
            i += 1
        if sayac == 2:
            return True
        else:
            return False


def ekok(a, b):

    a_bolen_list = list()
    b_bolen_list = list()
    ekok = 1
    i = 2

    while a != 1:
        if a % i == 0 and asal_mi(i):
            a /= i
            a_bolen_list.append(i)
        else:
            i += 1
    i = 2
    while b != 1:
        if b % i == 0 and asal_mi(i):
            b /= i
            b_bolen_list.append(i)
        else:
            i += 1

    for i in a_bolen_list:
        if i in b_bolen_list:
            b_bolen_list.remove(i)

        ekok *= i

    for i in b_bolen_list:
        ekok *= i
    return ekok


sayi1 = int(input ("birinci sayiyi girin:") )
sayi2 = int(input("ikinci sayiyi girin:"))
print(f"{sayi1} ve {sayi2} sayılarının ekoku {ekok(sayi1,sayi2)} sayısıdır")
