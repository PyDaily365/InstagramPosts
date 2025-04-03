def list_vs_tuple():
    my_list = [1,2,3] # Lists are mutable
    my_tuple = (1,2,3) # Tuples are immutable
    my_list[0] = 10
    print("list:", my_list)
    try:
        my_tuple[0] = 10
    except TypeError:
        print("Tuple error: Can't modify!")
    print("Tuple:", my_tuple)
list_vs_tuple()
#Learn: lists vs tuples(mutable vs immutable)