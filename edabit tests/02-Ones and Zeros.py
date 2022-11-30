def same_length(txt):
    if len(txt) % 2 != 0:
        return False
    temp0 = 0
    temp1 = 0
    for i in range(len(txt)):
        if txt[i] == '1':
            if temp0 == 0:
                temp1 += 1
            else:
                if temp0 == temp1:
                    temp0 = temp1 = 0
                    temp1 = + 1
                else:
                    return False
        elif txt[i] == '0':
            if temp1 == 0:
                pass
            else:
                temp0 += 1
    return True


x = same_length('1010')
print(x)