#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # mylist = [_ for _ in dir(hidden_4) if not _.startswith('__')]
    # for _ in dir(hidden_4):
    # if not _.startswith('__'):
    # mylist.append(_)

    for string in [_ for _ in dir(hidden_4) if not _.startswith('__')]:
        print("{}".format(string))
