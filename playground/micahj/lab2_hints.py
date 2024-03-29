import logging
import json

# setup v basic logging
logging.basicConfig(level=logging.DEBUG)
logging.info("Why hello Dolly")


def jprint(data, title="", pretty=True):
    if title:
        logging.info(title)
    print(json.dumps(data, indent=3 if pretty else None))
    print()


def dict_samples():
    # i am a dictionary
    d1 = {"key1": "value1"}

    # i am also a dictionary
    d2 = dict(key2="value2", key3="value3")

    # you can merge a dict with another dict at the top level with update()
    d1.update(d2)
    d1.update({"key4": 'value4'})
    jprint(d1, "d1 updated from d2 and the line above")

    # this will make a list of pairs
    keys = ("a", "b", "c")
    vals = (1, 2, 3)
    pairs_list = list(zip(keys, vals))  # check out what zip does
    jprint(data=pairs_list, title="pairs_list", pretty=False)

    # or make a dict using zip
    pairs_dict = dict(zip(keys, vals))
    jprint(pairs_dict, "pairs_dict")

    # deep clone a dict
    from copy import deepcopy
    d3 = {"a": {"a1": "v1", "a2": {"b1": "v3"}}}
    d4 = deepcopy(d3)
    jprint(d3, "the original")
    jprint(d4, "the deep copy")


def unpack_a_dict_as_list_of_key_value_pairs():
    d1 = {
        "a": 1,
        "b": 2,
        "c": 3
    }

    # d1.items() is a list of key value pairs
    # d1.keys() is just the keys
    # d1.values() is just the values

    # unpacking
    for key, val in d1.items():
        print(key, val)


def main():
    dict_samples()


if __name__ == '__main__':
    main()

# python -m platform
# from project root try this
# python -m playground.micahj.lab2_hints


# heres one for later
"""
https://realpython.com/flask-google-login/
"""
