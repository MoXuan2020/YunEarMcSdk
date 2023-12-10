# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnCarriedNewItemChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnCarriedNewItemChangedServerEvent, self).__init__(callback)
        self.oldItemDict = None
        self.newItemDict = None
        self.playerId = None

    def CreateFromArgs(self, args):
        self.oldItemDict = args.get("oldItemDict")
        self.newItemDict = args.get("newItemDict")
        self.playerId = args.get("playerId")
