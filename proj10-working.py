#!/usr/bin/env python

import sys
from event import Event
from eventList import EventList

#global debug var to help us seperate debug output
debug = True

ev = EventList()
e = Event

def readFile(filename):
    contents = ''
    fileList = []
    try:
        with open(filename) as openFile:
            contents = openFile.readline()
            while contents != '':
                contents.replace("\n"," ")
                contents = contents.strip()
                ev.insert(contents.split(" "))
                contents = openFile.readline()
        return fileList
    except:
        print('File could not be read. Please try again.')
        exit()

def main():
    
    # read in our file
    readFile('arrivals2.txt')
    
    # put the events into the event list
    if debug == True:
        print(ev.eventList)
    
    # then sort the list
    ev.eventList.sort(key=lambda x: float(x[0]))
    
    if debug == True:
        print(ev.eventList)
    
    # while event list is not empty    
    while ev.eventList:
        exit()
        # pop the next event off the event list
        # wallClockTime = the time of the event
        # if event type == ‘A’: # person arrives at the line
            # if the line is empty and an ATM is available:
                # send the person to an available ATM machine which means: create a new ‘D’event with an event time calculated from the wallClockTime plus the person’s service time
                # add this new ‘D’ event to the event list
            # else: # put the person in line because there is nowhere else to go
                # add the person to the back of the line
        # else: # event is type == ‘D’ someone is leaving an ATM machine
            # if the line is empty:
                # register the ATM machine as empty and available
            # else: # there are people in line and this ATM just became available
                # get the ATM number from the ‘D’ event information
                # pop the person (event) from the line
                # send the person to the available ATM machine which means: create a new ‘D’ event with an
                # event time calculated from the wallClockTime plus the person’s service time
                # add this new ‘D’ event to the event list
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
    main();
