# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityMotionStopServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityMotionStopServerEvent, self).__init__(callback)
        self.motionId = None
        self.entityId = None
        self.remove = None

    def CreateFromArgs(self, args):
        self.motionId = args.get("motionId")
        self.entityId = args.get("entityId")
        self.remove = args.get("remove")
