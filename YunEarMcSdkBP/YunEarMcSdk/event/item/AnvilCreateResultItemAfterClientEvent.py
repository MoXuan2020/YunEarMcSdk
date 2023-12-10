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
        self.playerId_ = args["playerId"]
        self.itemShowName_ = args["itemShowName"]
        self.itemDict_ = args["itemDict"]
        self.oldItemDict_ = args["oldItemDict"]
        self.materialItemDict_ = args["materialItemDict"]
