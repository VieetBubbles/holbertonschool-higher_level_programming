#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    mylist = []
    for _ in dir(hidden_4):
        if not _.startswith('__'):
            mylist.append(_)

    for string in mylist:
        print("{}".format(string))
