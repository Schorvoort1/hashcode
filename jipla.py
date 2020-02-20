text = open('a_example.txt','r')
textinlijntjes = text.readlines()
y = []
scoretot = []
for getallen in range(len(textinlijntjes)):
    y.append(textinlijntjes[getallen].split())
aantal = int(y[0][1])
for i in range(aantal):
    score = 0
    boekscore = 0
    for t in range(int(y[2+2*i][0])):
        boekscore = int(y[1][int(y[3+2*i][t])])
        score = score + boekscore
    scoretot.append(score)
Bestebib = scoretot.index(max(scoretot))
Boekengoed = y[3+2*Bestebib]
c = 1
c2 = 0
Bibscorepb = []
Jeej = 0
dagenover = 0
o = 0
Boekenleuk = []
for l in y[4][0]:
    try:
        o = Boekengoed.index(l)
    except:
        Boekenleuk.append(l)
for d in range(int(y[0][2])):
    if c == int(y[2+2*Bestebib][1]):     
        for t in range(int(y[2+2*Bestebib][0])):
            boekscore = int(y[1][int(y[3+2*Bestebib][t])])
            Bibscorepb.append(boekscore)
        dagennodig = int(y[2+2*Bestebib][0])//int(y[2+2*Bestebib][2])
        if int(y[2+2*Bestebib][0])%int(y[2+2*Bestebib][2]) != 0:
            dagennodig+=1
        if dagennodig < (int(y[0][2]) - d):
            dagenover = dagennodig
        else:
            dagenover = (int(y[0][2]) - d)
        for h in range(dagenover):
            for t in range(int(y[2+2*Bestebib][0])):
                if len(Bibscorepb) != 0:
                    Boekmomenteel = max(Bibscorepb)
                    Jeej = Boekmomenteel + Jeej
                    Bibscorepb.pop(Bibscorepb.index(Boekmomenteel))
    if c == int(y[2+2*Bestebib][1]) + int(y[4+2*Bestebib][1]):     
        for t in range(len(Boekenleuk)):
            boekscore = int(y[1][int(Boekenleuk[t])])
            Bibscorepb.append(boekscore)
        dagennodig = len(Boekenleuk)//int(y[2+2*Bestebib][2])
        if len(Boekenleuk)%int(y[2+2*Bestebib][2]) != 0:
            dagennodig+=1
        if dagennodig < (int(y[0][2]) - d):
            dagenover = dagennodig
        else:
            dagenover = (int(y[0][2]) - d)
        for h in range(dagenover):
            for t in range(len(Boekenleuk)):
                if len(Bibscorepb) != 0:
                    Boekmomenteel = max(Bibscorepb)
                    Jeej = Boekmomenteel + Jeej
                    Bibscorepb.pop(Bibscorepb.index(Boekmomenteel))
    c = c + 1
    
print(Jeej)
