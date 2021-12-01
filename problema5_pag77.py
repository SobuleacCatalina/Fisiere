'''REZOLVĂ!Într-un fişier sunt înscrise caractere arbitrare.Elaboraţi un program care afişează pe ecran 
numărul vocalelor din fişier.'''
f= open('CITIRE.txt','r')
caractere=f.readline()
f.close()
f= open('SCRIERE.txt','w')
k=0
vocalefisier=[]
for i in range(len(caractere)):
    if ((caractere[i]=='A')or(caractere[i]=='E')or(caractere[i]=='I')or(caractere[i]=='O')or(caractere[i]=='U')or(caractere[i]=='a')or(caractere[i]=='e')or(caractere[i]=='i')or(caractere[i]=='o')or(caractere[i]=='u')):
        vocalefisier.extend(caractere[i])
        k+=1
f.write(str(vocalefisier))
f.write('\n')
f.write('numarul de vocale= '+str(k))
f.close()