# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityMotionStartServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityMotionStartServerEvent, self).__init__(callback)
        self.motionId = None
        self.entityId = None

    def CreateFromArgs(self, args):
        self.motionId = args.get("motionId")
        self.entityId = args.get("entityId")
