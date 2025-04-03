def st_patricks_day():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    target = "happystpatricksday".lower()
    result = ""
    for letter in alphabet:
        if letter in target:
            result += letter
    full_phrase = "Happy St. Patricks Day"
    print(full_phrase)
st_patricks_day()