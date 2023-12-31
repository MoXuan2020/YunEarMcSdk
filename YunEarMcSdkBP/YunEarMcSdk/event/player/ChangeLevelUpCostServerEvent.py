# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChangeLevelUpCostServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChangeLevelUpCostServerEvent, self).__init__(callback)
        self.level_ = None
        self.levelUpCostExp_ = None
        self.changed_ = None

    def CreateFromArgs(self, args):
        self.level_ = args["level"]
        self.levelUpCostExp_ = args["levelUpCostExp"]
        self.changed_ = args["changed"]
