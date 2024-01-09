def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    word_dict = {}
    for line in lines:
        line = line.strip().split()
        number = int(line[0])
        word = line[1]
        word_dict[number] = word

    pyramid = []
    current_line = []
    for number, word in sorted(word_dict.items()):
        current_line.append(word)
        if len(current_line) == number:
            pyramid.append(current_line)
            current_line = []

    decoded_message = ' '.join(' '.join(line) for line in pyramid)
    return decoded_message

# Example usage
message_file = 'message_file.txt'
decoded_message = decode(message_file)
print(decoded_message)
