from attr import attrs, attrib

from aioalice.types import AliceObject


@attrs
class UploadedSound(AliceObject):
    """This object represents an uploaded sound"""
    id = attrib(type=str)
    originalName = attrib(default=None, type=str)
    skillId = attrib(default=None, type=str)
    size = attrib(default=None, type=int)
    createdAt = attrib(default=None, type=str)
    isProcessed = attrib(default=None, type=str)
    error = attrib(default=None, type=str)
    # origUrl will be None if image was uploaded from bytes, not by url

    @property
    def orig_name(self):
        return self.originalName
