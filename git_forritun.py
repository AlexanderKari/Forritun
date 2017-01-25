#Alexander Kári Ragnarsson
#Kt: 0404002220
#25.1.2017
#Forritun

#Liður 1
tala1=int(input("Slaðu inn tölu eitt "))
tala2=int(input("Slaðu inn tölu tvö "))
#spyr notanda um að sla inn tölur
utk1=tala1+tala2
utk2=tala1*tala2
#læt forritið reikna út tölurnar
print("Tölurnar lagðar saman: ",utk1)
print("Tölurnar margfaldaðar saman: ",utk2)
#Prenta tölurnar út lagðar saman og margfaldaðar

#Liður 2
fornafn=input("Slaðu inn fornafn ")
#Spyr um fornafn
eftirnafn=input("Slaðu inn eftirnafn ")
#Spyr um eftirnafn
print("Halló",fornafn,eftirnafn)
#Prenta út nöfnin með Halló í byrjun

#Liður 3
#Spyr notanda um texta
texti=input("Slaðu inn texta ")
tallagstafi=0
talhastafi=0
tallagstafireftir=0
#bý til teljara fyrir lagstafi, Hástafi og lágstafi eftir hástaf
for x in range(len(texti)):
    #Ef stafurinn í texta er bókstafur og er i hástaf
    if (texti[x].isalpha() and texti[x].isupper()):
        #Bæti 1 við teljara fyrir hástaf
        talhastafi+=1
        #Ef næsti stafur er lagstafur
        if (texti[x+1].islower()):
            #Bæti 1 við teljara fyrir lágstaf eftir hástaf
            tallagstafireftir+=1
    #Ef stafurinn í texta er bókstafur og er i lágstaf
    if (texti[x].isalpha() and texti[x].islower()):
        #Bæti 1 við teljara fyrir lágstaf
        tallagstafi+=1
#Birti fjölda Hástafi
print("Það komu",talhastafi,"Hástafir")
#Birti fjölda Lágstaf
print("Það komu",tallagstafi,"Lágstafir")
#Birti fjölda Lágstaf eftir hástaf
print("Það komu",tallagstafireftir,"lágstafir koma strax á eftir hástaf")
