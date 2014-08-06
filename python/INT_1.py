
import sys

events = []

def add_event():
    hour = -1
    while hour == -1:
        ri = raw_input('Please enter the hour: ')
        try:
            hour = int(ri)
        except:
            print 'Not a valid integer'
    desc = raw_input('Please enter event description: ')
    global events
    events.append([hour, desc])

def print_events():
    global events
    events.sort()
    for e in events:
        print "%02d: %s" % (e[0], e[1])

def delete_event():
    events.pop(get_index("delete"))

def edit_event():
    global events
    i = get_index("edit")
    new_hour = -1
    while new_hour == -1:
        ri = raw_input("Please enter new hour: ")
        try:
            new_hour = int(ri)
        except:
            print "Please enter valid integer"
    events[i][0] = new_hour
    ri = raw_input("Please enter new event description: ")
    events[i][1] = ri

def get_index(action):
    valid_index = -1
    global events
    events.sort()
    for i, e in enumerate(events):
        print "[%03d] %02d: %s" % (i+1, e[0], e[1])
    while valid_index == -1:
        ri = raw_input("Please enter index of event to %s: " % (action,))
        try:
            valid_index = int(ri)
        except:
            print "Please enter a valid integer"
        # test to see if it's in the range
        if valid_index <= 0 or valid_index > len(events):
            print "Please enter a number in a valid range"
            valid_index = -1
    # prints and takes in user friendly index (counting from 1) returns real
    # index (counting from 0)
    return valid_index-1

if __name__ == '__main__':
    while True:
        ri = raw_input('(a)dd, (d)elete, (e)dit, (p)rint, (q)uit: ')
        cmd = ri[0].lower();
        if (cmd == "a"):
            add_event()
        elif (cmd == "d"):
            delete_event()
        elif (cmd == "e"):
            edit_event()
        elif (cmd == "p"):
            print_events()
        elif (cmd == "q"):
            sys.exit()
