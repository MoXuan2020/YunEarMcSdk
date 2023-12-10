# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class OnPlayerHitBlockServerEvent(ServerEvent):

    def __init__(self, callback):
        super(OnPlayerHitBlockServerEvent, self).__init__(callback)
        self.playerId_ = None
        self.posX_ = None
        self.posY_ = None
        self.posZ_ = None
        self.blockId_ = None
        self.auxValue_ = None
        self.dimensionId_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.posX_ = args.get("posX")
        self.posY_ = args.get("posY")
        self.posZ_ = args.get("posZ")
        self.blockId_ = args.get("blockId")
        self.auxValue_ = args.get("auxValue")
        self.dimensionId_ = args.get("dimensionId")
