#!/usr/bin/env python

class Event:
    
    def init(self, eTime = '', sTime = '', eType = '', atm = ''):
        '''
        constructor
        '''
        self.eventTime = []
        self.serviceTime = []
        self.eventType = []
        self.ATMnumber = [1,2,3,4]
        pass

    def __cmp__(self,other):
        '''
        overload compare operator so that position 1 matches in all lists
        '''
        #return cmp(self.eventTime, other.eventTime)
        pass

