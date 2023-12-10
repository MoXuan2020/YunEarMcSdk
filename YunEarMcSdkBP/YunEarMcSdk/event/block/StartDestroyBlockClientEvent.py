# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class StartDestroyBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(StartDestroyBlockClientEvent, self).__init__(callback)
        self.pos = None
        self.blockName = None
        self.auxValue = None
        self.playerId = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.pos = args.get("pos")
        self.blockName = args.get("blockName")
        self.auxValue = args.get("auxValue")
        self.playerId = args.get("playerId")
        self.cancel = args.get("cancel")
