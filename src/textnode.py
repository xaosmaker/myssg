from enum import Enum

from htmlnode import LeafNode


class TextType(Enum):
    """
    Enum defining text types and their corresponding HTML tags.
    The enum value is used directly as the HTML tag
                    in text_node_to_html_node function.
    TEXT=None represents raw text without a tag.
    """
    TEXT = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"


class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and \
           self.text_type == other.text_type and \
           self.url == other.url:
            return True
        return False

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")


def text_node_to_html_node(text_node: TextNode):
    """
    Converts a TextNode to an HTMLNode using enum values as HTML tags.

    Design Strategy:
        - TextType enum values directly map to HTML tags (e.g., BOLD="b")
        - Only handle exceptions for special cases (LINK and IMAGE)
                                    that need additional properties
        - All other cases can use the enum value directly as the tag
    """

    if not isinstance(text_node.text_type, TextType):
        raise ValueError("text_node_to_html_node invalid TextNode type")

    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    return LeafNode(text_node.text_type.value, text_node.text)
