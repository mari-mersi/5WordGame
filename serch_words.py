f=open('word5b.txt','r',encoding="utf-8")
filewords=[]
words=[]
for el in f:
    filewords.append(el)
for i in range(0,len(filewords)):
    word=''
    for j in range(0,len(filewords[i])-1):
        word=word+filewords[i][j]
    words.append(word)
yes=[]
no=[]
flag=''
m=0
mes=[]
print("Поиск слова из 5 букв. Введите данные, чтобы закончить введите '0' вместо буквы.")
print("Если в слове есть буква, стоящая на своем месте, то введите букву, затем ее место, например в слове 'дефис', есть буква 'е', стоящая на 2 месте\n"
      "Если в слове есть буква, но не на своем месте, например в том же слове буква 'и' не на 3 месте, тогда нужно написать место '-3'\n\n"
      "Введите буквы которые есть в слове: (буква, место) или (буква, -место)")
while flag!='0':
    flag=input("буква: ")
    if flag!='0':
        yes.append(flag)
        m=int(input("место: "))
        mes.append(m)      
#print(yes)
#print(mes)

flag=''
print("Введите буквы которых нет в слове:")
while flag!='0':
    flag=input()
    if flag!='0':
        no.append(flag)

        
testYES=[]
#print(len(words));print(len(words[0]));print(len(yes))
for i in range(0,len(words)):
    flag=True
    y=[False]*len(yes)
    for k in range(0,len(yes)):
        for j in range(0,len(words[i])):
            if yes[k]==words[i][j]:
                y[k]=True
        if y[k]==False:
            flag=False
    if flag:
        testYES.append(words[i])
        #print(words[i])
print();print('testYES:', len(testYES))

testNO=[]
for i in range(0,len(testYES)):
    flag=True
    for k in range(0,len(no)):
        for j in range(0,len(testYES[i])):
            if no[k]==testYES[i][j]:
                flag=False
    if flag:
        testNO.append(testYES[i])
        #print(testYES[i])
print('testNO', len(testNO));print()

test=[]
for i in range(0,len(testNO)):
    f1=True
    f2=True
    #for j in range(0,len(testNO[i])):
    for k in range(0,len(mes)):
        if mes[k]>0:
            if testNO[i][mes[k]-1]!=yes[k]:
                f1=False
        else:
            if testNO[i][abs(mes[k])-1]==yes[k]:
                f2=False
    if f1 and f2:
        test.append(testNO[i])
        print(testNO[i])
print();print('подходящих слов:', len(test))
                
        
