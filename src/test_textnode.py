import unittest

from textnode import *


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


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")



if __name__ == "__main__":
    unittest.main()
