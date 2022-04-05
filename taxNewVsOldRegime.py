'''
new regime: no tax reduction				
annual income range				
start	        end	        tax rate in %		0.00    cumulative
0.00	        250,000.00	    0.00	    0.00	    0.00
250,001.00	    500,000.00	    5.00	    25,000.00	25,000.00
500,001.00	    750,000.00	    10.00	    75,000.00	100,000.00
750,001.00	    1,000,000.00	15.00	    150,000.00	250,000.00
1,000,001.00	1,250,000.00	20.00	    250,000.00	500,000.00
1,250,001.00	1,500,000.00	25.00	    375,000.00	875,000.00
1,500,001.00		            30.00   	0.00	    
-------cumulatives are wrong
'''
'''
old regime: no tax reduction				
annual income range				
start	        end	        tax rate in %		0.00    cumulative
0.00	        250,000.00	    0.00    	0.00	    0.00
250,001.00  	500,000.00	    5.00	    25,000.00	25,000.00
500,001.00	    1,000,000.00	20.00	    200,000.00	225,000.00
1,000,001.00				
-------cumulatives are wrong
'''

base_salary = float(input(" Enter Base salary for new regime: "))
#for new regime:
stop_calculating = False
amount = base_salary
tax = [0,0,0,0,0,0,0]
slab = 0


if (amount <=   250000):
    slab = 0
    #tax[0]  = 0
    #print ( slab)


elif (amount <= 500000):
    slab = 1
    #tax[1]  = (amount - 250000) * 0.05 
    #print ( slab)
    

elif (amount <= 750000):
    slab = 2
    #tax[2]  = (amount - 500000) * 0.10
    #print ( slab)

elif (amount <= 1000000):
    slab = 3
    #tax[3]  = (amount - 750000) * 0.15
    #print ( slab)

elif (amount <= 1250000):
    slab = 4
    #tax[4]  = (amount - 1000000) * 0.20
    #print ( slab)

elif (amount <= 1500000):
    slab = 5
    #tax[5]  = (amount - 1250000) * 0.25
    #print ( slab)

elif (amount >= 1500001):
    slab = 6
    #tax[6]  = (amount - 1500000) * 0.30
    #print ( slab)


if (slab == 0):
    tax[0] = 0

elif (slab == 1):
    tax[0] =  250000   * 0
    tax[1]  = (amount - 250000) * 0.05 
    
elif (slab == 2):
    tax[0] =  250000   * 0
    tax[1]  = (250000) * 0.05
    tax[2]  = (amount - 500000) * 0.10
    #tax[3]  = (amount - 750000) * 0.15
    #tax[4]  = (amount - 1000000) * 0.20
    #tax[5]  = (amount - 1250000) * 0.25 
    #tax[6]  = (amount - 1500000) * 0.30

elif (slab == 3):
    tax[0] = 250000   * 0
    tax[1]  = (250000) * 0.05
    tax[2]  = (250000) * 0.10
    tax[3]  = (amount - 750000) * 0.15
    
elif (slab == 4):
    tax[0] = 250000   * 0
    tax[1]  = (250000) * 0.05
    tax[2]  = (250000) * 0.10
    tax[3]  = (250000) * 0.15
    tax[4]  = (amount - 1000000) * 0.20
    
elif (slab == 5):
    tax[0] = 250000   * 0
    tax[1]  = (250000) * 0.05
    tax[2]  = (250000) * 0.10
    tax[3]  = (250000) * 0.15
    tax[4]  = (250000) * 0.20
    tax[5]  = (amount - 1250000) * 0.25 
    
elif (slab == 6):
    tax[0] = 250000   * 0
    tax[1]  = (250000) * 0.05
    tax[2]  = (250000) * 0.10
    tax[3]  = (250000) * 0.15
    tax[4]  = (250000) * 0.20
    tax[5]  = (250000) * 0.25 
    tax[6]  = (amount - 1500000) * 0.30

statement = [
"start	     -   end            tax rate      Tax",
"0.00         -   250,000.00     0.00       :  ",   	    
"250,001.00   -   500,000.00     5.00       :  ",
"500,001.00   -   750,000.00     10.00      :  ",
"750,001.00   -   1,000,000.00   15.00      :  ",
"1,000,001.00 -   1,250,000.00   20.00      :  ",
"1,250,001.00 -   1,500,000.00   25.00      :  ",	   	
"1,500,001.00 -                  30.00      :  ",   	
]

print(statement[0] )
print(statement[1] , tax[0])
print(statement[2] , tax[1])
print(statement[3] , tax[2])
print(statement[4] , tax[3])
print(statement[5] , tax[4])
print(statement[6] , tax[5])
print(statement[7] , tax[6])


#print(tax)
print("slab: ", slab)
print("SUM: ", sum(tax))


#tax[2]  = (amount - 500000) * 0.10
#tax[3]  = (amount - 750000) * 0.15
#tax[4]  = (amount - 1000000) * 0.20
#tax[5]  = (amount - 1250000) * 0.25 
#tax[6]  = (amount - 1500000) * 0.30
    
'''
#slab = 0
tax[0]  = 0

#slab = 1

tax[1]  = (amount - 250000) * 0.05 

#slab = 2
tax[2]  = (amount - 500000) * 0.10

#slab = 3
tax[3]  = (amount - 750000) * 0.15

#slab = 4
tax[4]  = (amount - 1000000) * 0.20

#slab = 5
tax[5]  = (amount - 1250000) * 0.25

#slab = 6
tax[6]  = (amount - 1500000) * 0.30

for i in range(0,6):
    if (tax[i] < 0):
        tax[i] = 0

print(tax)
'''
print("\n \n")

base_salary = float(input(" Enter Base salary for old regime: "))
amount = base_salary
tax = [0,0,0,0,0,0,0]
slab = 0


if (amount <=   250000):
    slab = 0
    #tax[0]  = 0
    #print ( slab)


elif (amount <= 500000):
    slab = 1
    #tax[1]  = (amount - 250000) * 0.05 
    #print ( slab)
    

elif (amount <= 1000000):
    slab = 2
    #tax[2]  = (amount - 500000) * 0.10
    #print ( slab)

elif (amount >= 1000001):
    slab = 3
    #tax[3]  = (amount - 750000) * 0.15
    #print ( slab)


if (slab == 0):
    tax[0] = 0

elif (slab == 1):
    tax[0] =  250000   * 0
    tax[1]  = (amount - 250000) * 0.05 
    
elif (slab == 2):
    tax[0] =  250000   * 0
    tax[1]  = (250000) * 0.05
    tax[2]  = (amount - 500000) * 0.20
    #tax[3]  = (amount - 750000) * 0.15
    #tax[4]  = (amount - 1000000) * 0.20
    #tax[5]  = (amount - 1250000) * 0.25 
    #tax[6]  = (amount - 1500000) * 0.30

elif (slab == 3):
    tax[0] = 250000   * 0
    tax[1]  = (250000) * 0.05
    tax[2]  = (500000) * 0.20
    tax[3]  = (amount - 1000000) * 0.30
    

statement = [
"start        -   end            tax rate      Tax",
"0.00         -   250,000.00     0.00       :  ",   	    
"250,001.00   -   500,000.00     5.00       :  ",
"500,001.00   -   1,000,000.00   20.00      :  ",
"1,000,001.00 -                  30.00      :  "
]

print(statement[0] )
print(statement[1] , tax[0])
print(statement[2] , tax[1])
print(statement[3] , tax[2])
print(statement[4] , tax[3])


#print(tax)
print("slab: ", slab)
print("SUM: ", sum(tax))

# compare 1,150,000 against 962,500.