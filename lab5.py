# your full name (as it appears in Blackboard)
# your 9-digit SBU ID number
# Your Stony Brook NetID (Blackboard username)
# CSE 101
# Lab 5

# IN THIS PART OF THE FILE, IT IS VERY IMPORTANT THAT YOU *ONLY* WRITE CODE
# INSIDE THE FUNCTION DEFINITIONS BELOW! IF YOU WRITE CODE BETWEEN (AND OUTSIDE)
# THE FUNCTION DEFINITIONSS, THE GRADING SYSTEM WILL NOT BE ABLE TO READ YOUR
# CODE AND YOU WILL RECEIVE A GRADE OF ZERO FOR THIS ASSIGNMENT!

# COMPLETE THIS FUNCTION FOR PROBLEM 1
def removeLast(first, second):
    for character in second:
        charfind = first.rfind(character)
        if charfind == -1:
            continue
        first = excise(first,charfind)
    return first

# optional helper function for removeLast() (above)
def excise(text, index):
    left = text[:index]
    right = text[index+1:]
    text = left + right
    return text

# COMPLETE THIS FUNCTION FOR PROBLEM 2
def statement(init_balance, transactions):
    for transaction in transactions:
        first = transaction[0]
        second = transaction[1]
        if first == "debit":
            init_balance += second
        elif first == "credit":
            init_balance -= second
        elif first == "interest":
            init_balance *= 1+second
    return init_balance

# COMPLETE THIS FUNCTION FOR PROBLEM 3
def limboScore(scores, contestant):
    result = 0
    for value in scores:
        country = value[0]
        point = value[1]
        if country == contestant:
            result += point + 5
        else:
            result += (point * 2)
    result = result / (len(scores)*2)
    return result

def getHost(url):
    scheme_index = url.rfind("://")
    # Gets the value after ://              irc://foo.com/ -> foo.com/
    url = url[scheme_index + 3 :]
    slash_index = url.find("/")
    # Remove all values including /         foo.com/ -> foo.com
    url = url[:slash_index]
    # Find the last period                  foo.com -> foo
    period_index = url.rfind(".")
    url = url[:period_index]

    # If there are two periods within URL, take only string that is last
    if url.find(".") != -1:
        another_index = url.rfind(".")
        url = url[another_index +1:]
    return url


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE OR REMOVE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part 1 Tests ###############
    print('Testing removeLast("starlord", "thor"):', removeLast("starlord", "thor")) # only some characters appear in first string

    print('Testing removeLast("graymalkin", "rag"):', removeLast("graymalkin", "rag")) # all characters appear in first string

    print('Testing removeLast("Booster Gold", "Aquaman"):', removeLast("Booster Gold", "Aquaman")) # no characters appear in first string

    # Write your own tests for Part 1 here!
    print()  # prints a blank line

    ############### Part 2 Tests ###############
    print('Testing statement(219.73, [["credit", 102.88], ["credit", 468.64], ["interest", 0.23], ["debit", 128.48]]):')
    print("Final balance:", statement(219.73, [["credit", 102.88], ["credit", 468.64], ["interest", 0.23], ["debit", 128.48]]))
    print()

    print('Testing statement(40.22, [["debit", 474.23], ["interest", 0.32], ["debit", 452.68], ["debit", 158.95], ["interest", 0.34], ["credit", 34.47]]):')
    print("Final balance:", statement(40.22, [["debit", 474.23], ["interest", 0.32], ["debit", 452.68], ["debit", 158.95], ["interest", 0.34], ["credit", 34.47]]))
    print()

    print('Testing statement(1220.61, [["credit", 393.09], ["credit", 62.42], ["credit", 284.84], ["payment", 88.19], ["debit", 153.12], ["payment", 122.98], ["credit", 69.1], ["interest", 0.06]]):')
    print("Final balance:", statement(1220.61, [["credit", 393.09], ["credit", 62.42], ["credit", 284.84], ["payment", 88.19], ["debit", 153.12], ["payment", 122.98], ["credit", 69.1], ["interest", 0.06]]))

    # Write your own tests for Part 2 here!
    print() # prints a blank line

    ############### Part 3 Tests ###############
    print('Testing limboScore([["Kenya", 1.8], ["France", 7.8], ["Ethiopia", 1.4], ["India", 5.7], ["South Korea", 8.9], ["Norway", 3.4], ["Morocco", 4.1]], "Thailand"):')
    print("Final score:", limboScore([["Kenya", 1.8], ["France", 7.8], ["Ethiopia", 1.4], ["India", 5.7], ["South Korea", 8.9], ["Norway", 3.4], ["Morocco", 4.1]], "Thailand"))
    print()

    print('Testing limboScore([["USA", 8.4], ["Finland", 2.5], ["Germany", 7.5], ["Jamaica", 1.5], ["Russia", 3.6], ["Poland", 7.9], ["South Africa", 3.7]], "Egypt"):')
    print("Final score:", limboScore([["USA", 8.4], ["Finland", 2.5], ["Germany", 7.5], ["Jamaica", 1.5], ["Russia", 3.6], ["Poland", 7.9], ["South Africa", 3.7]], "Egypt"))
    print()

    print('Testing limboScore([["Norway", 1.4], ["Aruba", 1.3], ["Russia", 8.4], ["Jamaica", 5.5], ["Spain", 2.6], ["USA", 3.3], ["Morocco", 3.0]], "Spain"):')
    print("Final score:", limboScore([["Norway", 1.4], ["Aruba", 1.3], ["Russia", 8.4], ["Jamaica", 5.5], ["Spain", 2.6], ["USA", 3.3], ["Morocco", 3.0]], "Spain"))
    print()

    # Write your own tests for Part 3 here!
    print()  # prints a blank line

    ############### Part 4 Tests ###############
    print('getHost("irc://foo.com/") returns:', getHost("irc://foo.com/"))
    print('getHost("http://i.am.a.hostname.edu/blah/blah/") returns:', getHost("http://i.am.a.hostname.edu/blah/blah/"))
    print('getHost("ftp://some-like.it-hot.net/something/filename.pdf") returns:', getHost("ftp://some-like.it-hot.net/something/filename.pdf"))

    # Write your own tests for Part 4 here!
    print()  # prints a blank line
