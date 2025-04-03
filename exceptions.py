def review_ai_code():
    # AI-suggested scores (some bad)
    scores = [85, "fail", 0]
    # Try processing, catch errors
    for score in scores:
        try:
            if not isinstance(score, (int, float)):
                raise ValueError(f"'{score}' isn't a number!")
            percent = score / 100 # Watch for zero!
            print(f"Score: {score} ({percent:.0%})")
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Zero division!")
review_ai_code()
# Learn: Exceptions (Value + Zero Error)