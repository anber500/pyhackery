def to_lookup(collection, key_func, selector=lambda i: i):
    """
    Convert a list of items into a lookup where the unique key is a grouping key
    and the values will be the list items that correspond to that unique key

    :param collection: this will be a list
    :param key_func: is a lambda or func that returns a key value from the row
    data in some way eg  use  'field1' from each item => lambda item: item['field1']
    :param selector: the values you want to bring back
    :return: a dict with a grouping key. The value for each key will be
    a list of items matching the key function
    """
    lookup = {}
    for item in collection:
        k = key_func(item)
        if k not in lookup:
            lookup[k] = []
        lookup[k].append(selector(item))
    return lookup
