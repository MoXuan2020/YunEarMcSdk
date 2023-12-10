# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerPreBlockPatternEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerPreBlockPatternEvent, self).__init__(callback)
        self.enable = None
        self.x = None
        self.y = None
        self.z = None
        self.dimensionId = None
        self.entityWillBeGenerated = None

    def CreateFromArgs(self, args):
        self.enable = args.get("enable")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
        self.dimensionId = args.get("dimensionId")
        self.entityWillBeGenerated = args.get("entityWillBeGenerated")
