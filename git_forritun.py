#Liður 1
tala1=int(input("Slaðu inn tölu eitt "))
tala2=int(input("Slaðu inn tölu tvö "))
utk1=tala1+tala2
utk2=tala1*tala2
print("Tölurnar lagðar saman: ",utk1)
print("Tölurnar margfaldaðar saman: ",utk2)

#Liður 2
fornafn=input("Slaðu inn fornafn ")
eftirnafn=input("Slaðu inn eftirnafn ")
print("Halló",fornafn,eftirnafn)

#Liður 3
texti=input("Slaðu inn texta ")
tallagstafi=0
talhastafi=0
tallagstafireftir=0
for x in range(len(texti)):
    if (texti[x].isalpha() and texti[x].isupper()):
        talhastafi+=1
        if (texti[x+1].islower()):
            tallagstafireftir+=1
    if (texti[x].isalpha() and texti[x].islower()):
        tallagstafi+=1
print("Það komu",talhastafi,"Hástafir")
print("Það komu",tallagstafi,"Lágstafir")
print("Það komu",tallagstafireftir,"lágstafir koma strax á eftir hástaf")
