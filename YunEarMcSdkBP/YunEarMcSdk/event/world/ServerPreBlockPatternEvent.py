# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerPreBlockPatternEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerPreBlockPatternEvent, self).__init__(callback)
        self.enable_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.dimensionId_ = None
        self.entityWillBeGenerated_ = None

    def CreateFromArgs(self, args):
        self.enable_ = args.get("enable")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
        self.dimensionId_ = args.get("dimensionId")
        self.entityWillBeGenerated_ = args.get("entityWillBeGenerated")
