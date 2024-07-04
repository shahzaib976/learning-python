user = {
    'id' : '1',
    'full_name' : 'John Alas',
    'age' : 18
}

is_adult = 'Adult' if user['age'] >= 18 else 'Underage'

name = 'Smith'
age = 29

# formatted string literals.

print(f"My Name is {name}, and I'm {age} years old")
print(f"{user.get('id')}")


number = 10

isPositive = True if number >= 0 else False







