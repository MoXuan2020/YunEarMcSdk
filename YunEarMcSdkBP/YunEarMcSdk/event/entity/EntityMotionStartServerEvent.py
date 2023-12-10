# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class EntityMotionStartServerEvent(ServerEvent):

    def __init__(self, callback):
        super(EntityMotionStartServerEvent, self).__init__(callback)
        self.motionId_ = None
        self.entityId_ = None

    def CreateFromArgs(self, args):
        self.motionId_ = args.get("motionId")
        self.entityId_ = args.get("entityId")
