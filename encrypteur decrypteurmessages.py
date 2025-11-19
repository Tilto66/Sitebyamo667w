import string
import time
import pickle
import os.path
JEUCAR = string.printable[:-5]
CARSUBTI = JEUCAR[-6:] + JEUCAR[:-6]
DICO_ENCRYP ={}
DICO_DECRYP ={}
for i,k in enumerate(JEUCAR):
    v = CARSUBTI[i]
    DICO_ENCRYP[k]=v
    DICO_DECRYP[v]=k
for c in string.printable[-5:]:
    DICO_ENCRYP[c]=c
    DICO_DECRYP[c]=c
##NOMFIC_IN = "cryptopy_in.pickle"
##NOMFIC_OUT = "cryptopy_out.pickle"
def encrypter(texteclair, vardico_cryp):
    textesecret = []
    for k in texteclair :
        v = vardico_cryp[k]
        textesecret.append(v)
    return ''.join(textesecret)


def decrypter(textesecret, vardico_decryp):
    texteclair = []
    for k in textesecret :
        v = vardico_decryp[k]
        texteclair.append(v)
    return ''.join(texteclair)
##def sauver(self):
##    with open(NOMFIC_IN, 'wb')as ficow:
##        pickle.dump(self,ficow)
##    with open(NOMFIC_OUT, 'wb')as ficor:
##        pickle.dump(self, ficor)

input("~~~~Encrypt or decrypt your messages with Caesar discrepancy~~~~")
input("Pay attention : not insert special characters (é,à,è,$...)")
z=input("Do you want translate since (h)ere or since a (c)ard index :")
##if z=="c" or z=="C":
##    pass
##    sauver
##    input("You need two card index : cryptopy_in.txt and cryptopy_out.txt. When it's right, press enter")
##    a = input("Do you want (e)ncrypt or (d)ecrypt ? :")
##    if os.path.exists(NOMFIC_IN)and os.path.exists(NOMFIC_OUT):
##        if a =="e" or a =="E":
##            print("Lecture...")
##            with open(NOMFIC_IN,'r')as fic_lect:
##                message = fic_lect.read()
##                with open(NOMFIC_OUT,'w')as fic_ecri:
##                    for g in range(0,26):
##                        CARSUBTI = JEUCAR[-g:] + JEUCAR[:-g]
##                        DICO_ENCRYP ={JEUCAR[i]: CARSUBTI[i] for i in range(len(JEUCAR))}
##                        txt_resultat = encrypter(message, DICO_ENCRYP)
##                        fic_ecri.write(txt_resultat)
##                        time.sleep(0.001)
##
##        elif a=="d" or a =="D":
##            print("Lecture...")
##    
if z=="h" or z=="Z":
    a = input("Do you want (e)ncrypt or (d)ecrypt ? :")
    if a =="e" or a =="E":
        nbr = int(input("What discrepancy do you want ? Ex : 7 Min: 1 Max: 26 If you want try all possibilities, enter 0 : "))
        if nbr==0:
            message = input("Message to encrypt :")
            for g in range(26):
                CARSUBTI = JEUCAR[-g:] + JEUCAR[:-g]
                DICO_ENCRYP ={JEUCAR[i]: CARSUBTI[i] for i in range(len(JEUCAR))}
                textesecret = encrypter(message, DICO_ENCRYP)
                print(f"[Discrepancy {g:2d} : {textesecret}]")
                time.sleep(0.001)

                
        elif nbr>=1 and nbr<=26:
            message = input("Message to encrypt :")
            for g in range(26):
                CARSUBTI = JEUCAR[-g:] + JEUCAR[:-g]
                DICO_ENCRYP ={JEUCAR[i]: CARSUBTI[i] for i in range(len(JEUCAR))}
                textesecret = encrypter(message, DICO_ENCRYP)
                time.sleep(0.001)
                if g==nbr:
                    print(f"[Discrepancy {g:2d} : {textesecret}]")
            

    elif a=="d" or a =="D":
        if nbr==0:
            message = input("Message to decrypt :")
            for g in range(1,26):
                CARSUBTI = JEUCAR[-g:] + JEUCAR[:-g]
                DICO_ENCRYP ={JEUCAR[i]: CARSUBTI[i] for i in range(len(JEUCAR))}
                DICO_DECRYP = {v: k for k,v in DICO_ENCRYP.items()}
                texteclair = encrypter(message, DICO_DECRYP)
                print(f"[Discrepancy {g:2d} : {texteclair}]")
                time.sleep(0.001)
        elif nbr>=1 and nbr<=26:
            message = input("Message to encrypt :")
            for g in range(26):
                CARSUBTI = JEUCAR[-g:] + JEUCAR[:-g]
                DICO_DECRYP ={JEUCAR[i]: CARSUBTI[i] for i in range(len(JEUCAR))}
                texteclair = decrypter(message, DICO_DECRYP)
                time.sleep(0.001)
                if g==nbr:
                    print(f"[Discrepancy {g:2d} : {texteclair}]")


           
   
