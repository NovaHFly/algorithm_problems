import re
from typing import TextIO

INSTRUCTION_REGEX = re.compile(r'(\d*)(\[\w+\])')


def get_input(io: TextIO) -> str:
    """Get input from some text io."""
    return io.readline().strip()


def unzip_instructions(instructions: str) -> str:
    """Unzip instructions sequence.

    Unzip instructions sequence by expanding
    substrings like "3[a]" into "aaa".

    Args:
        instructions (str): zipped instructions sequence.

    Returns:
        str: unzipped instructions sequence.
    """
    while match := INSTRUCTION_REGEX.search(instructions):
        instructions = instructions.replace(
            match[0], match[2].strip('[]') * int(match[1])
        )

    return instructions


def main() -> None:
    with open('ciphered_input.txt', encoding='UTF-8') as f:
        instructions = get_input(f)
    print(unzip_instructions(instructions))


if __name__ == '__main__':
    main()
