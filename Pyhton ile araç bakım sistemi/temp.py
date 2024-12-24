Tumbakimlar={}
def tamir(ykt,ucret):
    if 0<km<10000:
        print("Lastik değişimi yapılacaktır. İşlem ücreti 500TLdir.\n")
        ucret=ucret+500
    elif 10000<km<40000:
        print("Yağ bakımı yapılacaktır işlem ücreti 1500tldir\n")
        ucret=ucret+1500
    elif 40000<km<80000:
        print("Akü ve filtre değişimi yapılacaktır işlem ücreti 4000tldir\n")
        ucret=ucret+4000
    elif 80000<km<10000:
        print("Motor bakımı yapılacaktır işlem ücreti 8000tldir\n")
        ucret=ucret+8000
    else:
        print("Genel bakım işlemi uygulanacaktır işlem ücreti 150000tldir")
        ucret=ucret+15000
    return ucret
    


while(True):
    print("Araç bakım sistemimize hoş geldiniz\n")
    mod=input("Aracın marka ve modelini giriniz\n")
    ykt=input("Aracın yakıt türünü giriniz\n")
    km=int(input("Km değerini giriniz\n"))
    yas=int(input("Aracın trafikte olduğu süreyi yıl cinsinden giriniz\n"))
    ucret=int(input("Tamir için gerekli öntutarı sisteme yüklemelisiniz. Tutar 200TLdir\n"))
    sonuc=tamir(ykt, ucret)
    genel=[mod,ykt,km]
    ceza=list()
    Tumbakimlar.setdefault(yas,genel)
    gun=int(input("Ödemeyi yapmak için 10 gün süreniz vardır. gün geçilirse ek ödeme istenecektir.Ödemeyi kaçıncı günde yaptınız\n"))
    if gun>10:
        ucret=ucret*5
        ceza.append(ucret)
        print("Ödeyeceğiniz yeni tutar öntutar üzerinden yeniden hesaplanmıştır. tutar {}dır\n".format(ucret))
    else:
        print("İşleminiz tamamlandı.\n")
    durum=input("Başka işlem yapmak istiyor musunuz\n")
    if durum=="evet":
        continue
    else:
        print("Tüm işlemler tamamlanmıştır sistemden çıkıyorsunuz.")
        print("Girdiğiniz bilgiler ve sonuç:")
        print(Tumbakimlar)
        break
    
        
        
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
       
    
    

    
        
        
        
           
        
                                       

            
        
    
       
        
        
        
    




            




    
 
    
    
    
    


                
    


 

    
        