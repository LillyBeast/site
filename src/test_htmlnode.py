import unittest

from htmlnode import *

leaf1 = LeafNode('span',"this is a span text",{'style':'span style', 'font':'bold'})

leaf2 = LeafNode(tag="ul",value="This is a list leaf node", props={'font':'ariel'})


class TestHTMLNode(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.child_test_node = HTMLNode(
            tag="s"
            , value= "It's a mee! A child test node value!"
        )
        self.test_node = HTMLNode(
            tag="p",
            value="This is a test node string",
            children=[self.child_test_node]
            ,props={"style":"i be styling"}
        )

    def test_values(self):
        self.assertEqual(
            self.test_node.value
            ,"This is a test node string"
        )
        self.assertEqual(
            self.child_test_node.value
            ,"It's a mee! A child test node value!"
        )

    def test_repr(self):
        node = HTMLNode(tag="b", value="nonn", props={"key": "value"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag='b', value='nonn', children=None, props={'key': 'value'})",
        )

    def test_props_to_html(self):
        ...

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            LeafNode(
                tag=None,
                value=None,
            )

        # with self.assertRaises(NotImplementedError):
        #     HTMLNode.props_to_html(HTMLNode())


class TestHTMLLeafNode(unittest.TestCase):

    def test_to_html(self):
        self.assertEqual(
            leaf1.to_html(),
            '<span style="span style" font="bold">this is a span text</span>'
        )

    def test_exceptions(self):
        pass
