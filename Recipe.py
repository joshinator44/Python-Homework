

sentence1 = "A vacation is when you take a trip to some {} place with your {} family."
sentence2 = " Usually you go to some place that is near a/an {} or up on a/an {}."
sentence3 = " A good vacation place is one where you can ride {} or place {} or go hunting for {}."
sentence4 = " I like to spend my time {} or {}."
sentence5 = " When parents go on a vacation, they spend their time eating three {} a day, and fathers play golf, and mothers sit around {}."
sentence6 = " Last summer, my little brother fell in a/an {} and got poison {} all over his {}."
sentence7 = " My family is going to (the) {}, and I will practice {}."
sentence8 = " Parents need vacations more than kids because parents are always very {} and because they have to work {} hours every day all year making enough {} to pay for the vacation."

paragraph = sentence1 + sentence2 + sentence3 + sentence4 + sentence5 + sentence6 + sentence7 + sentence8

madlib_prompts = ["Adjective",
                  "Adjective",
                  "Noun",
                  "Noun",
                  "Plural Noun",
                  "Game",
                  "Plural Noun",
                  "Verb ending in \"ing\"",
                  "Verb ending in \"ing\"",
                  "Noun",
                  "Verb ending in \"ing\"",
                  "Noun",
                  "Plant",
                  "Part of the Body",
                  "Place",
                  "Verb ending in \"ing\"",
                  "Adjective",
                  "Number",
                  "Plural Noun"]

answers = []

if __name__ == "__main__":
    for prompt in madlib_prompts:
        answers.append(input("Type in a {}: ".format(prompt)))
    print(paragraph.format(*answers))
