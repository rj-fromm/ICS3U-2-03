#!user/bin/env python3

#Created by: RJ Fromm
#Created on: September 2019
#This program calculates circumference of circle

import constants

def main():
    
    radius = int(input("enter radius of circle (mm): "))

    circumference = constants.TAU * radius

    print("")
    print("Circumference is {}mm2".format(circumference))

if __name__ == "__main__":
    main()