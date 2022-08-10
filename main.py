class TimedSort:
    @staticmethod
    def help_me():
        print("TimedSort is a python library made for educational purposes.")
        print("It poses 6 sorting algorithms that can be timed and compared easily")
        print("\nThis library also uses the other the built in libraries:")
        print("----time")
        print("----random")
        print("----functools")
        print("Generation:")
        print("----gen_ran_int => returns list with random integers.")
        print("-------- Thus, it can be stored in variable or directly placed as an argument")
        print("----arguments are formatted in the following => length,range_start,range_end")
        print("--------Note: standard python ranges apply (i.e RANGES DO NOT GO TO THE LAST VALUE)")
        print("SORTING ALGORITHMS:")
        print("--1) each of the following functions print the time taken")
        print("--2) arguments should be list type")
        print("--3) the kwarg display is used when one wants to see the actual sorted list BEFORE AND AFTER sorting")
        print("----bubble => bubble sort")
        print("----selection => selection sort")
        print("----insertion => insertion sort")
        print("----merge => merge sort")
        print("----heap => heap sort")
        print("----quick => quick sort")
        print("Efficiencies:")
        print("----BIGO => prints BIGO notation for sorting algorithms, args => string name of sorting algorithm")
        print("Others:")
        print("----timer => do not touch!, this is a decorator used to time code")
        print("----permbogo => hmmm what is this? use at your own risk...")
        print("----miracle => hmmm what is this? use at your own risk...")
        print("----builtin => just shows how much faster builtins are")
        print("Developer: Jeremy Yu")
        print("Conceptual help from: Vince Tiu, Geek for Geeks, Stack Overflow, mycodeschool - Youtube")

    @staticmethod
    def timer(func):
        from time import perf_counter
        from functools import wraps

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = perf_counter()
            result = func(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start
            print(f"{func.__name__} sort time was: {elapsed} seconds")
            print()
            return result

        return wrapper

    @staticmethod
    def BIGO(args):
        args = args.lower()
        BIG_O_dictionary = {"bubble": ["bubble sort:", "BEST: O(n)", "AVE: O(n^2)", "WORST: O(n)"],
                            "insert": ['insertion sort:', 'BEST: O(n)', 'AVE: O(n^2)', 'WORST: O(n)'],
                            "selection": ['selection sort:', 'BEST: O(n)', 'AVE: O(n^2)', 'WORST: O(n)'],
                            "merge": ['merge sort:', 'BEST: O(n log(n))', 'AVE: O(n log(n))', 'WORST: O(n log(n))'],
                            "heap": ['heap sort:', 'BEST: O(n log(n))', 'AVE: O(n log(n))', 'WORST: O(n log(n))'],
                            "quick": ['quick sort:', 'BEST: O(n log(n))', 'AVE: O(n log(n))', 'WORST: O(n^2)']}
        try:
            print(*BIG_O_dictionary[args], sep='\n')
        except KeyError:
            print("ERROR sorting method not found")

    @staticmethod
    def gen_ran_int(length, range1=None, range2=None, display=False):
        from random import randint
        if range1 is None:
            range1 = 0
        if range2 is None:
            range2 = 2 * length
        array = []
        for i in range(length):
            array.append(randint(range1, range2))
        if display is True:
            print(array)
        else:
            return array

    @staticmethod
    @timer
    def bubble(array, clone=True, display=False):
        if clone is True:
            args = array.copy()  # we create a copy of the array, allows us to reuse array
        else:
            args = array  # this will change the actual list
        if display is True:
            print(array)
        swap = True
        while swap is True:
            swap = False
            for i in range(len(args) - 1):  # loop repeats over the array
                if args[i] > args[i + 1]:  # checks if current which if next is bigger
                    args[i], args[i + 1] = args[i + 1], args[i]  # swaps them
                    swap = True  # swap has occurred
            # loop repeats
        if display is True:
            print(args)

    @staticmethod
    @timer
    def selection(array, clone=True, display=False):
        if clone is True:
            args = array.copy()
        else:
            args = array
        if display is True:
            print(array)
        length = len(args)  # prevent unnecessary repeated calculations
        for i in range(length):  # for loop through all elements to  find min of subarray
            mindex = i  # sets minimum index of subarray as the first element
            for j in range(i + 1, length):
                if args[mindex] > args[j]:
                    mindex = j  # reassigns value if new minimum found
            args[i], args[mindex], = args[mindex], args[
                i]  # swaps the minimum of subarray with the first position of subarray
        if display is True:
            print(args)

    @staticmethod
    @timer
    def insertion(array, clone=True, display=False):
        if clone is True:
            args = array.copy()
        else:
            args = array
        if display is True:
            print(array)
        for i in range(1, len(args)):  # going to compare a current element with element before it
            hole = args[i]  # hole is value taken out from the array to allow all the other elements to shift
            # don't actually delete the hole
            j = i  # we want to iterate indefinitely
            while hole < args[j - 1] and j > 0:  # repeated until the hole finds its spot in array.
                # second condition is used to prevent negative indexes
                args[j] = args[j - 1]  # shift elements greater than hole 1 to the right
                j -= 1
            args[j] = hole  # hole finds its spot and is inserted
        if display is True:
            print(args)

    @staticmethod
    @timer
    def merge(array, clone=True, display=False):
        if clone is True:
            args = array.copy()
        else:
            args = array
        if display is True:
            print(array)
            return TimedSort._merge(args, display=True)
        return TimedSort._merge(args, display=False)

    @staticmethod
    def _merge(args,
               display=False):  # to prevent repeated calling of decorator, credit to stack overflow
        # (https://stackoverflow.com/questions/70069317/python-decorating-recursive-function)
        length = len(args)
        if length > 1:
            mid = length // 2  # integer division as indexes can only be integers
            left = args[:mid]
            right = args[mid:]
            TimedSort._merge(left)
            TimedSort._merge(right)
            # assume left and right arrays are already sorted
            L = len(left)
            R = len(right)
            minL = 0  # minimum of left subarray
            minR = 0  # minimum of right subarray
            mainarr = 0  # index of main array before any splitting or merging
            while minL < L and minR < R:
                if left[minL] <= right[minR]:  # checks which is smaller minimum between subarrays
                    args[mainarr] = left[minL]  # the current position in main array is set to the minimum
                    minL += 1  # next unpicked position in left array
                else:
                    args[mainarr] = right[minR]  # the current position in main array is set to the minimum
                    minR += 1  # next unpicked position in right array
                mainarr += 1
            # in some cases, 1 subarray may be exhausted first. So we need to check if there are any left
            while minL < L:  # check left remaining
                args[mainarr] = left[minL]
                minL += 1
                mainarr += 1
            while minR < R:  # check right remaining
                args[mainarr] = right[minR]
                minR += 1
                mainarr += 1
        if display is True:
            print(args)

    @staticmethod
    def heap():
        pass

    @staticmethod
    def quick():
        pass

    @staticmethod
    @timer
    def permbogo(array, clone=True, display=False):
        if clone is True:
            args = array.copy()
        else:
            args = array
        if display is True:
            print(array)
        from itertools import permutations
        # CAUTION USE AT YOUR OWN RISK
        for elem in permutations(args):
            condition = True
            for i in range(len(elem) - 1):
                if elem[i] > elem[i + 1]:
                    condition = False
                    break
            if condition is True:
                if display is True:
                    print(elem)
                return None

    @staticmethod
    @timer
    def builtin(array, clone=True, display=False):
        if clone is True:
            args = array.copy()
        else:
            args = array
        if display is True:
            print(array)
        args.sort()
        if display is True:
            print(args)

    @staticmethod
    @timer
    def miracle(array, clone=True, display=False):
        if clone is True:
            args = array.copy()
        else:
            args = array
        issorted = False
        while issorted is False:
            issorted = True
            for i in range(1, len(args)):
                if args[i] < args[i - 1]:
                    issorted = False
                    break