filename = 'random_text.txt'
filename2 = 'random_textB.txt'

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


def copy_file(filename2):
    open_file(filename)










def hello(name):
    print('hi ' + name)




if __name__ == '__main__':
    open_file(filename)
    copy_file(filename2)





