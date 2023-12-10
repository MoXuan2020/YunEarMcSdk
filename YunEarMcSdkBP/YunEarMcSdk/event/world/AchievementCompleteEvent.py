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
        self.playerId_ = args["playerId"]
        self.rootNodeId_ = args["rootNodeId"]
        self.achievementId_ = args["achievementId"]
        self.title_ = args["title"]
        self.description_ = args["description"]
