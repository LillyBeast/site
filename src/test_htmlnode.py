import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):

    def test_values(self): ...

    def test_repr(self):
        node = HTMLNode(tag="b", value="nonn", props={"key": "value"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag='b', value='nonn', children=None, props={'key': 'value'})"
        )

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            LeafNode(
                tag=None,
                value=None,
            )

        # with self.assertRaises(NotImplementedError):
        #     HTMLNode.props_to_html(HTMLNode())


class TestHTMLLeafNode(unittest.TestCase):
    def test_exceptions(self):
        pass
