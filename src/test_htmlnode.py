from htmlnode import HTMLNode
import unittest


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://help.me.com", "type": "text"})
        data = node.props_to_html()
        self.assertEqual(data, 'href="https://help.me.com" type="text"')

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        node = HTMLNode("p", "val", "child", "props")
        self.assertEqual(node.__repr__(), "HTMLNode(p, val, child, props)")
