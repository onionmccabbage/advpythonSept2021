
def main():
    # here we create a file access object
    fout = open('out.txt', 'at') # 'at' append text 'wt' (over)write text 'xt' exclusive - fails if exists
    # we can switch the context of our print statement so it output to this file access object
    print('here is some text', file=fout)
    fout.close() # always good to clean up

def my_read():
    fin = open('out.txt', 'rt') # 'rt' read text
    received = fin.read()
    fin.close()
    print(received)

if __name__ == '__main__':
    main() # write some text
    my_read() # read it back!