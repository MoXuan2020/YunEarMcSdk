# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class AchievementCompleteEvent(ServerEvent):

    def __init__(self, callback):
        super(AchievementCompleteEvent, self).__init__(callback)
        self.playerId = None
        self.rootNodeId = None
        self.achievementId = None
        self.title = None
        self.description = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.rootNodeId = args.get("rootNodeId")
        self.achievementId = args.get("achievementId")
        self.title = args.get("title")
        self.description = args.get("description")
