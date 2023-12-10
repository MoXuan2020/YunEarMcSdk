# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerJoinMessageEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerJoinMessageEvent, self).__init__(callback)
        self.id_ = None
        self.name_ = None
        self.cancel_ = None
        self.message_ = None

    def CreateFromArgs(self, args):
        self.id_ = args.get("id")
        self.name_ = args.get("name")
        self.cancel_ = args.get("cancel")
        self.message_ = args.get("message")
