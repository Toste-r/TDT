сonnection()

strng = query#input('BogDan, ')
strng = strng.lower()
strng = strng.split()


sel = ['find','show','print']
ins = ['add','insert']
rem = ['delete','remove']

for i in range(len(sel)):
    if sel[i] in strng:
        select(strng,'select')
for i in range(len(ins)):
    if ins[i] in strng:
        insert(strng)
for i in range(len(rem)):
    if rem[i] in strng:
        select(strng,'delete')