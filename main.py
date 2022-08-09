import time
import random
import itertools


# class JSORTING(time,random,itertools):
#     @staticmethod
# ^^the plan is a library that allows you to time sorting algorithms for educational purposes
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


def help():
    print("gen_ran_int => returns random integer array, args => length,range_start,range_end")
    print("bubble => returns bubble sort time, args => list of numbers")
    print("selection => returns selection sort time, args => list of numbers")
    print("insert => returns insertion sort time, args => list of numbers")
    print("merge => returns merge sort time, args => list of numbers")
    print("heap => returns heap sort time, args => list of numbers")
    print("quick => returns quick sort time, args => list of numbers")
    print("BIGO => returns BIGO notation for sorting algorithms, args => string name of sorting algorithm")


def gen_ran_int(length, range1=None, range2=None):
    if range1 is None:
        range1 = 0
    if range2 is None:
        range2 = 2 * length
    array = []
    for i in range(length):
        array.append(random.randint(range1, range2))
    return array


def bubble(args):
    start = time.time()  # starting time
    swap = True  # flag is true to check whether a swap has occured.
    while swap is True:  # loop continues until no swap occurs anymore
        swap = False  # sets the swap to false
        for i in range(len(args) - 1):  # loop repeats over the array
            if args[i] > args[i + 1]:  # checks if current element is greater than the next element
                args[i], args[i + 1] = args[i + 1], args[i]  # swaps them
                swap = True  # swap has occured, so it is true now
        # loop repeats
    print(args)

    # end = time.time() #ending time
    # return end - start #>>time out


def selection(args):
    start = time.time()  # start time
    l = len(args)  # prevent unecessary repeated calculations
    for i in range(l):  # for loop through all elements first, goal => find minimum of subarray
        mindex = i  # sets the minimum index of subarray as the first element
        for j in range(i + 1, l):  # for loop through all elements of subarray i+1 to l to check for minimum
            if args[mindex] > args[j]:
                mindex = j  # reassigns value if new minimum found
        args[i], args[mindex], = args[mindex], args[
            i]  # swaps the minimum of subarray with the first position of subarray
    end = time.time()
    return end - start  # >>time out


def insert(args):
    start = time.time()  # start time
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
    end = time.time()
    return end - start  # >>time out


def merge():
    pass


def heap():
    pass


def quick():
    pass


def permbogo(args):
    # CAUTION USE AT YOUR OWN RISK
    start = time.time()
    for elem in itertools.permutations(args):
        condition = True
        for i in range(len(elem) - 1):
            if elem[i] > elem[i + 1]:
                condition = False
                break
        if condition is True:
            end = time.time()
            return end - start  # >>time out
