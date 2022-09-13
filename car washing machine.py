import os

besTL= 20
onTL= 20
yirmiTL = 10
elliTL= 30
yuzTL = 5

kasa_bilgileri = [besTL,onTL,yirmiTL,elliTL,yuzTL]

hizmetler = open('hizmetler.txt','w')
hizmetler.write(str(kasa_bilgileri))


HizmetID=[1,2,3,4]
HizmetAd = ['kopukleme','yikama','kurulama','cilalama']
KalanHizmetAdet=[30,50,100,20]
HizmetFiyat = [15,10,5,50]


for i in range(0,4):
    hizmetler.write(('\n{0},{1},{2},{3} TL'.format(HizmetID[i],HizmetAd[i],KalanHizmetAdet[i],HizmetFiyat[i])))

hizmetler = open('hizmetler.txt','r')
print(hizmetler.read())
hizmetler.close()


print('Araç yıkama makinesi 5 TL, 10 TL, 20 TL, 50 TL ve 100 TL’lik banknotlari desteklemektedir.')

bakiye = 0
while True:
    para = int(input("Kac TL yatiracaksiniz= "))


    if para == 5:
        besTL= besTL+1
        kasa_bilgileri.append(besTL+1)
        hizmetler = open('hizmetler.txt','a')
        hizmetler.write(str(besTL))
    elif para == 10:
        onTL= onTL+1
        kasa_bilgileri.append(onTL+1)
        hizmetler = open('hizmetler.txt','a')
        hizmetler.write(str(onTL))
    elif para == 20:
        yirmiTL= yirmiTL+1
        kasa_bilgileri.append(yirmiTL+1)
        hizmetler = open('hizmetler.txt','a')
        hizmetler.write(str(yirmiTL))
    elif para == 50:
        elliTL= elliTL+1
        kasa_bilgileri.append(elliTL+1)
        hizmetler = open('hizmetler.txt','a')
        hizmetler.write(str(elliTL))
    elif para == 100:
        yuzTL= yuzTL+1
        kasa_bilgileri.append(yuzTL+1)
        hizmetler = open('hizmetler.txt','a')
        hizmetler.write(str(yuzTL))
    else:
        bakiye=int(bakiye)-para
        print("Hatali banknot girdiniz!")

    hizmetler.close()

    bakiye = int(bakiye + para)

    islem = input("Para yatirmaya devam edecek misiniz? (evet/hayir) > ")

    while islem.lower() not in ("evet", "hayir"):
        islem = input("Para yatirmaya devam edecek misiniz? (evet/hayir) > ")

    if islem == "hayir":
        print("Toplam {} TL para attiniz.".format(bakiye))
        print("Para yukleme islemi bitiriliyor.")
        break

print('Hizmet Secim Islemi=\n1,kopukleme 15 TL\n2,yikama 10 TL\n3,kurulama 5 TL\n4,cilalama 50 TL')


while True:
      
        hizmet = str(input("Secmek istediginiz hizmetin ID'sini giriniz= "))

        if hizmet == '1':
            if KalanHizmetAdet[0] > 0:
                if bakiye >= 15:
                    KalanHizmetAdet[0]=KalanHizmetAdet[0]-1
                    hizmetler = open('hizmetler.txt','a')
                    hizmetler.write(str(KalanHizmetAdet[0]))
                    bakiye= bakiye-HizmetFiyat[0]
                    kasa_bilgileri.append(besTL-1)
                    kasa_bilgileri.append(onTL-1)
                    print("Kalan bakiyeniz: {} TL".format(bakiye))
                else:
                    print("Bakiyeniz yetmemektedir.")
            else:
                print('Bu hizmet tukenmistir!')

        elif hizmet == '2':
            if KalanHizmetAdet[1] > 0:
                if bakiye >= 10:
                    KalanHizmetAdet[1]=KalanHizmetAdet[1]-1
                    hizmetler = open('hizmetler.txt','a')
                    hizmetler.write(str(KalanHizmetAdet[1]))
                    bakiye= bakiye-HizmetFiyat[1]
                    kasa_bilgileri.append(onTL-1)
                    print("Kalan bakiyeniz: {} TL".format(bakiye))
                else:
                    print("Bakiyeniz yetmemektedir.")
            else:
                print('Bu hizmet tukenmistir!')

        elif hizmet == '3':
            if KalanHizmetAdet[2] > 0:
                if bakiye >= 5:
                    KalanHizmetAdet[2]=KalanHizmetAdet[2]-1
                    hizmetler = open('hizmetler.txt','a')
                    hizmetler.write(str(KalanHizmetAdet[2]))
                    bakiye= bakiye-HizmetFiyat[2]
                    kasa_bilgileri.append(besTL-1)
                    print("Kalan bakiyeniz: {} TL".format(bakiye))
                else:
                    print("Bakiyeniz yetmemektedir.")
            else:
                print('Bu hizmet tukenmistir!')

        elif hizmet == '4':
            if KalanHizmetAdet[3] > 0:
                if bakiye >= 50:
                    KalanHizmetAdet[3]=KalanHizmetAdet[3]-1
                    hizmetler = open('hizmetler.txt','a')
                    hizmetler.write(str(KalanHizmetAdet[3]))
                    bakiye= bakiye-HizmetFiyat[3]
                    kasa_bilgileri.append(elliTL-1)
                    print("Kalan bakiyeniz: {} TL".format(bakiye))
                else:
                    print("Bakiyeniz yetmemektedir.")
            else:
                print('Bu hizmet tukenmistir!')
        
        else:
            print("Hatali Hizmet ID tusladiniz!") 

        hizmetler.close()

        
        hizmet_islemi = input("Hizmet secmeye devam edecek misiniz? (evet/hayir) > ")

        while hizmet_islemi.lower() not in ("evet", "hayir"):
            hizmet_islemi = input("Hizmet secmeye devam edecek misiniz? (evet/hayir) > ")

        if hizmet_islemi == "hayir":
            print("Hizmet secme islemi bitiriliyor.")
            break

if bakiye > 0:
    print("Lutfen para ustunuzu alin = {} TL".format(bakiye))
elif bakiye == 0:
    print("Tum bakiyenizi harcadiniz.")
elif besTL == 0 and bakiye % 5 == 0:
    print("Kasada yeterli para yoktur.")
elif onTL == 0 and bakiye % 10 == 0:
    print("Kasada yeterli para yoktur.")
elif yirmiTL == 0 and bakiye % 20 == 0:
    print("Kasada yeterli para yoktur.")
elif elliTL == 0 and bakiye % 50 == 0:
    print("Kasada yeterli para yoktur.")
elif yuzTL == 0 and bakiye % 100 == 0:
    print("Kasada yeterli para yoktur.")

