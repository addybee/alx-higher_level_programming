#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''
    search_replace -  replaces all occurrences of an element by another in a
    new list.
    @my_list: is the initial list
    @search: is the element to replace in the list
    @replace: is the new element
    '''
    return list(map(lambda x: replace if x == search else x, my_list))
