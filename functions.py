def buffet():
    """Ticket purchase with age as major criteria."""

    promptm ="please enter your age to purchase a movie tickets"
    promptm +="or enter 'quit' to exit: "
    while True:
        movie_message = input(promptm)
        if movie_message == "quit":
            break
        elif int(movie_message) <=3:
            print(f"age {movie_message} approved,your ticket is free\n")
        elif int(movie_message) <=12:
            print(f"age {movie_message} approved,your ticket is $10\n")
        elif int(movie_message) >=12:
            print(f"age {movie_message} approved, your ticket is $15\n")

buffet()