# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class CommandBlockContainerOpenEvent(ServerEvent):

    def __init__(self, callback):
        super(CommandBlockContainerOpenEvent, self).__init__(callback)
        self.playerId_ = None
        self.isBlock_ = None
        self.blockX_ = None
        self.blockY_ = None
        self.blockZ_ = None
        self.victimId_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.isBlock_ = args["isBlock"]
        self.blockX_ = args["blockX"]
        self.blockY_ = args["blockY"]
        self.blockZ_ = args["blockZ"]
        self.victimId_ = args["victimId"]
        self.cancel_ = args["cancel"]
