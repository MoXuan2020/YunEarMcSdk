# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityMotionStopServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityMotionStopServerEvent, self).__init__(callback)
        self.motionId_ = None
        self.entityId_ = None
        self.remove_ = None

    def CreateFromArgs(self, args):
        self.motionId_ = args.get("motionId")
        self.entityId_ = args.get("entityId")
        self.remove_ = args.get("remove")
