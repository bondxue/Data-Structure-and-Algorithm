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

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))

    print('-'*60)
    a_test_sentence = "Something for test."

    print("The size of the data is: {}".format(sys.getsizeof(a_test_sentence)))
    print("The content of the data is: {}".format(a_test_sentence))

    encoded_data, tree = huffman_encoding(a_test_sentence)

    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))

    print('-' * 60)
    another_great_sentence = "Another wonderful test."

    print("The size of the data is: {}".format(sys.getsizeof(another_great_sentence)))
    print("The content of the data is: {}".format(another_great_sentence))

    encoded_data, tree = huffman_encoding(another_great_sentence)

    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))

# The size of the data is: 69
# The content of the data is: The bird is the word
# The size of the encoded data is: 44
# The content of the encoded data is: 000000000010000001000000010000000000000000000010000010001000000001000000000000000010010000000000001000000100000001000000000001000010001000000001
# The size of the decoded data is: 69
# The content of the encoded data is: The bird is the word
# ------------------------------------------------------------
# The size of the data is: 68
# The content of the data is: Something for test.
# The size of the encoded data is: 44
# The content of the encoded data is: 00000000000100010000010000000000110000000100000010000100000000100000000000000000000001000100100000000000001000000000010110000000000001
# The size of the decoded data is: 68
# The content of the encoded data is: Something for test.
# ------------------------------------------------------------
# The size of the data is: 72
# The content of the data is: Another wonderful test.
# The size of the encoded data is: 48
# The content of the encoded data is: 00000000000010000001000001001000000001000000000010000100000000000000100000100000010000000000010000000000100001000000000101000000010000000000000000100000000001000100100000000000001
# The size of the decoded data is: 72
# The content of the encoded data is: Another wonderful test.
