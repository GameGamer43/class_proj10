#!/usr/bin/env python

import sys
from event import Event
from eventList import EventList

#global debug var to help us seperate debug output
debug = True

ev = EventList()

def readFile(filename):
    contents = ''
    fileList = []
    try:
        with open(filename) as openFile:
            contents = openFile.readline()
            while contents != '':
                contents.replace("\n"," ")
                contents = contents.strip()
                contents = contents.split(" ")
                contents = Event.Event(contents[0],contents[1],'A','0')
                ev.insert(contents)
                contents = openFile.readline()
        return True
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print('File could not be read, Please try again.')
        exit()
        
def main():
    # read in our file
    readFile('arrivals2.txt')

    ev.sort()
    
    waitingList = []
    atmList = [1,2,3,4]
    
    # while event list is not empty
    while ev.eventList:
        # pop the next event off the event list
        currentEvent = ev.eventList.pop()

        if debug == True:
            print('Event:',currentEvent,'Time:',currentEvent[0],'Duration:',
                    currentEvent[1])

        # wallClockTime = the time of the event
        wallClockTime = currentEvent[0]

        #person arrives at the line
        if currentEvent[2] == 'A':
            # if the line is empty and an ATM is available:
            if not waitingList and atmList:
                # send the person to an available ATM machine which means:
                #create a new ‘D’event with an event time calculated from the   
                #wallClockTime plus the person’s service time 
                currentATM = atmList.pop()
               
                # add this new 'D' event to the event list 
                ev.insert([int(currentEvent[0]) + int(currentEvent[1]), '0','D',currentATM])
            # else: # put the person in line because there is nowhere else
            else:
                # add the person to the back of the line
                ev.insert(currentEvent)
        # else: # event is type == ‘D’ someone is leaving an ATM machine
        elif currentEvent[2] == 'D':
            #if the line is empty:
            if not waitingList:
                pass
                # register the ATM machine as empty and available
            # else: # there are people in line and this ATM just became available
            else:
                pass
                # get the ATM number from the ‘D’ event information
                # pop the person (event) from the line
                # send the person to the available ATM machine which means: create a new ‘D’ event with an
                # event time calculated from the wallClockTime plus the person’s service time
                # add this new ‘D’ event to the event listi
        ev.sort()
        # print the event, the line and ATM’s in use

def output():
    '''
    After each event:
        • Output the event that happened. For each event output the eventTime, the serviceTime, and the event Type.
        • Output the line of people waiting for ATMs: since we are recording each “person” as an
Event, this will be a list of events in line for ATMs. For each event in line, output its arrival time and its service time.
        • Output each ATM: output the ATM number (1,2,3, or 4) and the service time
    At the end of the program run:
        • Output the average time spent by people in each line.
    '''
    pass

if __name__ == '__main__':
    main()
