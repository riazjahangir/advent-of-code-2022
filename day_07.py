import itertools
from utils import get_input_lines


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size


class Directory:
    def __init__(self, parent, name) -> None:
        self.parent = parent
        self.name = name
        self.dirs = {}
        self.files = {}
        self._size = None

    @property
    def size(self):
        if self._size is None:
            self._size = 0
            for obj in itertools.chain(self.dirs.values(), self.files.values()):
                self._size += obj.size

        return self._size

    def __repr__(self) -> str:
        return f'{self.name} ({self.size})'


def parse_input(input_lines):
    """Parse input lines into pairs of command and output"""
    result = []

    current_command = None
    current_output = []

    for line in input_lines:
        if line.startswith('$'):
            # New command. Close out the previous command if there was one.
            if current_command:
                result.append((current_command, current_output))
            current_command = line[2:]
            current_output = []
        else:
            current_output.append(line)

    # Include the final command
    result.append((current_command, current_output))
    return result


if __name__ == '__main__':
    root_dir = Directory(None, '/')
    flat_dirs = []
    current_working_dir = root_dir

    def process_command(command, output):
        global current_working_dir
        if command.startswith('cd'):
            target = command.split()[1]
            if target == '..':
                current_working_dir = current_working_dir.parent
            elif target == '/':
                current_working_dir = root_dir
            else:
                current_working_dir = current_working_dir.dirs[target]
        elif command.startswith('ls'):
            for listing in output:
                if listing.startswith('dir'):
                    _, dirname = listing.split()
                    if dirname not in current_working_dir.dirs:
                        current_working_dir.dirs[dirname] = Directory(
                            current_working_dir, dirname)
                        flat_dirs.append(current_working_dir.dirs[dirname])
                else:  # File
                    file_size, file_name = listing.split()
                    current_working_dir.files[file_name] = File(
                        file_name, int(file_size))
        else:
            raise RuntimeError(f'Unexpected command: {command}')

    commands = parse_input(get_input_lines(day=7))
    for command, output in commands:
        process_command(command, output)

    # Whew. Now we have a directory tree. What was the question again?
    print(
        f'Part 1: {sum(dir.size for dir in flat_dirs if dir.size <= 100_000)}')

    # Part 2
    total_disk = 70_000_000
    required_space = 30_000_000
    unused_space = total_disk - root_dir.size
    space_to_free = required_space - unused_space

    sorted_dirs = sorted(flat_dirs, key=lambda dir: dir.size)
    for dir in sorted_dirs:
        if dir.size >= space_to_free:
            print(f'Part 2: {dir}')
            break
