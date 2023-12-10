# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ApproachEntityClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ApproachEntityClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.entityId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.entityId_ = args.get("entityId")
