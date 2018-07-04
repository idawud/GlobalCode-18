rom_num= [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def romanNumeral(num):
    roman=""
    if num <= 0:
        return "ERROR: Number must be a postive number"
    
    for i,r in rom_num:
        while num >= i:
            roman += r
            num -= i
    return roman
    
val = romanNumeral(110)
print(val)