# Diya Gawande
# 4/7/25

import string

# Constants for English letter frequency and alphabet
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Function to get the frequency count of each letter in a message
def getLetterCount(message):
    # Create a dictionary with each letter set to 0
    letterCount = {letter: 0 for letter in LETTERS}

    # Loop through each character in the message
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1  # Increment the count for the letter

    return letterCount  # Return the dictionary of counts

# Helper function to sort by frequency
def getItemAtIndexZero(items):
    return items[0]

# Function to arrange letters from most to least frequent
def getFrequencyOrder(message):
    letterToFreq = getLetterCount(message)  # Get letter frequency dictionary
    freqToLetter = {}  # Dictionary to map frequency to letters

    # Fill freqToLetter dictionary
    for letter in LETTERS:
        freq = letterToFreq[letter]
        if freq not in freqToLetter:
            freqToLetter[freq] = [letter]
        else:
            freqToLetter[freq].append(letter)

    # Sort each list of letters in ETAOIN order
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    # Create a sorted list of (frequency, letters) pairs
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    # Combine all letters in sorted order
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)

# Function to calculate English frequency match score
def englishFreqMatchScore(message):
    freqOrder = getFrequencyOrder(message)  # Get frequency order of letters
    matchScore = 0  # Initialize match score

    # Add score for common letters
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1

    # Add score for uncommon letters
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore

# Main program starts here
def main():
    # Prompt user for message
    message = input("Enter a message to analyze: ")

    # Output frequency count
    letterCount = getLetterCount(message)
    print("\nLetter Frequency Count:")
    for letter in sorted(letterCount):
        print(f"{letter}: {letterCount[letter]}")

    # Output letters sorted by frequency
    freqOrder = getFrequencyOrder(message)
    print("\nLetters from most to least frequent:")
    print(freqOrder)

    # Output English frequency match score
    matchScore = englishFreqMatchScore(message)
    print(f"\nEnglish Frequency Match Score: {matchScore}")

# Run the main program
if __name__ == "__main__":
    main()
