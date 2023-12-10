# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerNamedEntityServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerNamedEntityServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.entityId_ = None
        self.preName_ = None
        self.afterName_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.entityId_ = args["entityId"]
        self.preName_ = args["preName"]
        self.afterName_ = args["afterName"]
        self.cancel_ = args["cancel"]
