# Python:   3.6.1
#
# Author:   Jake Clark
#
# Purpose:  Create code that will use the current time of the Portland HQ
#           to find out the time in the NYC & London branches, then compare
#           that time with the branches hours to see if they are open or closed.
#           Each branch is open from 9AM to 9PM.
#
#
#

import arrow



def getTime():
    PDXtime = arrow.now()
    print ('The time in Portland is ',PDXtime.format('HH:mm:ss'))
    LDNtime = arrow.now('+01:00').format('HH:mm:ss')
    print ('The time in London is ', LDNtime)
    NYCtime = arrow.now('-04:00').format('HH:mm:ss')
    print ('The time in New York City is ', NYCtime)
    if '21:00:00' >= LDNtime <= '17:00:00': 
        print ('The London Office is currently closed.')
    else:
        print('The London Office is open!')
    if '21:00:00' >= NYCtime <= '12:00:00':
        print ('The New York City Office is currently closed.')
    else:
        print('The New York City Office is open!')
    


getTime()
