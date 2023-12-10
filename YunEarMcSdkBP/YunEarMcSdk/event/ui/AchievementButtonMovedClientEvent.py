# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class AchievementButtonMovedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(AchievementButtonMovedClientEvent, self).__init__(callback)
        self.oldPosition = None
        self.newPosition = None

    def CreateFromArgs(self, args):
        self.oldPosition = args.get("oldPosition")
        self.newPosition = args.get("newPosition")
