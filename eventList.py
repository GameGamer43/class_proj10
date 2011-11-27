#!/usr/bin/env python


class EventList:
    
    def __init__(self):
        '''
        constructor
        '''
        #list of events
        self.eList = []

    def insert(self, event = ''):
        '''
        insert an event into the EventList
        '''
        print(self)
        pass

    def pop(self, position = 0):
        '''
        method to pop an Event from the EventList and return the event.
        '''
        pass

    
    def empty(self):
        '''
        return true if EventList is empty
        '''
        if self.eList:
            return True
        else:
            return False
