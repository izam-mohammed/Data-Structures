def substring(str1: str, str2: str) -> bool:
    """check  if the str2 is the substring of str1"""

    main = len(str1)
    sub = len(str2)

    for i in range(main):
        if str1[i : i + sub] == str2:
            return True
    return False


# testing

str1 = "hai hisham"
str2 = "his"

if substring(str1, str2):
    print("It is sub")


def reverse(str1):
    res = ""
    for i in str1:
        res = i + res
    return res


# testing

print(reverse("hellooo"))


def longest_substring_without_repeating_chars(s):
    if not s:
        return ""

    start = 0
    max_length = 0
    max_substring = ""
    char_index = {}

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1

        char_index[s[end]] = end

        if end - start + 1 > max_length:
            max_length = end - start + 1
            max_substring = s[start : end + 1]

    return max_substring


# Example usage:
input_string = "abcabcbb"
result = longest_substring_without_repeating_chars(input_string)
print(result)  # This will print "abc"
