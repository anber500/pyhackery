from pyhackery.utils import to_lookup

with open("lorum.txt") as fp:
    text = fp.read()

text = text.replace("\n", "").replace(".", "").replace(",", '')
words = [word.strip() for word in text.split(" ")]

print(text)
print(words)

lookup = to_lookup(
    collection=words,
    key_func=lambda word: word.lower(),
    selector=lambda word: word)

print(lookup)
result = [(len(v), k) for k, v in lookup.items()]
for item in reversed(sorted(result[:10])):
    print(item)
