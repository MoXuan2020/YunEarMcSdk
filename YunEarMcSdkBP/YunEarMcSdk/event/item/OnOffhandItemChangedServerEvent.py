# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnOffhandItemChangedServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnOffhandItemChangedServerEvent, self).__init__(callback)
        self.oldItemDict = None
        self.newItemDict = None
        self.playerId = None

    def CreateFromArgs(self, args):
        self.oldItemDict = args.get("oldItemDict")
        self.newItemDict = args.get("newItemDict")
        self.playerId = args.get("playerId")
