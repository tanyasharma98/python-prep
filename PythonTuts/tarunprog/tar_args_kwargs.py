def fun(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(f"{key} is {value}")
    pass


normal = "this is Tarun bhai"
tar = ["tarun", "yo yo ", "honey"]# it pass in tuple
hari = {"ram": "sir", "js": "unknown"}

fun(normal, *tar, **hari)
