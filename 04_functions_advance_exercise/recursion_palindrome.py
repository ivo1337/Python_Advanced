def palindrome(word, idx):
    if idx == len(word) // 2:
        return "true"

    if word[idx] != word[-idx - 1]:
        return "false"

    return palindrome(word, idx + 1)


print(palindrome("peter", 0))
print(palindrome("abcba", 0))