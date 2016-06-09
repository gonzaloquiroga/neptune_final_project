#!/usr/bin/env python

InFileName = 'GPCRFinaltable.txt'

InFile = open( InFileName, 'r' )


OutFileName_Rhod = "ClassA2.txt"
OutFileName_Secr = "ClassB2.txt"
OutFileName_Meta = "ClassC2.txt"
OutFileName_Other = "ClassOther2.txt"

OutFileA = open (OutFileName_Rhod, 'w')
OutFileB = open (OutFileName_Secr, 'w')
OutFileC = open (OutFileName_Meta, 'w')
OutFileD = open (OutFileName_Other, 'w')

for Line in InFile:
	
	if 'rhodopsin' in Line or 'Rhodopsin' in Line:
		
		Line = Line + "Class A \n"
		print (Line)
		
		OutFileA.write (Line)

	elif 'Secretin' in Line or 'secretin' in Line:
		
		Line = Line + "Class B  \n"
		print (Line)

		OutFileB.write (Line)

	elif 'Metabotropic' in Line or 'metabotropic' in Line:
		
		Line = Line + "Class C \n"
		print (Line)

		OutFileC.write (Line)

	elif 'Metabotropic' not in Line and 'rhodopsin' not in Line and 'Secretin' not in Line and 'metabotropic' not in Line and 'secretin' not in Line and 'Rhodopsin' not in Line: 

		Line = Line + "Class Other \n"
		print (Line)

		OutFileD.write (Line)

InFile.close()