import os
from dotenv import load_dotenv

from typing import Optional


class AOCUtils:
    def __init__(self, input_path: Optional[str] = None, get_env: bool = False):
        if input_path:
            self.input_path = input_path
        elif get_env:
            load_dotenv()
            self.input_path = os.environ["INPUT_PATH"]
        else:
            pass

    def get_input_by_line(
        self,
        day: int,
        filepath: Optional[str] = None,
        filename: Optional[str] = None,
        file_prefix: str = "input",
        filetype: str = "txt",
    ):
        if filepath:
            f = open(filepath)
        elif filename:
            f = open(f"{self.input_path}/advent_of_code_2023/inputs/{filename}")
        else:
            f = open(
                f"{self.input_path}/advent_of_code_2023/inputs/{file_prefix}{day}.{filetype}"
            )
        _out = f.readlines()
        f.close()

        return _out
