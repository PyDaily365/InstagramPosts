def format_ai_comment():
    #AI-generated comment
    raw = "code runs fast"
    #.format() with upper case
    print("AI: {0}".format(raw.upper()))
    #F-string: split, cap, join
    words = raw.split()
    print(f"AI: {words[0].capitalize()} {'-'.join(words[1:])}")
    #Pad with underscores
    print(f"Padded: {raw.ljust(15,'!')}")

format_ai_comment()