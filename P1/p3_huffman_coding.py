import sys
import heapq


def make_frequencies(message):
    char_freq = dict()
    for char in message:
        if char_freq.get(char):
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    freq_char = [(item[1], item[0]) for item in char_freq.items()]
    return freq_char


def make_tree(freq_char):
    # freq_char: list of tuples (frequency, char)
    heap = []
    for lf in freq_char:
        heapq.heappush(heap, [lf])
    while len(heap) > 1:
        left_child = heapq.heappop(heap)
        right_child = heapq.heappop(heap)
        freq0, label0 = left_child[0]
        freq1, label1 = right_child[0]
        label = ''.join(sorted(label0 + label1))
        freq = freq0 + freq1
        node = [(freq, label), left_child, right_child]
        heapq.heappush(heap, node)
    return heap.pop()


def walk_tree(code_tree, code_map, code_prefix):
    # tree: [value, left_child, right_child]
    if len(code_tree) == 1:
        freq, label = code_tree[0]
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
            freq, label = code_tree[0]
            decode_chars.append(label)
            code_tree = tree
    return ''.join(decode_chars)


if __name__ == "__main__":

    a_great_sentence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"

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

# The size of the data is: 97
# The content of the data is: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV
# The size of the encoded data is: 64
# The content of the encoded data is: 11011011011111100011100111101011101111110011110111111011111100000000010001000011001000010100110001110100001001010100101101100011010111001111100000100001100010100011100100100101100110100111101000101001101010101011101100101101101110101111110000110001110010110011110100110101
# The size of the decoded data is: 97
# The content of the encoded data is: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV
# ------------------------------------------------------------
# The size of the data is: 68
# The content of the data is: Something for test.
# The size of the encoded data is: 36
# The content of the encoded data is: 11111100011000011001000101011100111110001010010101110110000101111011110
# The size of the decoded data is: 68
# The content of the encoded data is: Something for test.
# ------------------------------------------------------------
# The size of the data is: 72
# The content of the data is: Another wonderful test.
# The size of the encoded data is: 36
# The content of the encoded data is: 1100111110001011110010000101110110000111111010100001110110101111010111101100010010111000
# The size of the decoded data is: 72
# The content of the encoded data is: Another wonderful test.
