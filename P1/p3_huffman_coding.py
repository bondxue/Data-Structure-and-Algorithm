import sys
import heapq


def make_frequencies(message):
    char_freq = dict()
    for char in message:
        if char_freq.get(char):
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq.items()


def make_tree(char_freq):
    # char_freq: list of tuples (char, frequency)
    heap = []
    for lf in char_freq:
        heapq.heappush(heap, [lf])
    while len(heap) > 1:
        left_child = heapq.heappop(heap)
        right_child = heapq.heappop(heap)
        label0, freq0 = left_child[0]
        label1, freq1 = right_child[0]
        label = ''.join(sorted(label0 + label1))
        freq = freq0 + freq1
        node = [(label, freq), left_child, right_child]
        heapq.heappush(heap, node)
    return heap.pop()


def walk_tree(code_tree, code_map, code_prefix):
    # tree: [value, left_child, right_child]
    if len(code_tree) == 1:
        label, freq = code_tree[0]
        code_map[label] = code_prefix
    else:
        value, left_child, right_child = code_tree
        walk_tree(left_child, code_map, code_prefix + '0')
        walk_tree(right_child, code_map, code_prefix + '1')


def make_code_map(code_tree):
    code_map = dict()
    walk_tree(code_tree, code_map, '')
    return code_map


def huffman_encoding(data):
    code_tree = make_tree(make_frequencies(data))
    code_map = make_code_map(code_tree)
    encode = ''.join([code_map[char] for char in data])
    return encode, code_tree


def huffman_decoding(data, tree):
    code_tree = tree
    decode_chars = []
    for bit in data:
        if bit == '0':
            code_tree = code_tree[1]
        else:
            code_tree = code_tree[2]
        if len(code_tree) == 1:
            label, freq = code_tree[0]
            decode_chars.append(label)
            code_tree = tree
    return ''.join(decode_chars)


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
