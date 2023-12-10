# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerLeftMessageServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerLeftMessageServerEvent, self).__init__(callback)
        self.id_ = None
        self.name_ = None
        self.cancel_ = None
        self.message_ = None

    def CreateFromArgs(self, args):
        self.id_ = args["id"]
        self.name_ = args["name"]
        self.cancel_ = args["cancel"]
        self.message_ = args["message"]
