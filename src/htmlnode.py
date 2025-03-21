from __future__ import annotations

__all__ = [
    "HTMLNode",
    "LeafNode",
]


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[HTMLNode] | None = None,
        props: dict | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        string_rep = "".join([f' {k}="{v}"' for k, v in self.props.items()])
        return string_rep

    def __repr__(self):
        props = ", ".join([f"{k}={v!r}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({props})"


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag=None,
        value=None,
        props=None,
    ):
        if not value:
            raise ValueError("All Leaf Nodes must have a value")
        super().__init__(
            tag=tag,
            value = value,
            children=None,
            props=props
        )

    def to_html(self):
        if not self.value:
            raise ValueError("All Leaf Nodes must have a value")
        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag,
        children,
        props: dict|None = None,
    ):
        super().__init__(tag, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError(f'{self.__class__.__name__} must have tag')
        if not self.children:
            raise ValueError(f'{self.__class__.__name__} must have children')
        smoosh_children = ''.join([leaf.to_html() for leaf in self.children])
        return f"<{self.tag}>{smoosh_children}</{self.tag}>"
    

