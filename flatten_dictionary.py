Input = {'a': {'b': 'c'}, 'd': 'f', 'g': {'h': {'i': 'j'}}}
Input2 = {'a':{ 'b': {'c': {'d': {'e': 'f'}}}}, 'aa': 'zz'}


def get_flatten(Input):
    inner_most = {}
    for k, v in Input.items():
        if type(v) == str:
            p = {k:v}
            inner_most.update(p)
        else:
            for item in v:
                if type(v[item]) == dict:
                    op = v[item]
                    inner_most.update(get_flatten(op))
                else:
                    inner_most.update(v)
    return inner_most


print(get_flatten(Input2))