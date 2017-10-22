def compound_interest():
    principal = input('Please enter initial deposit: $')
    rate = input('Enter rate of interest: ')
    rate = rate/100
    time = input('Enter duration in years: ')
    time +=1
    compound = input('How many times is the interest compounded yearly: ')

    print "Year %21s" % "Amount on deposit"

    for time in range(1, time):
        formula = principal * (1.0 + rate)** time
        print "%4d%21.2f" % (time,formula)

def start():
    print "Lets start compounding"
    compound_interest()

start()
