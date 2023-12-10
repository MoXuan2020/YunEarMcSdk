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
        self.playerId_ = args.get("playerId")
        self.victimId_ = args.get("victimId")
        self.damage_ = args.get("damage")
        self.isValid_ = args.get("isValid")
        self.cancel_ = args.get("cancel")
        self.isKnockBack_ = args.get("isKnockBack")
