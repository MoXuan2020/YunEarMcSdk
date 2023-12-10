# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityMotionStopServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityMotionStopServerEvent, self).__init__(callback)
        self.motionId_ = None
        self.entityId_ = None
        self.remove_ = None

    def CreateFromArgs(self, args):
        self.motionId_ = args["motionId"]
        self.entityId_ = args["entityId"]
        self.remove_ = args["remove"]
