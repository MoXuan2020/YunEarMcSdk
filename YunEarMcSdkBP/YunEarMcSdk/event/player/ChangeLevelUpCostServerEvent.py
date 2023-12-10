# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ChangeLevelUpCostServerEvent(ServerEvent):

    def __init__(self, callback):
        super(ChangeLevelUpCostServerEvent, self).__init__(callback)
        self.level = None
        self.levelUpCostExp = None
        self.changed = None

    def CreateFromArgs(self, args):
        self.level = args.get("level")
        self.levelUpCostExp = args.get("levelUpCostExp")
        self.changed = args.get("changed")
