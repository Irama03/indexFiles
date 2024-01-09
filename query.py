from utils import process_arguments


def query_index(word, files_names, index_file_name):
    print('Query index')


if __name__ == '__main__':
    args = process_arguments('args')
    query_index(args['word'], args['files_names'], args['index_file_name'])
