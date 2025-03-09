import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Test", TextType.BOLD)
        node2 = TextNode("Test", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_ulr_none(self):
        node = TextNode("Test", TextType.BOLD, url=None)
        node2 = TextNode("Test", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_ulr_some(self):
        node = TextNode("Test", TextType.BOLD, url="blah.com")
        node2 = TextNode("Test", TextType.BOLD, url="blah.com")
        self.assertEqual(node, node2)

    def test_noteq_link(self):
        node = TextNode("Test", TextType.LINK)
        node2 = TextNode("Test", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()
