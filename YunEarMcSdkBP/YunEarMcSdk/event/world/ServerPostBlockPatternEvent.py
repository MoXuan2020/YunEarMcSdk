# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerPostBlockPatternEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerPostBlockPatternEvent, self).__init__(callback)
        self.entityId_ = None
        self.entityGenerated_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.entityId_ = args.get("entityId")
        self.entityGenerated_ = args.get("entityGenerated")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.dimensionId_ = args.get("dimensionId")
