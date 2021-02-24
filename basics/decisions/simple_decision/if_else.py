def run():
    # Ask user to enter activity.
    print("Please enter the activity to be performed.")
    activity = input()

    # If activity is 'calculate'
    if activity == "calculate":
        print("Performing calculations...")
    else:
        print("Performing activity...")

    # Completion message
    print("Activity completed!")

# call the function when the module is executed directly
if __name__ == "__main__":
    run()