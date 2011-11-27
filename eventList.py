#!/usr/bin/env python


class EventList:
    
    def __init__(self):
        '''
        constructor
        '''
        #list of events
        self.eventList = []

    def insert(self, event):
        '''
        insert an event into the EventList
        >>> e.insert(1)
        ... print(e.eventList)
        [1]
        '''
        self.eventList.append(event)
        return self.eventList

    def pop(self, position = 0):
        '''
        method to pop an Event from the EventList and return the event.
        >>> print(e.pop())
        []
        '''
        self.eventList.pop(position)
        return self.eventList

    def empty(self):
        '''
        return true if EventList is empty
        >>> print(str(e.empty()))
        True
        '''
        if len(self.eventList) == 0:  
            return True
        else:
            return False

    def __str__(self):
        """Represent the whole list as a string for printing -- very useful
           during code development
        """
        s = ""
        for index, value in enumerate(self.eventList):
            # insert newline: print 13 cards per line
            if index%13 == 0:
                s += "\n"
            s += str(value) + " "
        return s

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'e': EventList()})
