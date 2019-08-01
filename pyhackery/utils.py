def to_lookup(collection, key, selector=lambda i: i):
    """
    Convert a list of items into a lookup where the unique key is a grouping key
    and the values will be the list items that correspond to that unique key

    :param collection: this will be a list
    :param key: key is a lambda like lambda item: item['field1']
    :param selector: the values you want to bring back
    :return: a dict with a grouping key. The value for each key will be
    a list of items matching the key function
    """
    lookup = {}
    for item in collection:
        k = key(item)
        if k not in lookup:
            lookup[k] = []
        lookup[k].append(selector(item))
    return lookup
