# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class CameraMotionStopClientEvent(ClientEvent):

    def __init__(self, callback):
        super(CameraMotionStopClientEvent, self).__init__(callback)
        self.motionId = None
        self.remove = None

    def CreateFromArgs(self, args):
        self.motionId = args.get("motionId")
        self.remove = args.get("remove")
