# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class CraftItemOutputChangeServerEvent(ServerEvent):

    def __init__(self, callback):
        super(CraftItemOutputChangeServerEvent, self).__init__(callback)
        self.playerId = None
        self.itemDict = None
        self.screenContainerType = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.itemDict = args.get("itemDict")
        self.screenContainerType = args.get("screenContainerType")
        self.cancel = args.get("cancel")
