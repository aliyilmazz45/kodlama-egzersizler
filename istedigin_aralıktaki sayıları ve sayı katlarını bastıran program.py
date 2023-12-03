baslangic = int(input("baslangıç sayiniz girin:"))
bitis= int(input("bitiş sayınızı girin."))
bölen=int(input("hangi sayıya bölünen sayıları görmek istersiniz:"))

for i in range(baslangic,bitis+1):
    if i%bölen==0:
        print(i)