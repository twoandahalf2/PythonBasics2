###zadacha2 part2 TravelC

cities = {}

while True:
    user_input = input()
    if user_input == "ready":
        break
    a = [item for item in user_input.split(":")]
    city = a[0]

    b = [item for item in a[1].split(",")]

    for i in b:
        c = [item for item in i.split("-")]
        if city not in cities:
            cities[city] = {}
        cities[city][c[0]] = int(c[1])
for city, transport in cities.items():
    cities[city] = sum(transport.values())

while True:
    command = input()
    if command == "travel time!":
        break
    a = [item for item in command.split(" ")]
    check_city = a[0]
    value = int(a[1])
    if check_city in cities:
        if value <= cities[check_city]:
            print(f"{check_city} -> all {value} accommodated")
        else:
            print(f"{check_city} -> all except {abs(cities[check_city] - value)} accommodated")
