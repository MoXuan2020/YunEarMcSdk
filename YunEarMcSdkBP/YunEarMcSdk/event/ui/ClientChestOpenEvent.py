# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ClientChestOpenEvent(ClientEvent):

    def __init__(self, callback):
        super(ClientChestOpenEvent, self).__init__(callback)
        self.playerId_ = None
        self.x_ = None
        self.y_ = None
        self.z_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.x_ = args.get("x")
        self.y_ = args.get("y")
        self.z_ = args.get("z")
