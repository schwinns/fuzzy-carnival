# This is some code

def myFunc(stuff):
    '''
    Function to do something to stuff
    
    Parameters
    ----------
    stuff : str
        The stuff to which we want to do something
        
    Returns
    -------
    new_stuff : str
        The stuff after we have done something to it

    '''

    print(f'Here is the stuff: {stuff}')
    new_stuff = stuff.upper()
    print(f'We did something to it! Here is the new stuff: {new_stuff}')
    return new_stuff


if __name__ == '__main__':

    good_stuff = myFunc('bad stuff')
    