# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnPlayerActiveShieldServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnPlayerActiveShieldServerEvent, self).__init__(callback)
        self.playerId = None
        self.isActive = None
        self.itemDict = None
        self.cancelable = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.isActive = args.get("isActive")
        self.itemDict = args.get("itemDict")
        self.cancelable = args.get("cancelable")
        self.cancel = args.get("cancel")
