total = 2000
while True:
    islem = int(input("Lütfen yapmak istediğiniz işlemi seçin\n1-Para çekme\n2-Para Yatırma\n3-Kart Bilgileri\n4-Kart iade"))
    if islem == 1 :
        cekim = int(input("lütfen çekmek istediğiniz tutarı girin"))
        if cekim < total:
            total = total - cekim
            print("çekim işlemi başarılı! {} Tl bakiyeniz kaldı".format(total))
        else:
            print("yetersiz bakiye")
            continue
    elif islem == 2:
        yatırma = int(input("lütfen yatırmak istediğiniz tutarı girin"))
        if yatırma > 0:
            total = total+ yatırma
            print("yatırma işlemi başarılı! yeni bakiyeniz {} Tl".format(total))
        else:
            print("lütfen geçerli bir tutar girin")
    elif islem == 3:
        print("Bakiyeniz {} Tl dir".format(total))
    elif islem == 4:
        print("Kartı iade alınız. ATM den ayrılabilirsiniz.")
        break
print("son")