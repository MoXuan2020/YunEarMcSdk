# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class CameraMotionStopClientEvent(ClientEvent):

    def __init__(self, callback):
        super(CameraMotionStopClientEvent, self).__init__(callback)
        self.motionId_ = None
        self.remove_ = None

    def CreateFromArgs(self, args):
        self.motionId_ = args["motionId"]
        self.remove_ = args["remove"]
