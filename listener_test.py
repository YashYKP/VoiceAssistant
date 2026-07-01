from listener import listen

while True:

    command = listen()

    if command:

        print("You said :", command)

        if "exit" in command:
            break