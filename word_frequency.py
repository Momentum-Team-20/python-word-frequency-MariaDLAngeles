import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # open(file, 'r')
    # string is a built in module for string manipulation 
    # opening and reaword_countng our file
    with open(file, 'r') as reader:
        text = reader.read()
    # print(text)
    # making our text a list
    text_list = text.split()
    # print(text_list)
    # removing punctuation
    table = str.maketrans("", "", string.punctuation)
    # do nothing, do nothing, remove punctuation
    no_punc = [word.translate(table) for word in text_list]
    # "we're going to translate every word in our text list" -- for every word in text_list we're running translate
    # print(no_punc)
    # making our text lowercase
    lowercase = [word.lower() for word in no_punc]
    # print(lowercase)
    # removing STOP_WORDS from the list
    nonstop = []
    for word in lowercase:
        if word not in STOP_WORDS:
            nonstop.append(word)
    # print(nonstop)
    # starting to count words
    word_count = {}
    for word in nonstop:
        # if word in word_count:
        #     word_count[word] = word_count[word] + 1
        # else:
        #     word_count[word] = 1
        # print(word_count)

        word_count[word] = word_count.get(word, 0) + 1
    # print(word_count)

    for word, count in word_count.items():
        # print(f'{word:>15s}', f'| {count}')
        print(f'{word:>15s}', f'| {count}', count*'*')
    




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
