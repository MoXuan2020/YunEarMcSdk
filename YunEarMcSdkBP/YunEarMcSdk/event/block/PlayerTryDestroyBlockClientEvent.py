# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class PlayerTryDestroyBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(PlayerTryDestroyBlockClientEvent, self).__init__(callback)
        self.x_ = None
        self.y_ = None
        self.z_ = None
        self.face_ = None
        self.blockName_ = None
        self.auxData_ = None
        self.playerId_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
        self.face_ = args["face"]
        self.blockName_ = args["blockName"]
        self.auxData_ = args["auxData"]
        self.playerId_ = args["playerId"]
        self.cancel_ = args["cancel"]
