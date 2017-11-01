import sys

def message(first_name, last_name):
    print('Hello {}. Your last name is {}.'.format(first_name, last_name))


if __name__ == '__main__':
    message(sys.argv[1], sys.argv[2])