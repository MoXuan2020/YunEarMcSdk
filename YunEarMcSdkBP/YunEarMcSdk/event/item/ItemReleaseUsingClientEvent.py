# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ItemReleaseUsingClientEvent(ClientEvent):

    def __init__(self, callback):
        super(ItemReleaseUsingClientEvent, self).__init__(callback)
        self.playerId_ = None
        self.durationLeft_ = None
        self.itemDict_ = None
        self.maxUseDuration_ = None
        self.cancel_ = None

    def CreateFromArgs(self, args):
        self.playerId_ = args.get("playerId")
        self.durationLeft_ = args.get("durationLeft")
        self.itemDict_ = args.get("itemDict")
        self.maxUseDuration_ = args.get("maxUseDuration")
        self.cancel_ = args.get("cancel")
