# import json

from flatten_json import flatten as flatten
from flatten_json import unflatten


# # Function to flatten JSON
# def flatten_json(y):
#     out = {}

#     def flatten(x, name=''):
#         if type(x) is dict:
#             for a in x:
#                 flatten(x[a], name + a + '_')
#         elif type(x) is list:
#             i = 0
#             for a in x:
#                 flatten(a, name + str(i) + '_')
#                 i += 1
#         else:
#             out[name[:-1]] = x

#     flatten(y)
#     return out


# def dict_to_json(_dict):
#     return json.dumps(_dict)




#########
# flatten_json = flatten # flatten(dictionary=input_dict)
# unflatten_json = unflatten # unflatten(json_dict=json_dict)

def check_hierarchy(data, parent_key=''):
    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            print(f"Checking {new_key}")
            check_hierarchy(value, new_key)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_key = f"{parent_key}[{index}]"
            print(f"Checking {new_key}")
            check_hierarchy(item, new_key)
    else:
        print(f"{parent_key}: {data}")

"""
# Example JSON data
json_data = '''
{
    "name": "John",
    "info": {
        "age": 30,
        "address": {
            "city": "New York",
            "zipcode": "10001"
        }
    },
    "hobbies": ["reading", "travelling"]
}
'''

data = json.loads(json_data)
check_hierarchy(data)
"""