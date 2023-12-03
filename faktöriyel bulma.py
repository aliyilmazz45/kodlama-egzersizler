sayi= int(input("hangi sayının faktöriyelini bulmak istiyorsunuz:"))
carpim=1
for i in range(1,sayi+1):
    carpim*=i
print(f"{sayi} sayısının faktöriyeli {carpim} sayısına eşittir.")

