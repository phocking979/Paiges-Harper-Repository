import re

# Function 1
def check_alphanumeric(s):
    return bool(re.fullmatch(r'[a-zA-Z0-9]+', s))

print("Function 1 Tests:")
print("ABCDEFabcdef123450 ->", check_alphanumeric("ABCDEFabcdef123450"))
print("*&%@#!}{ ->", check_alphanumeric("*&%@#!}{"))
print()

# Function 2
pattern_zero_or_more = r'^ab*$'

print("Function 2 Tests:")
tests = ["ab", "abc", "a", "ab", "abb"]
for t in tests:
    print(t, "->", bool(re.fullmatch(pattern_zero_or_more, t)))
print()

# Function 3
pattern_one_or_more = r'^ab+$'

print("Function 3 Tests:")
for t in tests:
    print(t, "->", bool(re.fullmatch(pattern_one_or_more, t)))
print()

# Function 4
pattern_lower_underscore = r'^[a-z]+_[a-z]+$'

print("Function 4 Tests:")
tests = ["aab_cbbbc", "aab_Abbbc", "Aaab_abbbc"]
for t in tests:
    print(t, "->", bool(re.fullmatch(pattern_lower_underscore, t)))
print()

# Function 5
pattern_start_word = r'^\w+'

print("Function 5 Tests:")
tests = [
    "The quick brown fox jumps over the lazy dog.",
    " The quick brown fox jumps over the lazy dog."
]
for t in tests:
    match = re.match(pattern_start_word, t)
    print(t, "->", match.group() if match else None)
print()

# Function 6
pattern_contains_z = r'\b\w*[zZ]\w*\b'

print("ZFunction 6 Tests:")
tests = [
    "The quick brown fox jumps over the lazy dog.",
    "Python Exercises."
]
for t in tests:
    print(t, "->", re.findall(pattern_contains_z, t))
print()

# Function 7
def remove_leading_zeros(ip):
    return '.'.join(str(int(part)) for part in ip.split('.'))

print("Function 7 Tests:")
print("216.08.094.196 ->", remove_leading_zeros("216.08.094.196"))
print()

# Function 8
text = 'The quick brown fox jumps over the lazy dog.'
words = ['fox', 'dog', 'horse']

print("Function 8 Tests:")
for word in words:
    found = re.search(word, text)
    print(word, "->", bool(found))
print()

# Function 9
print("9. Find location of 'fox':")
match = re.search('fox', text)
if match:
    print("'fox' found at index:", match.start())
print()

# Function 10
def replace_space_underscore(s):
    if '_' in s:
        return s.replace('_', ' ')
    else:
        return s.replace(' ', '_')

print("10. Replace spaces and underscores:")
print("Regular Expressions ->", replace_space_underscore("Regular Expressions"))
print("Code_Examples ->", replace_space_underscore("Code_Examples"))
print()

# Function 11
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams"
pattern_date = r'/(\d{4})/(\d{2})/(\d{2})/'

print("11. Extract date from URL:")
match = re.search(pattern_date, url)
if match:
    print("Year:", match.group(1))
    print("Month:", match.group(2))
    print("Day:", match.group(3))
print()

# Function 12
pattern_ae = r'\b[aeAE]\w*'

text = "The following example creates an ArrayList with a capacity of 50 elements."

print("12. Words starting with 'a' or 'e':")
print(re.findall(pattern_ae, text))
print()

# Function 13
text = 'Python Exercises, PHP exercises.'

print("13. Replace space/comma/dot with colon:")
print(re.sub(r'[ ,.]', ':', text))
print()

# Function 14
print("14. Words starting with 'a' or 'e':")
print(re.findall(pattern_ae, text))
print()

# Function 15
def remove_extra_spaces(s):
    return re.sub(r'\s+', ' ', s)

print("15. Remove multiple spaces:")
print("'Python      Exercises' ->", remove_extra_spaces("Python      Exercises"))