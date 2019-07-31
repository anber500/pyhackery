import sys
import json

from pyhackery.awesomeness.awesome import something_awesome


def jprint(data):
    text = json.dumps(data, indent=3)
    print(text)


def main(args=[]):
    jprint(data=sys.path)
    print(sys.path)
    print(something_awesome())


if __name__ == '__main__':
    main(sys.argv[1:])

# from workspace root run from command line like so
# python -m playground.micahj.scratchpad
