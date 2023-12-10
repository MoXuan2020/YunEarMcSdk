# -*- coding: utf-8 -*-

from YunEarMcSdk.event.ClientEvent import ClientEvent


class ClientShapedRecipeTriggeredEvent(ClientEvent):

    def __init__(self, callback):
        super(ClientShapedRecipeTriggeredEvent, self).__init__(callback)
        self.recipeId = None

    def CreateFromArgs(self, args):
        self.recipeId = args.get("recipeId")
