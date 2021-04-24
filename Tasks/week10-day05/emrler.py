''' 
Aşağıdakı tələblərə cavab verən console app yazmağınız tələb olunur
Proqramın Menyusu --Salam mini HR proqramına xoş gəlmisiniz--

Zəhmət olmasa sizə uyğun əmri seçin

Yeni işçi əlavə et
İstifadəçi məlumatlarına bax
Ümumi maaş cəmini göstər
İşçi sayını göstər
Ən köhnə işçini göstər
Ən yeni işçini göstər
Əsas menyuya qayıt
=====================================
emr=''
print('--Menim dunyama xos gelmisiniz--')
def emrler():
    print('Emrlerden biri sec')
    print('1. Ekrana salam yazdir')
    print('2. Ekrana sag ol yazdir')
    print('3. Ekrana buralarda ol yazdir')
    emr=input('Istediyiniz emri daxil edin : ')

emrler()



if emr=='1':
    print('salam')
elif emr=='2':
    print('sag ol')
elif emr=='3':
    print('buralarda ol')
else:
    print('Sizin emre uygun netice tapilmadi.')
    emrler()
'''