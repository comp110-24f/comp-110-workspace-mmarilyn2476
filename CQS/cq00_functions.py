__author__ = "730467763"


def mimic(message: str) -> str:
    """Return my message"""
    return message


def main() -> None:
    """Pulls together the function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
