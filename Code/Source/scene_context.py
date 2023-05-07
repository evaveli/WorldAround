from typing import cast

from Source import ui

from Source.assets import Assets, FailedToLoadAssets
from Source.font_cache import FontCache
from Source.image_cache import ImageCache
from Source.profile import Profile

# TODO:
# how do you initialize the profile?
# solution: store a list of profiles + index of the active profile


class SceneContext:
    """
    A class that holds data that is shared between scenes.
    """

    def __init__(self):
        self.images = ImageCache()
        self.fonts = FontCache()

        assets = Assets.load(self.images, self.fonts)

        if assets is FailedToLoadAssets:
            raise RuntimeError("Failed to load assets")

        self.assets = cast(Assets, assets)
        self.ui = ui.Context(self.images, self.fonts)
