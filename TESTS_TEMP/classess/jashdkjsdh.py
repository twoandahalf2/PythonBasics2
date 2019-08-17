import random

def main(): # main function
    print("Welcome to the number guesser game")
    lower, upper, rand = range_func()
    total_guesses = max_guess_number(lower, upper)
    evaluation(rand, total_guesses)

def range_func():   # allows user to select a range for the number guess
    print("Please select a range in which you would like to guess.")
    lower_range_cut = int(input("Lower boundary limit: "))
    upper_range_cut = int(input("Upper boundary limit: "))
    random_number = random.randint(lower_range_cut, upper_range_cut)
    return lower_range_cut, upper_range_cut, random_number

def max_guess_number(low,high): # returns the total number of guesses
    total_numbers = (high - low) + 1
    total_guesses = 0
    while (2**total_guesses) < total_numbers:
        total_guesses += 1
    print ("You have a total of %d guesses\n"
           "for your range between %d to %d"
           % (total_guesses, low, high))

    return total_guesses

def evaluation(random_number, total_guesses): # evaluates the users input
    guess_count = 0
    while guess_count < total_guesses:
        guess_count += 1
        user_guess = int(input("Your guess: "))
        print("Your guess is: %d" % (user_guess))
        if (random_number == user_guess):
            print("You got it!")
            break
    else:
        print(f"Sorry, you didn't guess it in time. The answer was: {random_number}")

if __name__ == '__main__':
    main()