def append(lst1, lst2):
    """Given two lists, add all the items in the second list to the end of the first list"""
    result = lst1 + lst2
    return result
def concat(lsts):
    """Given a series of lists, combine all items in all lists into one flattened list."""
    result = []
    for lst in lsts:
        for item in lst:
            result.append(item)
    return result
def filter(function, lst):
    """Given a predicate and a lst, return the lst of all items for which predicate(item)
       is True
    """
    result = []
    for item in lst:
        if function(item):
            result.append(item)
    return result
def length(lst):
    """Given a list, return the total number of items within it."""
    count = 0
    for _ in lst:
        count += 1
    return count
def map(function, lst):
    """Given a function and a list, return the list of the result of applying funciton(item) on
       all items.
    """
    result = []
    for item in lst:
        result.append(function(item))
    return result
def foldl(function, lst, initial):
    """Given a function, a list, and initial accumulator, fold (reduce) each item into the
       accumulator from the left using function(accumulator, item)
    """
    result = initial
    for item in lst:
        result = function(result, item)
    return result
def foldr(function, lst, initial):
    """Given a function, a list, and initial accumulator, fold (reduce) each item into the
       accumulator from the left using function(accumulator, item)
    """
    result = initial
    for item in reverse(lst):
        result = function(item, result)
    return result
def reverse(lst):
    """Given a list, return a list with all the original items, but in reversed order."""
    result = []
    for item in lst:
        result.insert(0, item)
    return result