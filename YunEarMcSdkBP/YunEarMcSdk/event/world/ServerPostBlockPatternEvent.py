# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerPostBlockPatternEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerPostBlockPatternEvent, self).__init__(callback)
        self.entityId = None
        self.entityGenerated = None
        self.x = None
        self.y = None
        self.z = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.entityGenerated = args.get("entityGenerated")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.dimensionId = args.get("dimensionId")
