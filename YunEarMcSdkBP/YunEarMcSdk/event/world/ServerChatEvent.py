# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class ServerChatEvent(ServerEvent):

    def __init__(self, callback):
        super(ServerChatEvent, self).__init__(callback)
        self.username = None
        self.playerId = None
        self.message = None
        self.cancel = None
        self.bChatById = None
        self.bForbid = None
        self.toPlayerIds = None
        self.gameChatPrefix = None
        self.gameChatPrefixColorR = None
        self.gameChatPrefixColorG = None
        self.gameChatPrefixColorB = None

    def CreateFromArgs(self, args):
        self.username = args.get("username")
        self.playerId = args.get("playerId")
        self.message = args.get("message")
        self.cancel = args.get("cancel")
        self.bChatById = args.get("bChatById")
        self.bForbid = args.get("bForbid")
        self.toPlayerIds = args.get("toPlayerIds")
        self.gameChatPrefix = args.get("gameChatPrefix")
        self.gameChatPrefixColorR = args.get("gameChatPrefixColorR")
        self.gameChatPrefixColorG = args.get("gameChatPrefixColorG")
        self.gameChatPrefixColorB = args.get("gameChatPrefixColorB")
