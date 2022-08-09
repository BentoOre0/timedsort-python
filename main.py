import time
import random
import itertools
import functools

# class JSORTING(time,random,itertools):
#     @staticmethod
# ^^the plan is a library that allows you to time sorting algorithms for educational purposes
def help():
    print("This library also inherits from the following built in libraries:")
    print("----time")
    print("----random")
    print("----itertools")
    print("----functools")
    print("Generation:")
    print("----gen_ran_int => returns list with random integers, can be stored in variable or directly placed as an argument")
    print("----arguments are formatted in the following => length,range_start,range_end\n----standard python ranges apply (i.e) not inclusive of ending range value")
    print("SORTING ALGORITHMS:")
    print("1) each of the following functions print the time taken\n2) arguments should be list type\n3) kwargs display is used when one wants to see the actual sorted list")
    print("----bubble => bubble sort")
    print("----selection => selection sort")
    print("----insert => insertion sort")
    print("----merge => merge sort")
    print("----heap => heap sort")
    print("----quick => quick sort")
    print("Efficiencies:")
    print("----BIGO => prints BIGO notation for sorting algorithms, args => string name of sorting algorithm")
    print("Others:")
    print("----timer => do not touch!, this is a decorator used to time code")
    print("----permbogo => hmmm what is this? use at your own risk...")
    print("----speed => just shows how much faster builtins are")
    print("Developer: Jeremy Yu")
    print("Conceptual help from: Vince Tiu, Geek for Geeks, Stack Overflow")
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"time was: {end-start} seconds")
        return result
    return wrapper

def BIGO(args):
    args = args.lower()
    match args:
        case "bubble":
            print("\nbubble sort:")
            print("BEST: O(n)")
            print("AVE: O(n^2)")
            print("WORST: O(n)")
        case "insert":
            print("\ninsertion sort:")
            print("BEST: O(n)")
            print("AVE: O(n^2)")
            print("WORST: O(n)")
        case "selection":
            print("\nselection sort:")
            print("BEST: O(n)")
            print("AVE: O(n^2)")
            print("WORST: O(n)")
        case "merge":
            print("\nmerge sort:")
            print("BEST: O(n log(n))")
            print("AVE: O(n log(n))")
            print("WORST: O(n log(n))")
        case "heap":
            print("\nheap sort:")
            print("BEST: O(n log(n))")
            print("AVE: O(n log(n))")
            print("WORST: O(n log(n))")
        case "quick":
            print("\nquick sort:")
            print("BEST: O(n log(n))")
            print("AVE: O(n log(n))")
            print("WORST: O(n^2)")
        case _:
            print("ERROR sorting method not found")

def gen_ran_int(length, range1=None, range2=None,display = False):
    if range1 is None:
        range1 = 0
    if range2 is None:
        range2 = 2 * length
    array = []
    for i in range(length):
        array.append(random.randint(range1, range2))
    if display is True:
        print(array)
    else:
        return array

@timer
def bubble(args,display = False):
    if display is True:
        print(args)
    swap = True  # flag is true to check whether a swap has occured.
    while swap is True:  # loop continues until no swap occurs anymore
        swap = False  # sets the swap to false
        for i in range(len(args) - 1):  # loop repeats over the array
            if args[i] > args[i + 1]:  # checks if current element is greater than the next element
                args[i], args[i + 1] = args[i + 1], args[i]  # swaps them
                swap = True  # swap has occured, so it is true now
        # loop repeats
    if display is True:
        print(args)
@timer
def selection(args,display = False):
    if display is True:
        print(args)
    l = len(args)  # prevent unecessary repeated calculations
    for i in range(l):  # for loop through all elements first, goal => find minimum of subarray
        mindex = i  # sets the minimum index of subarray as the first element
        for j in range(i + 1, l):  # for loop through all elements of subarray i+1 to l to check for minimum
            if args[mindex] > args[j]:
                mindex = j  # reassigns value if new minimum found
        args[i], args[mindex], = args[mindex], args[
            i]  # swaps the minimum of subarray with the first position of subarray
    if display is True:
        print(args)

@timer
def insert(args,display=False):
    if display is True:
        print(args)
    for i in range(1, len(args)):  # we are going to compare a current element with the element before it
        hole = args[
            i]  # the hole is the value that is taken out from the array to allow all the other elements to shift
        # right once. However, we dont actually delete the hole, it is just an arbitrary variable saved for future reference
        j = i  # inside the while loop we want to iterate indefinitely
        while hole < args[j - 1] and j > 0:  # this is repeated until the hole finds its spot in the array.
            # the second conditionn is used to prevent negative indexes from messing with the algorithm
            args[j] = args[j - 1]  # shift elements greater than hole 1 to the right
            j -= 1
        args[j] = hole  # hole finds its spot and is inserted
    if display is True:
        print(args)

def merge():
    pass


def heap():
    pass


def quick():
    pass
@timer
def permbogo(args,display=False):
    # CAUTION USE AT YOUR OWN RISK
    for elem in itertools.permutations(args):
        condition = True
        for i in range(len(elem) - 1):
            if elem[i] > elem[i + 1]:
                condition = False
                break
        if condition is True:
            if display is True:
                print(elem)
            return None
@timer
def speed(args,display=False):
    args.sort()
    if display is True:
        print(args)

help()