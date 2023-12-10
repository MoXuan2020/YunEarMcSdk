# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ServerEvent import ServerEvent


class PlayerAttackEntityEvent(ServerEvent):

    def __init__(self, callback):
        super(PlayerAttackEntityEvent, self).__init__(callback)
        self.playerId = None
        self.victimId = None
        self.damage = None
        self.isValid = None
        self.cancel = None
        self.isKnockBack = None

    def CreateFromArgs(self, args):
        self.playerId = args.get("playerId")
        self.victimId = args.get("victimId")
        self.damage = args.get("damage")
        self.isValid = args.get("isValid")
        self.cancel = args.get("cancel")
        self.isKnockBack = args.get("isKnockBack")
