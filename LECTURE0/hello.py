# # ask user for their name
# name = input("what is your name ")
# # # say hello to the user
# # print("hello " + name)
# # print("hello  ", end="")  # using comma instead of + will give a gap automatally
# # print(name)
# # print("hello, \"friend\"")
# print(f"Hello, {name}")
# name=name.strip()
# print(f"Hello, {name}")
name=input("whats your name : ").strip().title()
first, middle , last =name.split(" ")


# print(f"Hello, {name}")
print(f"Hello, {middle}")
 