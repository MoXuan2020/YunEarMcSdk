# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class AchievementButtonMovedClientEvent(ClientEvent):

    def __init__(self, callback):
        super(AchievementButtonMovedClientEvent, self).__init__(callback)
        self.oldPosition_ = None
        self.newPosition_ = None

    def CreateFromArgs(self, args):
        self.oldPosition_ = args["oldPosition"]
        self.newPosition_ = args["newPosition"]
