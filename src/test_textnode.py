import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node",
                        TextType.BOLD, "https://test.com")
        node2 = TextNode("This is a text node",
                         TextType.BOLD, "https://test.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node",
                        TextType.BOLD, "https://test.com")
        node2 = TextNode("This is a text node not equal to other",
                         TextType.BOLD, "https://test.com")
        self.assertNotEqual(node, node2)

    def test_without_url(self):
        node = TextNode("This is a text node",
                        TextType.BOLD)
        self.assertEqual(node.url, None)


class TestTextToHTML(unittest.TestCase):
    def test_value_error(self):
        node = TextNode("some Text", TextType.__name__)
        with self.assertRaises(ValueError) as e:
            text_node_to_html_node(node)

        self.assertEqual(str(e.exception),
                         "text_node_to_html_node invalid TextNode type")


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE,
                        "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
