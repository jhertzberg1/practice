filename = 'random_text.txt'

def write_file(filename, string_to_write):
    stream = open(filename, 'w')
    stream.write('some text')
    stream.write(string_to_write)
    stream.close()


def open_file(filename):
    stream = open(filename, 'r')
    for line in stream:
        print line
    stream.close()


def copy_file():
    pass

def hello(name):
    print('hi ' + name)




if __name__ == '__main__':
    open_file(filename)
    write_file(filename, ' adding some more text')





