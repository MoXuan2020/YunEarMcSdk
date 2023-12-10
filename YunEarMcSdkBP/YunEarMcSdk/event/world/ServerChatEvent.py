# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerChatEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerChatEvent, self).__init__(callback)
        self.username_ = None
        self.playerId_ = None
        self.message_ = None
        self.cancel_ = None
        self.bChatById_ = None
        self.bForbid_ = None
        self.toPlayerIds_ = None
        self.gameChatPrefix_ = None
        self.gameChatPrefixColorR_ = None
        self.gameChatPrefixColorG_ = None
        self.gameChatPrefixColorB_ = None

    def CreateFromArgs(self, args):
        self.username_ = args["username"]
        self.playerId_ = args["playerId"]
        self.message_ = args["message"]
        self.cancel_ = args["cancel"]
        self.bChatById_ = args["bChatById"]
        self.bForbid_ = args["bForbid"]
        self.toPlayerIds_ = args["toPlayerIds"]
        self.gameChatPrefix_ = args["gameChatPrefix"]
        self.gameChatPrefixColorR_ = args["gameChatPrefixColorR"]
        self.gameChatPrefixColorG_ = args["gameChatPrefixColorG"]
        self.gameChatPrefixColorB_ = args["gameChatPrefixColorB"]
