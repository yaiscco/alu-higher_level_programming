#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:  # Check if the sentence is not empty
        return (len(sentence), sentence[0])
    else:
        return (0, None)  # Return 0 and None for empty sentence

# Example usage
if __name__ == "__main__":
    print(multiple_returns("Hello, World!"))  # Output: (13, 'H')
    print(multiple_returns(""))                  # Output: (0, None)
