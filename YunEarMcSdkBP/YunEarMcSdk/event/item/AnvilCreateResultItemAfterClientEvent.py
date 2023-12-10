# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class AnvilCreateResultItemAfterClientEvent(ClientEvent):

    def __init__(self, callback):
        super(AnvilCreateResultItemAfterClientEvent, self).__init__(callback)
        self.playerId = None
        self.itemShowName = None
        self.itemDict = None
        self.oldItemDict = None
        self.materialItemDict = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.itemShowName = args.get("itemShowName")
        self.itemDict = args.get("itemDict")
        self.oldItemDict = args.get("oldItemDict")
        self.materialItemDict = args.get("materialItemDict")
