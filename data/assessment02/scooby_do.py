def gang():
    print("Loading gang...")
    friends = ["Scooby Doo", "Shaggy Rogers", "Fred Jones", "Daphne Blake", "Velma Dinkley"]

    print(friends)
    print("...Done!")

    return friends


def phrases(friends):
    quotes = {}

    for friend in friends:
        print(f"What does {friend} say?")
        quote = input()
        quotes[f"{friend}"] = quote

    return quotes


def save(quotes):

    with open("quotes.txt", "w") as file:
        for key, value in quotes.items():
            line = f"{key}: {value}\n"

            data = file.write(line)



friends = gang()
quotes = phrases(friends)
print(f"\nPhrases: {quotes}\n")

save(quotes)
print("The file contains...")
file = open("quotes.txt")
print(file.read())