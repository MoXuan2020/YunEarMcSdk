# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ClientChestOpenEvent(ClientEvent):

    def __init__(self, callback):
        super(ClientChestOpenEvent, self).__init__(callback)
        self.playerId = None
        self.x = None
        self.y = None
        self.z = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
