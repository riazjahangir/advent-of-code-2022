def find_marker_start(buffer, length):
    for i in range(length, len(buffer)):
        if len(set(buffer[i-length:i])) == length:
            return i


if __name__ == '__main__':
    with open('input.txt') as f:
        buffer = f.read().strip()

    print('Part 1:', find_marker_start(buffer, 4))
    print('Part 2:', find_marker_start(buffer, 14))
