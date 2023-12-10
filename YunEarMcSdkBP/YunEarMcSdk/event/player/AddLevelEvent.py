# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class AddLevelEvent(ServerEvent):

    def __init__(self, callback):
        super(AddLevelEvent, self).__init__(callback)
        self.id_ = None
        self.addLevel_ = None
        self.newLevel_ = None

    def CreateFromArgs(self, args):
        self.id_ = args.get("id")
        self.addLevel_ = args.get("addLevel")
        self.newLevel_ = args.get("newLevel")
