# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnLightningLevelChangeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnLightningLevelChangeServerEvent, self).__init__(callback)
        self.oldLevel = None
        self.newLevel = None

    def CreateFromArgs(self, args):
        self.oldLevel = args.get("oldLevel")
        self.newLevel = args.get("newLevel")
