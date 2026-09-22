from pathlib import Path

def ask_for_file():
    while True:
        raw = input("Enter the full path of your text file: ").strip()
        raw = raw.strip('"').strip("'")
        path = Path(raw).expanduser()

        if path.suffix.lower() != ".txt":
            print("That's not a text file. Please try again!")
        elif not path.is_file():
            print(f"Couldn't find '{path}'.")
            print(f"Python is looking in: {Path.cwd()}")
        else:
            return path.resolve()


def main():
    file_path = ask_for_file()
    with open(file_path, "r") as file_object:
        for line in file_object:
            print(line.rstrip("\n"))


main()
