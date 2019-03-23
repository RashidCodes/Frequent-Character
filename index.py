def find_most_frequently_occuring_character():
    ## Question: write a program that takes a string and prints the most frequently occuring character to the user
    ## There's a much shorter way but I tried to solve this problem without using any modules eg. (Counter from collections)

    ## initialize a count variable to count the number of times a character appears in a string
    count = 0

    # an empty array to store the counts for each character
    empty_arr = []

    ## ask user for input
    some_string = input("Enter your string: ")

    ## create an array of the characters
    character_of_some_string = [ch for ch in some_string]


    for i in range(len(some_string)):
        ## select a character whose frequency you want to count
        character = some_string[i]

        ## increase the count variable by 1 everytime the character is found in the inputted string
        for ch in some_string:
            if character == ch:
                count += 1

        ## append the count variable to the empty array
        empty_arr.append(count)

        ## reset the count variable to 0 for the next character
        count = 0


    ## grab the index of the max value from the empty array(which isn't emtpy anymore)
    index_of_mode = empty_arr.index(max(empty_arr))

    ## find the most frequently occuring character
    mode = character_of_some_string[index_of_mode]

    ## print it to the user
    print("Most frequently occuring character: "f'{mode}')

    
find_most_frequently_occuring_character()


