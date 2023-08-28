
def tile(di,tile, st):
    res= 0
    inx = []
    for i in st:
        if i not in tile  :
            return -1
        else:
            res+= di[i]
            inx.append(tile.index(i))
    return res,inx

st= "cat"
tiles="tmcbasdk"
di =dict()

for i in range(26):
    di[chr(97+i)]= i


print(tile(di,tiles,st))