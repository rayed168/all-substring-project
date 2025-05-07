def find_all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

string = input("Enter a string: ")
result = find_all_substrings(string)
print("All substrings:")
for substr in result:
    print(substr)
