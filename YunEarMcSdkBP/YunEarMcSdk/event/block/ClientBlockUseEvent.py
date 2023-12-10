# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ClientBlockUseEvent(ClientEvent):

    def __init__(self, callback):
        super(ClientBlockUseEvent, self).__init__(callback)
        self.playerId = None
        self.blockName = None
        self.aux = None
        self.cancel = None
        self.x = None
        self.y = None
        self.z = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.blockName = args.get("blockName")
        self.aux = args.get("aux")
        self.cancel = args.get("cancel")
        self.x = args.get("x")
        self.y = args.get("y")
        self.z = args.get("z")
