from textnode import *


def main():
    blam = TextNode(
        text="Blam",
        text_type=TextType.LINK,
        url="blam.com",
    )
    print(blam)


if __name__ == "__main__":
    main()
