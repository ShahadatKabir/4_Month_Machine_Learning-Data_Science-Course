# The large File Reader


def file_reader(path, max_line_length = 100000000):
    with open(path, encoding = "utf-8") as file:
        for line_num , line in enumerate(file, start = 1):
            if len(line) > max_line_length:
                raise ValueError(f"Line {line_num} exceeds max line length of {max_line_length}")

            yield line.strip() 
