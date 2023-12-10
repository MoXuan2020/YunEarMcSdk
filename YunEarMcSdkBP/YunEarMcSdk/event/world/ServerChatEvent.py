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
        self.username_ = args.get("username")
        self.playerId_ = args.get("playerId")
        self.message_ = args.get("message")
        self.cancel_ = args.get("cancel")
        self.bChatById_ = args.get("bChatById")
        self.bForbid_ = args.get("bForbid")
        self.toPlayerIds_ = args.get("toPlayerIds")
        self.gameChatPrefix_ = args.get("gameChatPrefix")
        self.gameChatPrefixColorR_ = args.get("gameChatPrefixColorR")
        self.gameChatPrefixColorG_ = args.get("gameChatPrefixColorG")
        self.gameChatPrefixColorB_ = args.get("gameChatPrefixColorB")
