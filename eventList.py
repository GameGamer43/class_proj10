#!/usr/bin/env python


class EventList:
    
    def __init__(self):
        '''
        constructor
        '''
        #list of events
        self.__eList = []

    def insert(self, event):
        '''
        insert an event into the EventList
        '''
        self.__eList.append(event)

    def pop(self, position = 0):
        '''
        method to pop an Event from the EventList and return the event.
        '''
        return self.__eList.pop(position)

    def empty(self):
        '''
        return true if EventList is empty
        '''
        if len(self.__eList) == 0:  
            return True
        else:
            return False

    def __str__(self):
        """Represent the whole list as a string for printing -- very useful
           during code development"""
        s = ""
        for index, card in enumerate(self.__eList):
            # insert newline: print 13 cards per line
            if index%13 == 0:
                s += "\n"
            s += str(card) + " "
        return s
