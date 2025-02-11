def print_numbers(*args,**kwargs):
    for value in args:
        print(f"Positional argumnets are:{value}")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_numbers(1,2,3,4,5,"Krish",name="Kirat",age=20,grade="A",Phone_number=7015601064)
