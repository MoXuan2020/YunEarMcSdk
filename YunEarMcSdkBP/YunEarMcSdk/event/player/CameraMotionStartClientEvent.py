# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class CameraMotionStartClientEvent(ClientEvent):

    def __init__(self, callback):
        super(CameraMotionStartClientEvent, self).__init__(callback)
        self.motionId = None

    def CreateFromArgs(self, args):
        self.motionId = args.get("motionId")
