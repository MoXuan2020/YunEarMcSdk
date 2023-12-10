# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerItemTryUseEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerItemTryUseEvent, self).__init__(callback)
        self.playerId_ = None
        self.itemDict_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.itemDict_ = args.get("itemDict")
        self.cancel_ = args.get("cancel")
