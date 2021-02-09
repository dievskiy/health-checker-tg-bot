from typing import List


def write_tokens_to_file(tokens: List[str]):
    """
    Writes tokens to file
    :param tokens: List of tokens
    """
    if len(tokens) != 2:
        raise ValueError("Length of tokens list is not 2")
    with open("tokens.txt", 'w') as file:
        tokens = [token + "\n" for token in tokens]
        file.writelines(tokens)


def read_tokens_from_file() -> List[str]:
    """
    Reads tokens from file
    :return List of tokens
    """
    with open("tokens.txt") as file:
        return file.readlines()
