# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnLocalLightningLevelChangeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnLocalLightningLevelChangeServerEvent, self).__init__(callback)
        self.oldLevel = None
        self.newLevel = None
        self.dimensionId = None

    def CreateFromArgs(self, args):
        self.oldLevel = args.get("oldLevel")
        self.newLevel = args.get("newLevel")
        self.dimensionId = args.get("dimensionId")
