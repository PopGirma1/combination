'''

SUBMITTED BY:         ID NO                 Sec
GIRMAY TADESE        ATR/8714/09            2 
KALEAB TAYE          ATR/2066/09            2
KALEAB AMARE         ATR/0078/09	    2
MAHLET WORKNEH	     ATR/1321/09	    2



# NB!  OUR GIVEN SUBSET IS THE FIRST GENERATED LIST FROM OUR MAIN LIST 

#  methode one selection

def Combination( mylist, length ):
    OURTEAM = str( ['mylist[i' + str( i ) + ']' for i in range( length )] ).replace( "'", '' ) \
                     + 'for i0 in range(len( mylist) )'
    if length > 1:
        OURTEAM += str( [' for i' + str( i ) + ' in range( i' + str( i - 1 ) + ', len( mylist ) )' for i in range( 1, length )] )\
            .replace( "', '", ' ' )\
            .replace( "['", '' )\
            .replace( "']", '' )

    OURTEAM = '[' + OURTEAM + ']'
    OURTEAM= eval( OURTEAM )

    return OURTEAM

length=eval(input(" HOW MANY NUMBERS DO YOU WANT TO SELECT ?   "))
k=input(" ENTER YOUR SET FROM WICH YOU WANT TO SELECT THEM .  ")

mylist = list(k)
OURTEAM = Combination( mylist, length )



'''






#   methode   two  selection
# NB!  OUR GIVEN SUBSET IS THE FIRST GENERATED LIST FROM OUR MAIN LIST 

# r means the number of things that we want to select from our given list 

def combination(r,domain,ourlist):
    if len(ourlist)==r:
        yield tuple(ourlist)
    elif len(domain)==0:
        pass
    else:
        for k in combination (r, domain[1:],ourlist[:] +[domain[0]]):
            yield k
        for k in combination(r,domain[1:],ourlist[:]):
            yield k 
        
r=eval(input("  HOW MANY NUMBERS DO YOU WANT TO SELECT ?   "))
n=input("  ENTER YOUR SET FROM WICH YOU WANT TO SELECT THEM . ")
count=0
selectedItems=[k for k in  combination(r, list(n),[])]
m=[]
c=0
for count in selectedItems:
    c=c+1
    m.append(selectedItems)
print (selectedItems)
print("THERE ARE  ",  c  ," NUMBER OF WAYS TO SELECT "  ,  r   ,  " THINGS FROM THEM !!!  "      )




















