import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    # Read file to get fieldnames for each STR
    with open(sys.argv[1], newline='') as database:
        reader = csv.DictReader(database)
        strs = reader.fieldnames[1:]

    # Read DNA sequence file into a variable
    with open(sys.argv[2], newline='') as dnafile:
        dna = dnafile.read()

    # Find longest match of each STR in DNA sequence
    # Create an empty dictionary which store results of longest match
    results = {}

    # Loop through each str and save the value in the dictionary
    for STR in strs:
        longest_STR = str(longest_match(dna, STR))
        results[STR] = longest_STR

    # Check database for matching profiles
    with open(sys.argv[1], newline='') as database:
        reader = csv.DictReader(database)

        # Read each lines
        for data in reader:
            # Recreate a temporary dictionary without name
            testlist = list(data.items())
            strdata = dict(testlist[1:])
            # Compare temporary dictionary with results
            if strdata == results:
                print(data['name'])
                break
        else:
            print('No match')

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
