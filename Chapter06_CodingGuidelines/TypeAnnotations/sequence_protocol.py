from __future__ import annotations

from typing import Any
from typing import Collection  # noqa: F401
from typing import Container  # noqa: F401
from typing import Iterable  # noqa: F401
from typing import MutableSequence  # noqa: F401
from typing import Protocol
from typing import Sequence  # noqa: F401
from typing import Sized  # noqa: F401


class SizedMutableIterable(Protocol):
    def __len__(self):
        pass

    def __getitem__(self, idx: int) -> Any:
        pass

    def __setitem__(self, idx: int, val: Any) -> None:
        pass


def iterate_over_length(obj: SizedMutableIterable) -> None:
    for i in range(len(obj)):
        obj[i] = i**2
        print(obj[i])


def main() -> None:
    values = [1, 2, 3]

    iterate_over_length(values)


if __name__ == "__main__":
    main()
