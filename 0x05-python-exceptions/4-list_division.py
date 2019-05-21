#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new = []

    for _ in range(list_length):
        try:
            result = my_list_1[_] / my_list_2[_]
            new.append(result)

        except ValueError:
            result = 0
            new.append(result)
        except ZeroDivisionError:
            result = 0
            new.append(result)
            print("division by 0")
        except TypeError:
            result = 0
            new.append(result)
            print("wrong type")
        except IndexError:
            result = 0
            new.append(result)
            print("out of range")
        finally:
            pass
    return new
