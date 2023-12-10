# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnRainLevelChangeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnRainLevelChangeServerEvent, self).__init__(callback)
        self.oldLevel_ = None
        self.newLevel_ = None

    def CreateFromArgs(self, args):
        self.oldLevel_ = args.get("oldLevel")
        self.newLevel_ = args.get("newLevel")
