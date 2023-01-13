import math

items = [
    82,
    859,
    8686,
    85813,
    858040,
    8580267,
    85802670,
    858026700,
    8580267000,
    85802670000,
    858026700000,
    8580267000000,
    85802670000000,
    858026700000000,
    8580267000000000
]

def convert_byte_size(size):
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size, 1024)))
    p = math.pow(1024, i)
    s = round(size / p, 2)
    return f"{s} {size_name[i]}"

for i in items:
    print(convert_byte_size(i))