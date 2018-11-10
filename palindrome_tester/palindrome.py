import re
#
# #
# pal_1 = "stunt nuts"
# pal_2 = "Lisa Bonet ate no basil."
# pal_3 = "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!"
# pal_4 = "Doc, note, I dissent. A fast never prevents a fatness. I diet on cod."
# pal_5 = "Madam I'm Adam"
# pal_6 = "When a problem comes along, you can whip it, whip it good"
#
#
def is_palindrome(palindrome):
    """
    Given a string, ignore case, strip punctuation and spaces, reverse the string, and determine if
    the original stripped string == reversed string.
    """
    clean_string = re.sub(r'[^A-Za-z]', "", palindrome)
    clean_string = clean_string.lower()
    reverse_string = clean_string[::-1]
    print(" -- From non recursive function -- ")
    if clean_string == reverse_string:
        print("is a palindrome")
    else:
        print("is not a palindrome")

#
# is_palindrome(pal_1)
# is_palindrome(pal_2)
# is_palindrome(pal_3)
# is_palindrome(pal_4)
# is_palindrome(pal_5)
# is_palindrome(pal_6)
# is_palindrome(input("Please enter a string to test if it is a palindrome: "))



# def recursive_is_palindrome(palindrome):
#     if palindrome == [] or len(palindrome) == 1:
#         print("This is a true palindrome!")
#     else:
#         first = palindrome.pop(0)
#         last = palindrome.pop(-1)
#         if first == last:
#             print(palindrome)
#             recursive_is_palindrome(palindrome)
#         else:
#             print("\nThis is most certainly not a palindrome!")


def strip(palindrome):
    stripped = []
    lowercased = palindrome.lower()
    for letter in lowercased:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            stripped.append([letter])
    return stripped


def recursive_is_palindrome(palindrome):
    if palindrome == [] or len(palindrome) == 1:
        print(" -- From recursive function -- ")
        print("is a palindrome")
    else:
        if palindrome[0] == palindrome[-1]:
            recursive_is_palindrome(palindrome[1:-1])
        else:
            print(" -- From recursive function -- ")
            print("is not a palindrome")


test = input("Please enter a sentence")
is_palindrome(test)
recursive_is_palindrome(strip(test))
