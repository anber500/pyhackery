import csv


def read_a_simple_csv(path, delimiter=','):
    with (open(path)) as f:
        # read the first row - we expect it to be the header row
        header = f.readline()  # nb: this advances the reader by 1 line

        # replace spaces in the headers with underscores
        # (makes for better dict keys - you also might want lowercase)
        fieldnames = [
            c.strip().replace(' ', '_') for c in
            header.strip().split(delimiter)
        ]
        # get a csv reader for the rest of the file eg f[1:]
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=delimiter)

    # each item in the reader is an OrderedDict - i prefer to use just a
    # normal Dict for json purposes
    return [dict(row) for row in reader]
