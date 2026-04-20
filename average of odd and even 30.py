total = 0
evenSums = 0
oddSums = 0
done = False
while(not done):
    user_in = input("Give me an integer or type 'done' to be done.")
    if( user_in.lower() == "done"):
        done = True
    else:
        # assuming they've typed in an integer
        total += int(user_in)
        if user_in % 2 == 0:
            evenSums += user_in
            evenAverage = evenSums / user_in
        else:
            oddSums += user_in
            oddAverage = oddSums / user_in
print(total)
print("Even Average: " + str(evenAverage))
print("Odd Average: " + str(oddAverage))