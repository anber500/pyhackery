def to_lookup(collection, key, selector=lambda i: i):
    lookup = {}
    for item in collection:
        k = key(item)
        if k not in lookup:
            lookup[k] = []
        lookup[k].append(selector(item))
    return lookup
