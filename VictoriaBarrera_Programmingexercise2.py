# Victoria Barrera Exercise 2.

# List 30 words and phrases commonly found in spam messages.
spam_keywords = [
    'free', 'act now', 'click here', 'prize', 'winner', 'urgent', 'expires soon', 'limited time offer',
    'bonus', 'once in a lifetime', 'earn money', 'buy now', 'lowest price', 'special offer', 'get rich quick',
    'instant approval', 'money back', 'win big', 'claim now', 'unlimited', 'opt in', 'name brand', 'cheap',
    'discount', 'cash', 'you have been selected', 'while supplies last', 'instant', 'free sample', 'free trial'
]

# This function calculates the spam score based on keywords in the email the user inputs.
def calculate_spam_score(email_message):
    # Initialize spam score.
    spam_score = 0
    # Keeps track of spam keywords.
    found_spam_keywords = []

    # Loops each keyword in the spam_keywords list.
    for keyword in spam_keywords:
        # If the keyword is found in the email, adds a point to the "spam score".
        if keyword.lower() in email_message.lower():
            spam_score += 1
            found_spam_keywords.append(keyword)

    return spam_score, found_spam_keywords

# This function calculates the spam score.
def evaluate_spam_likelihood(spam_score):
    # Determines the likelihood that a message is spam based on the spam score.
    if spam_score >= 5:
        return "Likely Spam"
    elif spam_score >= 2:
        return "Possible Spam"
    else:
        return "Not Spam"

# Main function prompts the user and display the results.
def main():
    # Ask for user input.
    email_message = input("Enter email message: ")

    # Calculates the spam score and find the keywords.
    spam_score, found_spam_keywords = calculate_spam_score(email_message)

    # Print the spam score.
    print(f"\nSpam Score: {spam_score}")

    # Print spam likelihood.
    print(f"Likelihood: {evaluate_spam_likelihood(spam_score)}")

    # Displays keywords.
    if found_spam_keywords:
        print("\n Words/phrases contributed to the spam score:")
        for keyword in found_spam_keywords:
            print(f"- {keyword}")

# Call main function.
if __name__ == "__main__":
    main()
