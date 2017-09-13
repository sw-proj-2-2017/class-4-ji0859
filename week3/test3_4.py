import pickle

dbfilename = 'test3_4.dat'

#예외처리
#처음으로 입력하는 값이 명령어 다음에 무조건 이름 숫자가 들어가면 예외처리
def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
            scdb += [record]
            
        elif parse[0] == 'del':
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)
                    
        elif parse[0] == 'find':
            for p in scdb:
                if p['Name'] == parse[1]:
                    print(p)
        #숫자변경못함..
        elif parse[0] == 'inc':
            for p in scdb:
                if p['Name'] == parse[1]:
                    amout = int(input("Enter a num:"))
                    Score = int('Score')
                    Score += amout
                    print (p)

        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
