customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
# print(customer["Name"]) -> Error
print(customer.get("birthday"))
customer["name"] = "Jack Smith"
print(customer["name"])