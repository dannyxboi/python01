Hrs = raw_input('Enter Hours:')
Pay = raw_input('Enter Pay:')
Hrs = float(Hrs)
Pay = float(Pay)

if  (Hrs) <= 40 :
	Total = Hrs * Pay

else:
	Total = (((Hrs - 40) * 1.5) * Pay) + (40 * Pay)


print "I owe you", Total


