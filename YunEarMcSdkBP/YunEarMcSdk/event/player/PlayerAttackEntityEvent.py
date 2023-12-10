# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerAttackEntityEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerAttackEntityEvent, self).__init__(callback)
        self.playerId_ = None
        self.victimId_ = None
        self.damage_ = None
        self.isValid_ = None
        self.cancel_ = None
        self.isKnockBack_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args["playerId"]
        self.victimId_ = args["victimId"]
        self.damage_ = args["damage"]
        self.isValid_ = args["isValid"]
        self.cancel_ = args["cancel"]
        self.isKnockBack_ = args["isKnockBack"]
