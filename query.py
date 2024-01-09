import sys
import os
import importlib
from utils import process_arguments


# Write to standard output the list of files containing the word ordered by the number of occurrences
# of the word in the file. Each line of output is a frequency followed by the filename
def query_index(word, files_names, index_file_name):
    module = importlib.import_module(os.path.splitext(index_file_name)[0])
    index = module.index
    try:
        frequency = index[word]
    except KeyError:
        print('Word is not present in files')
        return
    for i, fr in enumerate(frequency):
        frequency[i] = str(fr) + ' ' + os.path.splitext(files_names[i])[0]
    frequency.sort(reverse=True)
    print('Frequency for word ' + word + ':')
    for fr in frequency:
        print(fr)


if __name__ == '__main__':
    args = process_arguments(sys.argv[1:], 'query.py')
    query_index(args['word'], args['files_names'], args['index_file_name'])
