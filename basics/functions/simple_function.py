# The function
def run():
#def listen():
    print("Please enter a word representing a sound: ",end="")
    sound = input()
    print(f"That was a loud {sound}!")

# Call function 'listen'
#listen()

# call the function when the module is executed directly
if __name__ == "__main__":
    run()