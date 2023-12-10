# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class AchievementCompleteEvent(ServerEvent):

    def __init__(self, callback):
        super(AchievementCompleteEvent, self).__init__(callback)
        self.playerId_ = None
        self.rootNodeId_ = None
        self.achievementId_ = None
        self.title_ = None
        self.description_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.rootNodeId_ = args.get("rootNodeId")
        self.achievementId_ = args.get("achievementId")
        self.title_ = args.get("title")
        self.description_ = args.get("description")
