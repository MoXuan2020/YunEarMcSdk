# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class OnPlayerHitBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(OnPlayerHitBlockClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.blockId_ = None
        self.auxValue_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.posX_ = args["posX"]
        self.posY_ = args["posY"]
        self.posZ_ = args["posZ"]
        self.blockId_ = args["blockId"]
        self.auxValue_ = args["auxValue"]
