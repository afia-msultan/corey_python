greeting = "Hello"
name = "Afia"

message = f"{greeting}, {name.upper()}. Welcome."

print(message)

print(message[0:5])
print(message[7:11])

print(message.count("l"))  # how many times 'l' is in sentence

print(message.find("AFIA")) # location of 'AFIA'

message = f"{greeting.replace('Hello', 'Hi!')}, {name.upper()}. Welcome."
print(message.upper())

# print(dir(name))
# print(help(str.lower))

print("Enter your name: ")
name = input()

message = f"{greeting}, {name.upper()}. Welcome."
print(message)

#  python3 PycharmProjects/Project1/strings.py  # terminal
#  sudo /opt/pycharm/bin/pycharm.sh
