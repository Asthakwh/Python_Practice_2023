def sort_words():
    input_str = input("Enter comma-separated words: ")
    words = [word.strip() for word in input_str.split(',')]
    words.sort()
    output_str = ', '.join(words)
    print("Sorted words:", output_str)

# Example usage
sort_words()
