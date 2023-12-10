# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class lobbyGoodBuySucServerEvent(ServerEvent):

    def __init__(self, callback):
        super(lobbyGoodBuySucServerEvent, self).__init__(callback)
        self.eid_ = None
        self.buyItem_ = None

    def CreateFromArgs(self, args):
        self.eid_ = args["eid"]
        self.buyItem_ = args["buyItem"]
