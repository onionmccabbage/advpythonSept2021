import sys # sys is in control of inputs and outputs

class Redirect: # brackets are optional
    '''
    Provide an easy way to redirect the standard output
    (which defaults to printing to the console)
    '''
    def __init__(self, new_stdout):
        self.new_stdout = new_stdout
    # override the (default) enter and exit lifecycle methods
    def __enter__(self):
        '''implement a redirect for output'''
        #store the courrent stdout
        self.save_stdout = sys.stdout
        # set a new std out
        sys.stdout = self.new_stdout
    def __exit__(self, exc_type, exc_value, exc_traceback):
        '''restore the original output'''
        sys.stdout = self.save_stdout

if __name__ == '__main__':
    print('Currently stdout is {}'.format(sys.stdout))
    # make use of our redirection class
    # NB the 'with' operator will automatically close any file acces object
    with open('mylog.txt', 'a') as fobj: # open a file access object
        with Redirect(fobj): # pass our file access object as a parameter
            print('this gets redirected to our log file') # look - no file 
    print('this will print to the console') # return to original stdout