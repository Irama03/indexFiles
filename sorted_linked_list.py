class Node:
    def __init__(self, word=None, freq=[], next_node=None):
        self.word = word
        self.freq = freq
        self.next_node = next_node


class SortedLinkedList:
    def __init__(self):
        self.head = None

    # Add new node or increment frequency of existing word for file by its index in the list
    def add_word_appearance(self, word, file_index_in_list):
        print('Add word appearance')
