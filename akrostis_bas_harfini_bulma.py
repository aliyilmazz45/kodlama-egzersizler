
with open("siir.txt","w",encoding="utf-8") as dosya:
    dosya.write("Memlekete sis çökmüş bir gece\n")
    dosya.write("Usulca yanağıma sen düşüyorsun\n")
    dosya.write("Sabah saat dokuzu beş geçe\n")
    dosya.write("Terk edip bizleri gidiyorsun\n")
    dosya.write("Ayrılık bu kadar yakmamıştı içimizi\n")
    dosya.write("Farkında mısın bilmiyorum\n")
    dosya.write("Aldın beraberinde cumhuriyetimizi\n")
    dosya.write("Korkunç bir veda, sararmıştı her yer\n")
    dosya.write("Ellerini uzat tutmak istiyoruz\n")
    dosya.write("Masmavi gözleri kaybetmiş çocuk\n")
    dosya.write("Aldı bir sabah ruhumuzu\n")
    dosya.write("Lakin nasıl bölmesin yokluğun uykumuzu\n")

bas_harfler = ""
with open("siir.txt","r+",encoding="utf-8") as file:
    for i in file:
        bas_harfler += i[0]
print(bas_harfler)
