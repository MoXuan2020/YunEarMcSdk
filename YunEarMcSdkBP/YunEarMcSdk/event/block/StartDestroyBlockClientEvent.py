# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class StartDestroyBlockClientEvent(ClientEvent):

    def __init__(self, callback):
        super(StartDestroyBlockClientEvent, self).__init__(callback)
        self.pos_ = None
        self.blockName_ = None
        self.auxValue_ = None
        self.playerId_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.pos_ = args.get("pos")
        self.blockName_ = args.get("blockName")
        self.auxValue_ = args.get("auxValue")
        self.playerId_ = args.get("playerId")
        self.cancel_ = args.get("cancel")
