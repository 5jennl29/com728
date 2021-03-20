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

    print(quotes)

friends = gang()
quotes = phrases(friends)
