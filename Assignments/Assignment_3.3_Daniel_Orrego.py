Score = raw_input("Enter Score:")
Score = float(Score)

if Score > 1.0:
	print "Invalid Number" 

elif Score >= 0.9:
	print "Grade A"

elif Score >= 0.8:
	print "Grade B"

elif Score >= 0.7:
	print "Grade C"

elif Score >= 0.6:
	print "Grade D"

elif Score < 0.6:
	print "Grade F" 


