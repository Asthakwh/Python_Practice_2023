def extract_digit_words_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            words = content.split()  # Split by whitespace
            digit_words = [word for word in words if word.isdigit()]
            print("Words composed of digits only:")
            print(" ".join(digit_words) if digit_words else "None found.")
    except FileNotFoundError:
        print("File not found. Please check the path.")

# Example usage
# Make sure a file like 'input.txt' exists with some text
extract_digit_words_from_file('input.txt')
