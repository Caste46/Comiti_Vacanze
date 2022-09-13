def flatten(iterable):
    ls=[]
    for item in iterable:
        if isinstance(item, list) == True:
            ls.extend(flatten(item))
        else:
            if item == None:
                continue
            ls.extend([item])
    return ls
