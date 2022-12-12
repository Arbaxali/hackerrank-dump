# matrix = [[0, 1, 2],
#           [3, 4, 5],
#           [6, 7, 8],
#           [9, 10, 11]]




# lst = []

# lst1 = sum(matrix, [])

# print(lst1)


dictA  = {"a" : 1,
        "b" : 2,
        "c" : {
            "d":3,
            "e":4
        },
        "f" : 5

}



def dict_flatten(in_dict, dict_out=None, parent_key=None, separator="_"):
    if dict_out is None:
      dict_out = {}

    for k, v in in_dict.items():
      k = f"{parent_key}{separator}{k}" if parent_key else k
      if isinstance(v, dict):
         dict_flatten(in_dict=v, dict_out=dict_out, parent_key=k)
         continue

      dict_out[k] = v

    return dict_out

final_dict = dict_flatten(dictA)
print(final_dict)


