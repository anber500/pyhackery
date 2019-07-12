import sys
from awesomeness.awesome import something_awesome


def lets_go():
    print(something_awesome())


def main(args=[]):
    lets_go()


if __name__ == '__main__':
    main(sys.argv[1:])