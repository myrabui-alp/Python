# Remove special symbols / punctuation from a string
import string

oldString = "/*Jon is @developer & musician"
newString = oldString.translate(
    str.maketrans("", "", string.punctuation))
print(newString)
