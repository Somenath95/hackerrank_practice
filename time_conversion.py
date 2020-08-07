s = "04:25:47PM"

txt = s.split(':')
if 'P' in txt[2]:
    num = int(txt[0]) + 12
    time = (str(num)+":"+txt[1]+":"+txt[2])

    