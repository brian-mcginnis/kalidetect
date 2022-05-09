#!/usr/bin/python3

"""System module."""
import sys # To work with Arguments
import os # to delete files for cleanliness

import gzip # for unzipping
from heapq import nlargest
import requests # Used to get available Contents information from url

#TO DO:
# add arguments for setting Top n number: default 10| robust url argument,
# add load bar and time, simplify and rewrite OO, check formatting,
# try/except, Better scraping on START variable for more urls

class Arch:
    ''' Class Definition for each object architecture'''
    def __init__(self, name,num_arg, num):
        self.name = name
        self.num_arg = num_arg
        self.num = num

    def download(self, url):
        ''' Checks if requested Architecture gz file exists in directory/ Downloads'''
        arch = "Contents-" + self.name
        archgz = arch + ".gz"
        urldwn = url + archgz

        if os.path.exists(archgz):
            print("Found File (", self.num, "of", self.num_arg,") \'" +archgz+ "\' in Directory")
        else:
            # Downloads the Relevant File
            print("Downloading","File (", self.num, "of", self.num_arg,") from", urldwn)
            req = requests.get(urldwn, allow_redirects=True)
            open(archgz, 'wb').write(req.content)
            req.close()
        urldwn = ""

    def parse(self, obj):
        ''' Contains the way to parse a defined object '''
        print ("Running Analysis on architecture '" + self.name + "'")
        # Initialization
        arch = "Contents-" + self.name
        archgz = arch + ".gz"
        # Reads the package and Adds to a Dictionary, Increments on duplicate file in Package
        print("Reading package files")
        debpkg = {}

        with gzip.open(archgz, 'rb') as file:
            file_content = file.read().decode()
            file_content = file_content.splitlines()

            for element in file_content:
                word =  "".join(element.strip().split()[1])
                if word in debpkg:
                    debpkg[word] = debpkg[word] + 1
                else:
                    debpkg[word] = 1
            file.flush()
            obj[self.num].printstat(debpkg)

    def printstat(self, debpkg):
        ''' Prints out the Ten largest Dictionary Entries '''
        ten_largest = nlargest(10, debpkg, key=debpkg.get)
        j = 1
        print("\nFile Results (", self.num, "of", self.num_arg,"):\n")
        print(f"{'#':>12} {'Package':^50} {'# Files':>16}")
        print(" "*10,"-"*75)
        for val in ten_largest:
            print(f"{j:12}. {val:50} {debpkg.get(val):>16}")
            j += 1
            print (" "*10,"-"*75)

def argcheck(url):
    ''' Argument scraping and valid argument check '''
    start = '<tr><td valign="top"><img src="/icons/compressed.gif" alt="[   ]"></td>'\
        '<td><a href=\"Contents-'
    end = '.gz\"'
    argarr = []
    req = requests.get(url)
    for line in req.text.splitlines():
        if line.startswith(start):
            argarr.append(line[line.find(start)+len(start):line.rfind(end)])
    req.close()

    # Proper argument check
    num_arg = len(sys.argv)

    if num_arg < 2:
        print("! Error: Incorrect Number of Arguments...\n! At least one argument is needed to run")
        print("! Valid arguments are:\n " , argarr, "\n! Exiting")
        print("! Exiting")
        sys.exit()
    else:
        count = 1

        while count <= num_arg-1:
            while sys.argv[count] not in argarr:
                print("! Error: Incorrect Argument \'" + sys.argv[count] +"\'")
                print("! Valid arguments are:\n " , argarr, "\n! Exiting")
                sys.exit()
            count += 1

def fileop(num_arg, url, obj):
    ''' File Operations: Download Object Function pass'''
    k = 1 # Parse Files
    while k <= num_arg:
        obj[k] = Arch(sys.argv[k] , num_arg, k)
        obj[k].download(url)
        k += 1

def process(num_arg, obj):
    ''' Parsing Farm '''
    i = 1
    while i <= num_arg:
        obj[i].parse(obj)
        i += 1

def main():
    ''' Main Function'''

    url = 'https://http.kali.org/kali/dists/kali-dev/main/'
    num_arg = len(sys.argv)-1
    obj = {}

    # Scrape/ Check for valid arguments
    argcheck(url)
    # Check for existance of file / Download
    fileop(num_arg, url, obj)
    # Parse data for packages with the most files and print to the screen
    process(num_arg, obj)
    # End
    print("Program complete\nExiting...")
    sys.exit()

if __name__ == "__main__":
    main()
