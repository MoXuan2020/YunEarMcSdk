# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class AddLevelEvent(ServerEvent):

    def __init__(self, callback):
        super(AddLevelEvent, self).__init__(callback)
        self.id = None
        self.addLevel = None
        self.newLevel = None

    def CreateFromArgs(self, args):
        self.id = args.get("id")
        self.addLevel = args.get("addLevel")
        self.newLevel = args.get("newLevel")
