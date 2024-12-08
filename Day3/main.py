import re

text = open("input.txt", "r").read()
# text =  "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64]do()(mul(11,8)undo()?mul(8,5))"
pattern = r"(?<=mul\()\d+,\d+(?=\))"

pattern1 =  r"don't\(\).*?do\(\)"

revision = re.sub(pattern1, '', text, flags=re.DOTALL)
print(revision)
# Find all matches
matches = re.findall(pattern, revision)

# Convert each match into a tuple of integers
tuples = [tuple(map(int, match.split(','))) for match in matches]
print(tuples)

sum = 0
for i in tuples:
    sum+= i[0] * i[1]
print(sum)