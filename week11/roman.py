def decToRoman(n):
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50,'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, "V"), (4, "IV"),
        (1, "I")
        ]
    result = ""
    ins = 0
    try:
        ins = int(n)
    except ValueError:
        pass
        
    for value,letters in romans:
        while ins >= value:
            result += letters
            ins-= value
    return result

def RomanTodec(n):
    romans = {
        'M' : 1000 ,'CM': 900 ,'D': 500 , 'CD':400,
        'C' :100 ,'XC' :90, 'L': 50 , 'XL': 40,
        'X' :10 ,'IX': 9, "V": 5, "IV": 4,
        "I":1
        }
    inc = 0
    result = 0
    la = len(n)
    while la != 0: 
        if n[:2] in romans and inc == 0:
            result += romans[n[:2]]
            n = n[2:]
            la -=2
        if la >0:
            if n[0] in romans and inc == 1:
                result += romans[n[0]]
                n = n[1:]
                inc = 0
                la -= 1
        if inc == 2:
            return "Error"
        inc +=1
    
        

    return str(result)
