def finder(files, queries):
    cache = {}
    result = []
    for query in queries:
        cache[query] = []
    for fileName in files:
        split = fileName.split('/')
        if split[-1] in cache:
            cache[split[-1]].append(fileName)
    for item in cache.items():
        result += item[1]
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
