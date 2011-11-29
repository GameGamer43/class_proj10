#!/usr/bin/env python

class Event:
    
    def __init__(self):
        # worthless
        pass

    def Event(eTime = '', sTime = '', eType = '', atm = ''):
        return [eTime,sTime,eType,atm]
    
    def __cmp__(self,other):
        '''
        overload compare operator so that position 1 matches in all lists
        '''
        #return cmp(self.eventTime, other.eventTime)
        pass

