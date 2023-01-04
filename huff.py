import heapq as hq
import node as n
import pandas as pd


def make_occur_dict(text):
    """Create dictionary with keys as unique letters and values as how many times they appear"""
    letters = set(text)
    data = {}
    for letter in letters:
        data[letter] = text.count(letter)
    return data


def show_table(dic):
    """Show table with letters and code"""
    df = pd.DataFrame.from_dict(dic, orient='index', columns=['Code'])
    print(df)


class huffman:
    def __init__(self, file):
        self.file = file
        self.heap = []
        self.code = {}

    # HEAP

    def min_heap(self, occurrence_dict):
        """Create heap with Node objects"""
        for letter in occurrence_dict:
            new_node = n.Node(letter, occurrence_dict[letter])
            hq.heappush(self.heap, new_node)

    def merge(self):
        """Merge codes of letters"""
        while len(self.heap) > 1:
            node_1 = hq.heappop(self.heap)
            node_2 = hq.heappop(self.heap)

            new_name = node_1.key + node_2.key
            new_freq = node_1.occurrence + node_2.occurrence

            merged_node = n.Node(new_name, new_freq)
            merged_node.left = node_1
            merged_node.right = node_2

            hq.heappush(self.heap, merged_node)

    # ASSIGNING CODES

    def code_once(self, node, new_code):
        if node is None:
            return
        elif node.key is not None:
            self.code[node.key] = new_code

        self.code_once(node.left, new_code + "0")
        self.code_once(node.right, new_code + "1")

    def clear_codes(self):
        to_delete = []
        for key in self.code:
            if len(key) >= 2 or key == '\n':
                to_delete.append(key)

        if '\n' in to_delete:
            to_delete.remove('\n')

        for key in to_delete:
            self.code.pop(key)

    def coding(self):
        root = hq.heappop(self.heap)
        self.code_once(root, "")
        self.clear_codes()

    # ENCODING AND SAVING

    def encode(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.code[char]
        return encoded_text

    def compress_file(self):
        with open(self.file) as f:
            text = f.read()

            occur_dict = make_occur_dict(text)
            self.min_heap(occur_dict)
            self.merge()

            if len(text) != self.heap[0].occurrence:
                print("Something went wrong. We couldn't compress your file.")
                return

            self.coding()

            show_table(self.code)

            encoded = self.encode(text)

        print("Compression finished")
