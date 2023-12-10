# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnLocalRainLevelChangeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnLocalRainLevelChangeServerEvent, self).__init__(callback)
        self.oldLevel_ = None
        self.newLevel_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.oldLevel_ = args["oldLevel"]
        self.newLevel_ = args["newLevel"]
        self.dimensionId_ = args["dimensionId"]
