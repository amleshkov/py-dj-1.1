import os


def walkdir(dirname: str) -> list[str]:
    tree = []
    for cur, _dirs, files in os.walk(dirname):
        pref = ''
        head, tail = os.path.split(cur)
        while head:
            pref += '...'
            head, _tail = os.path.split(head)
        print(pref+tail)
        for file in files:
            tree.append(pref+file)
    return tree