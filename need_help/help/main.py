def format_linter_error(error: dict) -> dict:
    # write your code here
    return {
        key: values
        for key, values in error.items()
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass
