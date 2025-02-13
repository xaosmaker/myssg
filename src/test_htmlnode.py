from htmlnode import HTMLNode, LeafNode, ParentNode
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


class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        node = ParentNode()
        with self.assertRaises(ValueError) as e:
            node.to_html()
        self.assertEqual(str(e.exception), "tag required for ParentNode")

    def test_no_children(self):
        node = ParentNode(tag="p")
        with self.assertRaises(ValueError) as e:
            node.to_html()
        self.assertEqual(str(e.exception), "children required for ParentNode")

    def test_parent_node(self):
        node = ParentNode("div", children=[LeafNode(
            "div", "im a div", {"type": "text"})])
        to_html = "<div><div type=\"text\">im a div</div></div>"
        self.assertEqual(to_html, node.to_html())

    def test_parent_node_with_props(self):
        node = ParentNode("div", children=[LeafNode(
            "div", "im a div", {"type": "text"})], props={"type": "password"})
        to_html = "<div type=\"password\"><div type=\"text\">im a div</div></div>"
        self.assertEqual(to_html, node.to_html())

    def test_parent_node_with_props_and_multiple_nodes(self):
        node = ParentNode("div", children=[LeafNode(
            "div", "im a div", {"type": "text"}),
            LeafNode(None, "simple text"),
            ParentNode("div", [LeafNode("p", "im a p"),], {"key": "value"}),

        ], props={"type": "password"})
        to_html = "<div type=\"password\"><div type=\"text\">im a div</div>simple text<div key=\"value\"><p>im a p</p></div></div>"
        self.assertEqual(to_html, node.to_html())
