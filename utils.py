import getopt
import os
import sys
import re
from filenames import filenames


def get_provided_arguments(argv, file_from_which_function_is_called):
    files_names = []
    index_file_name = ''
    word = ''
    command = ('python ' + file_from_which_function_is_called + ' -n <files_names> -i <index_file_name>' +
               (' word' if file_from_which_function_is_called == 'query.py' else ''))

    try:
        opts, args = getopt.getopt(argv, 'hn:i:', ['help', 'files_names=', 'index_file_name='])
    except getopt.GetoptError:
        print(command)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(command)
            sys.exit()
        elif opt in ('-n', '--files_names'):
            files_names = arg.split(',')
        elif opt in ('-i', '--index_file_name'):
            index_file_name = arg

    if file_from_which_function_is_called == 'query.py':
        if not args:
            print("Mandatory argument 'word' is missing")
            sys.exit(2)
        else:
            word = args[0]

    args = {
        'files_names': files_names,
        'index_file_name': index_file_name,
        'word': word
    }
    return args


def file_or_directory_exists(path):
    if not os.path.exists(path):
        print(f"File or directory '{path}' does not exist")
        return False
    return True


# If file_name refers to directory, add all files from that directory to file_names
def add_all_files_from_directory_to_file_names(file_name, file_names, default_file_names_needed):
    if not file_or_directory_exists(file_name):
        file_names.remove(file_name)
        return default_file_names_needed

    if os.path.isdir(file_name):
        file_names.remove(file_name)
        for root, dirs, files in os.walk(file_name):
            if len(files) > 0:
                default_file_names_needed = False
                for file in files:
                    file_path = os.path.join(root, file)
                    file_names.append(file_path)
    else:
        default_file_names_needed = False

    return default_file_names_needed


# If files for all given file names do not exist or given directories are empty,
# default_file_names_needed = True and default filenames will be used
def process_arguments(argv, file_from_which_function_is_called):
    args = get_provided_arguments(argv, file_from_which_function_is_called)
    if not args['files_names']:
        args['files_names'] = filenames
    else:
        file_names = (args['files_names'])[:]
        default_file_names_needed = True
        for file_name in file_names:
            default_file_names_needed = add_all_files_from_directory_to_file_names(
                file_name, args['files_names'], default_file_names_needed)
        if default_file_names_needed:
            args['files_names'] = filenames

    if args['index_file_name'] == '' or not file_or_directory_exists(args['index_file_name']):
        args['index_file_name'] = 'index.py'

    return args


# Remove punctuation characters and change all uppercase letters to lowercase letters
def process_word(word):
    return (re.sub(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', '', word)).lower()


def get_words_from_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            tokens = content.split()
            words = []
            for token in tokens:
                word = process_word(token)
                if word != '':
                    words.append(word)
        return words
    except FileNotFoundError:
        print(f"File '{file_name}' is not found")
        sys.exit(2)
    except Exception as e:
        print(f"Error occurred when reading file: {e}")
        sys.exit(2)


def write_to_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
