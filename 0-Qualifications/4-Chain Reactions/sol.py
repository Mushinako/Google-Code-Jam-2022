from __future__ import annotations

import sys
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final, Optional

sys.setrecursionlimit(1_000_000)


@dataclass(order=True)
class _Node:
    index: Final[int] = field(hash=True, compare=True)
    fun: Final[int] = field(hash=False, compare=False)
    _parent: Optional[_Node] = field(
        default=None, init=False, hash=False, compare=False
    )
    _children: set[_Node] = field(
        default_factory=set, init=False, hash=False, compare=False
    )

    def __hash__(self) -> int:
        return hash(self.index)

    @property
    def parent(self) -> Optional[_Node]:
        return self._parent

    @parent.setter
    def parent(self, parent: Optional[_Node]) -> None:
        if self._parent is not None:
            self._parent._children.remove(self)
        if parent is not None:
            parent._children.add(self)
        self._parent = parent

    @parent.deleter
    def parent(self) -> None:
        self.parent = None

    @property
    def children(self) -> set[_Node]:
        # Return a shallow copy to avoid accidental modification
        return set(self._children)

    def accum_fun(self, accum: _FunAccumulator) -> int:
        """"""
        if not len(self._children):
            return self.fun
        children_funs = sorted(
            (child_node.accum_fun(accum) for child_node in self._children), reverse=True
        )
        least_fun = children_funs.pop()
        accum.fun += sum(children_funs)
        return max(least_fun, self.fun)


@dataclass()
class _FunAccumulator:
    fun: int = 0


def _make_trees(nodes: list[int], links: list[int]) -> list[_Node]:
    """
    Make trees from nodes, and return a list of top nodes.
    """
    nodes_list: list[_Node] = [_Node(i, fun) for i, fun in enumerate(nodes, start=1)]
    top_nodes: list[_Node] = []
    for child_node, link in zip(nodes_list, links):
        if link == 0:
            top_nodes.append(child_node)
            continue
        # -1 because conversion from 1-based to 0-based
        child_node.parent = nodes_list[link - 1]
    return top_nodes


def _chain_reactions(nodes: list[int], links: list[int]) -> int:
    """"""
    top_nodes = _make_trees(nodes, links)
    fun_accum = _FunAccumulator()
    top_fun = sum(top_node.accum_fun(fun_accum) for top_node in top_nodes)
    return fun_accum.fun + top_fun


def _main() -> None:
    t = int(input())
    for i in range(1, t + 1):
        # `N` not needed
        int(input())
        nodes = list(map(int, input().split()))
        links = list(map(int, input().split()))
        fun = _chain_reactions(nodes, links)
        print(f"Case #{i}: {fun}")


if __name__ == "__main__":
    _main()
