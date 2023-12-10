# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ClientBlockUseEvent(ClientEvent):

    def __init__(self, callback):
        super(ClientBlockUseEvent, self).__init__(callback)
        self.playerId_ = None
        self.blockName_ = None
        self.aux_ = None
        self.cancel_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.blockName_ = args["blockName"]
        self.aux_ = args["aux"]
        self.cancel_ = args["cancel"]
        self.x_ = args["x"]
        self.y_ = args["y"]
        self.z_ = args["z"]
