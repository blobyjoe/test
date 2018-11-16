def let_to_num(letter):
    letter = letter.upper()
    
    if letter == "":
        return "The key corresponding to an empty space is 1"
    if letter.isdigit():
        return "You have entered a number"
    
    key = 0
    while key < 10:
            if phone_letters[key].find(letter) > -1:
    # Create Code: determine if letter is **`in`** any of the phone_letters[key] where key is the index 0 -9:
                 return "The key coressponding to", letter, "is", key
            else:
                    key = key + 1
