"""
Alisha Pegan's Pickle Toolbox
A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
import pickle


def update_counter(file_name, reset=False):
    """ Updates a counter stored in the file 'file_name'

    A new counter will be created and initialized to 1 if none exists or if
    the reset flag is True.

    If the counter already exists and reset is False, the counter's value will
    be incremented.

    file_name: the file that stores the counter to be incremented.  If the file
    doesn't exist, a counter is created and initialized to 1.
    reset: True if the counter in the file should be rest.
    returns: the new counter value

    >>> update_counter('blah.txt',True)
    1
    >>> update_counter('blah.txt')
    2
    >>> update_counter('blah2.txt',True)
    1
    >>> update_counter('blah.txt')
    3
    >>> update_counter('blah2.txt')
    2
    """
    counter = 0
    if exists(file_name) is True and reset is True:
        f = open(file_name, 'wb')
        counter = 1
        pickle.dump(counter, f)
        f.close()
        return counter
    elif exists(file_name) is True and reset is False:
        filer = open(file_name, 'rb+')
        counter = pickle.load(filer) + 1
        filer.close()
        f = open(file_name, 'wb')
        pickle.dump(counter, f)
        f.close()
        return counter
    elif exists(file_name) is False:
        f = open(file_name, 'wb')
        counter = 1
        pickle.dump(counter, f)
        f.close()
        return counter


if __name__ == '__main__':
    if len(sys.argv) < 2:
        import doctest
        doctest.testmod()
    else:
        print("new value is " + str(update_counter(sys.argv[1])))
