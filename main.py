
def main():
    
  # Open the file in read mode
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()

    # Count the number of words
    num_words = count_words(file_contents)

    # Count the occurrences of each character
    char_counts = count_characters(file_contents)

    # Generate the report
    generate_report(file_path, num_words, char_counts)

def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    # Convert the text to lowercase
    text = text.lower()
    
    # Initialize an empty dictionary to store character counts
    char_counts = {}
    
    # Iterate over each character in the text
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    
    return char_counts


def generate_report(file_path, num_words, char_counts):
    # Sort the character counts by frequency in descending order
    sorted_char_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    
    # Print the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for char, count in sorted_char_counts:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    main()