import os


def main():
    line = (
        "My Monday alarm went off at 6 a.m.; "
        "I negotiated with it until 9 and still lost the meeting."
    )
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
