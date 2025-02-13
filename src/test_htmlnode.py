from htmlnode import HTMLNode, LeafNode
import unittest


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://help.me.com", "type": "text"})
        data = node.props_to_html()
        self.assertEqual(data, ' href="https://help.me.com" type="text"')

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        node = HTMLNode("p", "val", "child", "props")
        self.assertEqual(node.__repr__(), "HTMLNode(p, val, child, props)")


class TestLeafNode(unittest.TestCase):
    def test_to_html_no_value(self):
        node = LeafNode()
        with self.assertRaises(ValueError) as e:
            node.to_html()
        self.assertEqual(str(e.exception), "value required for LeafNode")

    def test_normal_text(self):
        node = LeafNode(value="some plain text")
        self.assertEqual(node.to_html(), "some plain text")

    def test_text_with_tag(self):
        node = LeafNode(tag="div", value="I'm a div")
        self.assertEqual(node.to_html(), "<div>I'm a div</div>")

    def test_text_with_tag_and_props(self):
        node = LeafNode(tag="div", value="I'm a div", props={
                        "type": "text", "value": "124"})
        self.assertEqual(
            node.to_html(), "<div type=\"text\" value=\"124\">I'm a div</div>")
