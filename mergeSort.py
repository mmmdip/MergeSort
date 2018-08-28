def mergeSort( lst ):
    '''
    sorts the list passed as parameter using traditional merge sort
    parameter:
        lst - list to be sorted (list)
    return:
        sorted list ( list )
    '''
    if len( lst ) == 1:
        return lst
    else:
        half = len( lst ) // 2
        list1 = lst[:half]
        list2 = lst[half:]
        return merge( mergeSort( list1 ), mergeSort( list2 ))

def merge( list1, list2 ):
    '''
    merges two already sorted lists into a new sorted list by comparing values from each
    list
    parameter:
        list1 - list of numbers (list)
        list2 - list of numbers (list)
    return:
        newlst - merged list (list)
    '''
    newlst = []
    while len( list1 ) and len( list2 ):
        element = min( list1[0], list2[0] )
        newlst.append( element )
        if element == list1[0]:
            list1.remove( element )
        else:
            list2.remove( element )
    if len( list1 ):
        newlst.extend( list1 )
    elif len( list2 ):
        newlst.extend( list2 )
    return newlst
