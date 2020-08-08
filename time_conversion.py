s = "12:25:47PM"

txt = s.split(':')
if 'PM' in txt[2]:
    if txt[0] == '12':
        time = s
    else:    
        num = int(txt[0]) + 12
        time = (str(num)+":"+txt[1]+":"+txt[2])

elif (('AM' in txt[2]) & (txt[0] == '12')):
    txt[0] = '00'
    time = (txt[0]+":"+txt[1]+":"+txt[2])

else:
    time = s    
print(time[:-2])
    