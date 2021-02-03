def reversal(w):
    bazinga = w[len(w)-1]

    for i in range(2,len(w)+1):
        bazinga = bazinga + w[len(w)-i]


    return bazinga   

print(reversal("polaroid"))
