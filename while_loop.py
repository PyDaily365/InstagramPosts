def countdown_with_while(start):
    #Use a while loop to count down from the start number
    while start > 0:
        print(f"Counting down: {start}")
        start -= 1 # Decrease by 1 each loop
    print("Blast off!")
countdown_with_while(5)
#Learn: while loops + decrementing