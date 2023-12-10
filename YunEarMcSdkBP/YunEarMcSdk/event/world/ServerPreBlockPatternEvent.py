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
        self.enable_ = args["enable"]
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
        self.dimensionId_ = args["dimensionId"]
        self.entityWillBeGenerated_ = args["entityWillBeGenerated"]
