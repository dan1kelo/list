def app():
    massiv=[]
    dlina=int(input("Enter len> "))
    i=0
    while i<dlina:
        txt1= ("Enter num " + str(i+1) + "> ")
        numbers= int(input(txt1))
        i+=1
        massiv.append(numbers)
    return massiv
massiv= app()
massiv2= app()
print ("1st", massiv, "\n2nd", massiv2 )
compare= input("Compare? Y/N> ")
c= compare.lower()

if c == "y":
    min1=min(massiv)
    min2=min(massiv2)
    if min1<min2:
        print (min1, "massiv1 win")
    else:
        print("No, lose")
else:
    print("Okay")