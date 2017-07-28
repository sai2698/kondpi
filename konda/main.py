from konda import konda
import os
import sys

def main():
    try:
        method()
    except KeyboardInterrupt:
        print ("konda stopped by user.")
        sys.exit(0)

def method():
    print "Hello konda"
    print "*********************"
    print "\n"
    print "bye konda"

if __name__ == '__main__':
    main()

