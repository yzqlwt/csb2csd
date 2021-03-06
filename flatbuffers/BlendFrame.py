# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers

class BlendFrame(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBlendFrame(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BlendFrame()
        x.Init(buf, n + offset)
        return x

    # BlendFrame
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BlendFrame
    def FrameIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # BlendFrame
    def Tween(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BlendFrame
    def BlendFunc(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .BlendFunc import BlendFunc
            obj = BlendFunc()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BlendFrame
    def EasingData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .EasingData import EasingData
            obj = EasingData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def BlendFrameStart(builder): builder.StartObject(4)
def BlendFrameAddFrameIndex(builder, frameIndex): builder.PrependInt32Slot(0, frameIndex, 0)
def BlendFrameAddTween(builder, tween): builder.PrependBoolSlot(1, tween, 1)
def BlendFrameAddBlendFunc(builder, blendFunc): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(blendFunc), 0)
def BlendFrameAddEasingData(builder, easingData): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(easingData), 0)
def BlendFrameEnd(builder): return builder.EndObject()
