# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class CameraMotionStartClientEvent(ClientEvent):

    def __init__(self, callback):
        super(CameraMotionStartClientEvent, self).__init__(callback)
        self.motionId_ = None

    def CreateFromArgs(self, args):
        self.motionId_ = args["motionId"]
