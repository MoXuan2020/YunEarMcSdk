# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerPlayerGetExperienceOrbEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerPlayerGetExperienceOrbEvent, self).__init__(callback)
        self.playerId = None
        self.experienceValue = None
        self.cancel = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.experienceValue = args.get("experienceValue")
        self.cancel = args.get("cancel")
