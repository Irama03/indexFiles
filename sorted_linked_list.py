class Node:
    def __init__(self, word=None, freq=[], next_node=None):
        self.word = word
        self.freq = freq
        self.next_node = next_node


class SortedLinkedList:
    def __init__(self, quant_of_files):
        self.head = None
        self.quant_of_files = quant_of_files

    # Add new node or increment frequency of existing word for file by its index in the list
    def add_word_appearance(self, word, file_index_in_list):
        freq = [0] * self.quant_of_files
        freq[file_index_in_list] = 1
        new_node = Node(word, freq)

        # If the list is empty or the new word is smaller alphabetically than the head word,
        # insert at the beginning
        if not self.head or word < self.head.word:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        # If such word already exist in the list, update freq
        if current.word == word:
            current.freq[file_index_in_list] += 1
            return
        while current.next:
            current = current.next
            if current.word == word:
                current.freq[file_index_in_list] += 1
                return

        current = self.head
        # Iterate through the list to find the appropriate position to insert the new node
        while current.next and word > current.next.word:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def to_string(self):
        result = ['{']
        current = self.head
        while current:
            result.append(' "' + current.word + '": ' + str(current.freq) + ',')
            current = current.next
        result.append('}\n')
        return '\n'.join(result)
