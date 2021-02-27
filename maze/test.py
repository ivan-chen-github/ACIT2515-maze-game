with open("test.txt", "r") as in_file:
    first_words = ""
    last_words = ""
    word_list = in_file.readlines()
    print(word_list)
    for word in word_list:
        print(word.strip())