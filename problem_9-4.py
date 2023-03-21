'''9.4 Write a program to read through the mbox-short.txt and figure out who has
sent the greatest number of mail messages. The program looks for 'From 'lines
and takes the second word of those lines as the person who sent the mail. The
program creates a Python dictionary that maps the sender's mail address to a
count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer'''


# store solution in a function named count_commits
def count_commits():

    # open the file
    FILE_NAME = './mbox-short.txt'

    try:
        file = open(FILE_NAME)
    except:
        print(f'{FILE_NAME} not found... exiting')
        exit()
    
    # initialize tracking variables
    count_dict = {}
    current_max_key = ''
    current_max_value = -1

    # traverse file
    for line in file:

        # extract relevant lines
        if line.startswith('From '):

            # extract email
            line_by_word = line.split()
            email = line_by_word[1]

            # increment value or add key with count of 1
            if email in count_dict.keys():

                # increment value
                new_value = count_dict[email] + 1
                count_dict[email] = new_value

                # check for new max
                if count_dict[email] > current_max_value:
                    current_max_key = email
                    current_max_value = new_value

            else:
                # add key with count of 1
                count_dict[email] = 1

                # check for new max
                if count_dict[email] > current_max_value:
                    current_max_key = email
                    current_max_value = 1
    
    # end of file, return max key,value pair
    return current_max_key, current_max_value


# call count_commits to print to terminal
print(count_commits())