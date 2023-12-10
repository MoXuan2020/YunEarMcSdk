# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class CommandEvent(ServerEvent):

    def __init__(self, callback):
        super(CommandEvent, self).__init__(callback)
        self.entityId = None
        self.command = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.entityId = args.get("entityId")
        self.command = args.get("command")
        self.cancel = args.get("cancel")
