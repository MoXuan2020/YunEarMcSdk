# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerLeftMessageServerEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerLeftMessageServerEvent, self).__init__(callback)
        self.id = None
        self.name = None
        self.cancel = None
        self.message = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
        self.name = args.get("name")
        self.cancel = args.get("cancel")
        self.message = args.get("message")
