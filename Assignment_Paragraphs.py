#File path
file_path = "paragraphs.txt"
# Read the contents of the text file
with open(file_path, "r") as file:
    paragraphs = file.readlines()
    # Remove whitespace and newline characters
    paragraphs = [paragraph.strip() for paragraph in paragraphs]
# Define stop words
stop_words = ["a", "an", "the", "in", "on", "at", "to", "and", "is", "it" , "." , ",", ":"]

# Read the contents of the text file
with open(file_path, "r") as file:
    paragraphs = file.readlines()
    # Remove whitespace and newline characters
    paragraphs = [paragraph.strip() for paragraph in paragraphs]

print("Original paragraphs:")
for paragraph in paragraphs:
    print(paragraph)

# Remove stop words from the paragraphs
filtered_paragraphs = []
for paragraph in paragraphs:
    words = paragraph.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]  # Convert both word and stop_words to lowercase
    filtered_paragraph = " ".join(filtered_words)
    filtered_paragraphs.append(filtered_paragraph)

print("\nParagraphs after removing stop words:")
for paragraph in filtered_paragraphs:
    print(paragraph)

# Count each word
word_counts = {}
for paragraph in filtered_paragraphs:
    words = paragraph.split()
    for word in words:
        word = word.lower()  # Convert to lowercase to count consistently
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

print("\nWord counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
# File path for the new text file
new_file_path = "filtered_word_counts_in_paragraph.txt"

# Write the word counts to a new text file
with open(new_file_path, "w") as file:
    for word, count in word_counts.items():
        file.write(f"{word}: {count}\n")