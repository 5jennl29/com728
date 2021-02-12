#Asks user where to look
print("Where should I look?")
where = input()

#If answer is 'in the bedroom' do this...
if where == "in the bedroom":

    print("Where in the bedroom should I look?")
    where_bedroom = input()

    if where_bedroom == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery")

# If answer is 'in the bathroom' do this...
elif where == "in the bathroom":

    print("Where in the bathroom should I look?")
    where_bathroom = input()

    if where_bathroom == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")

# If answer is 'in the lab' do this...
elif where == "in the lab":

    print("Where in the lab should I look?")
    where_lab = input()

    if where_lab == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery")

# If any other answer is given
else:
    print("I do not know where that is but I will keep looking.")
