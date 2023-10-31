STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # open(file, 'r')
    import string
    with open(file, 'r') as reader:
        text = reader.read()
    # print(text)
    text_list = text.split()
    print(text_list)
    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in text_list]
    print(stripped)
    lower = [strip.lower() for strip in stripped]
    print(lower)





if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
