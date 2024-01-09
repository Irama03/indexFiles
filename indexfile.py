import sys
from utils import process_arguments, get_words_from_file, write_to_file
from sorted_linked_list import SortedLinkedList


def create_index(files_names, index_file_name):
    files_length = len(files_names)
    if files_length == 0:
        print("No files were provided, so index was not created")
        return

    index_list = SortedLinkedList(files_length)
    for i, file_name in enumerate(files_names):
        words = get_words_from_file(file_name)
        for word in words:
            index_list.add_word_appearance(word, i)
    write_to_file(index_file_name, 'index = ' + index_list.to_string())

    print('Index for ' + str(files_length) + ' files was created')


if __name__ == '__main__':
    args = process_arguments(sys.argv[1:], 'indexfile.py')
    create_index(args['files_names'], args['index_file_name'])
