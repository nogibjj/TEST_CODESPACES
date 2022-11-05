import requests

# r = requests.get("http://localhost:5000/hello")
# print(r.status_code)
# print(r.text)

# r = requests.post(
#     "http://localhost:5000/hdl_check", json={"name": "John", "hdl_value": 33}
# )
# print(r.status_code)
# print(r.text)

# r = requests.post("http://localhost:5000/add", json={"a": 3, "b": 4})
# print(r.status_code)
# print(r.text)

r = requests.post("http://localhost:5000/age",
                  json={'date': "10/10/1999", 'units': "years"})
print(r.status_code)
print(r.text)

# r = requests.post(
#     "http://localhost:5000/new_test",
#     json={"id": 1, "test_name": "hdl", "test_result": 33},
# )
# print(r.status_code)
# print(r.text)

# r = requests.post(
#     "http://localhost:5000/add_test",
#     json={"id": 1, "test_name": "hdl", "test_result": 33},
# )
# print(r.status_code)
# print(r.text)

# r = requests.post("http://localhost:5000/age",json={'date': "10/10/1999", 'units': "years"})
# print(r.status_code)
# print(r.text)

# r=requests.get("http://localhost:5000/time",)
