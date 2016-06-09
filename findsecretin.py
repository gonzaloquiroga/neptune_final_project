#!/usr/bin/env python
import re

InFileName = 'GPCRFinaltable.txt'

InFile = open( InFileName, 'r' )

LineNumber = 0

for Line in InFile:
	
	#print Line
	#Line = Line.strip()

	if 'Secretin' in Line:
		
		Line = Line + " Class B"
		print (Line)

		#return Line

	#LineNumber = LineNumber + 1

	'''

	

	if LineNumber > 0:

		ElementList = Line.split( ';' )
		#print( 'Depth:{} Lat:{} Lon:{}'.format( ElementList[4], ElementList[2], ElementList[3] ) )
		#Domain = ElementList [4]
		#DomainInside = Domain.split ( '\n' )
		#print (ElementList)
		print (ElementList)
	LineNumber = LineNumber + 1
	


'''
'''
"NA
Gene3D G3DSA:1.20.1070.10  26 353 1.3E_58 T 14_10_2015
Pfam PF00001 7 transmembrane receptor (rhodopsin family) 64 328 1.1E_36 T 14_10_2015
PRINTS PR00237 Rhodopsin_like GPCR superfamily signature 82 103 4.7E_31 T 14_10_2015
PRINTS PR00237 Rhodopsin_like GPCR superfamily signature 310 336 4.7E_31 T 14_10_2015
PRINTS PR00237 Rhodopsin_like GPCR superfamily signature 216 239 4.7E_31 T 14_10_2015
PRINTS PR00237 Rhodopsin_like GPCR superfamily signature 268 292 4.7E_31 T 14_10_2015
PRINTS PR00237 Rhodopsin_like GPCR superfamily signature 128 150 4.7E_31 T 14_10_2015
PRINTS PR00237 Rhodopsin_like GPCR superfamily signature 49 73 4.7E_31 T 14_10_2015
PANTHER PTHR24242  1 349 9.1E_60 T 14_10_2015"

'''


InFile.close()