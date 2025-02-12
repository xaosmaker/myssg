import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
