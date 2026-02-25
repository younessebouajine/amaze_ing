
def parsing_line(line: str) -> tuple:
    key, value = line.split("=", 1)
    return key.strip(), value.strip()


def read_file():
    path = "config.txt"
    config = {}

    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = parsing_line(line)
                config[key] = value

    return config

print(read_file())