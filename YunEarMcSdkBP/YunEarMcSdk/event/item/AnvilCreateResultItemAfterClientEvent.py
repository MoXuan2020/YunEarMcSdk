# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class AnvilCreateResultItemAfterClientEvent(ClientEvent):

    def __init__(self, callback):
        super(AnvilCreateResultItemAfterClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.itemShowName_ = None
        self.itemDict_ = None
        self.oldItemDict_ = None
        self.materialItemDict_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.itemShowName_ = args.get("itemShowName")
        self.itemDict_ = args.get("itemDict")
        self.oldItemDict_ = args.get("oldItemDict")
        self.materialItemDict_ = args.get("materialItemDict")
