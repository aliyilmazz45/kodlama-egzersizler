vize1 = int(input("ilk vize sonucunuzu girin:"))
vize2 = int(input("ikinci vize sonucunuzu girin:"))
final = int(input("final sonucunuzu girin:"))
ortalama = vize1*30/100+vize2*30/100+final*40/100

if ortalama >= 90:
    print("harf notunuz AA")
elif ortalama >=85:
    print("harf notunuz BA")
elif ortalama>=80:
    print("harf notunuz BB")
elif ortalama>=75:
    print("harf notunuz CB")
elif ortalama >= 70:
    print("harf notunuz CC")
elif ortalama>=65:
    print("harf notunuz DC")
elif ortalama>=60:
    print("harf notunuz DD")
elif ortalama>=55:
    print("harf notunuz FD")
elif ortalama<55:
    print("harf notunuz FF")

