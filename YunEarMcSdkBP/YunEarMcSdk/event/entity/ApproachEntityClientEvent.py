# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ApproachEntityClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ApproachEntityClientEvent, self).__init__(callback)
        self.playerId = None
        self.entityId = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.entityId = args.get("entityId")
