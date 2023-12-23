"""Abstract sprite class definition"""

from abc import abstractmethod

from pygame import sprite, Rect

from . import ISprite


class Sprite(ISprite, sprite.Sprite):
    """Abstract sprite class"""

    def __init__(self) -> None:
        super().__init__()

        self.texture_file: str = ""
        self.texture: str = ""
        self.texture_size: tuple[int, int] = (0, 0)
        self._rect: Rect = Rect(0, 0, 0, 0)

    @property
    def rect(self) -> Rect:
        """Get sprite position and size"""
        return self._rect

    def set_rect(self, rect: Rect) -> None:
        """Set sprite position and size"""
        self._rect = rect

    def set_size(self, rect: Rect) -> None:
        """Set sprite size"""
        self._rect.h = rect.h
        self._rect.w = rect.w

    def set_texture(self, texture_id: str) -> None:
        """Set sprite texture id"""
        self.texture = texture_id

    @abstractmethod
    def update(self, delta: float) -> None:
        """Inheritor-defined abstract update method"""
