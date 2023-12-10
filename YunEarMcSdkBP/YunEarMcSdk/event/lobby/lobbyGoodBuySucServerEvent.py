# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class lobbyGoodBuySucServerEvent(ServerEvent):

    def __init__(self, callback):
        super(lobbyGoodBuySucServerEvent, self).__init__(callback)
        self.eid = None
        self.buyItem = None

    def CreateFromArgs(self, args):
        self.eid = args.get("eid")
        self.buyItem = args.get("buyItem")
