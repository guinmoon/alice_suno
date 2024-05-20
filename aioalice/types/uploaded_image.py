from attr import attrs, attrib

from aioalice.types import AliceObject


@attrs
class UploadedImage(AliceObject):
    """This object represents an uploaded image"""
    id = attrib(type=str)
    origUrl = attrib(default=None, type=str)
    # origUrl will be None if image was uploaded from bytes, not by url

    @property
    def orig_url(self):
        return self.origUrl
