# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi

from YunEarMcSdk.event.item.ClientItemTryUseEvent import ClientItemTryUseEvent
from YunEarMcSdk.event.ui.UiInitFinished import UiInitFinished
from YunEarMcSdk.sdk.Sdk import YunEarMcSdk
from YunEarMobEditorScripts.config import modConfig


@YunEarMcSdk
class MobEditorMod(object):

    def __init__(self):
        self.mobEditorScreenNode = None

    @UiInitFinished
    def UiInitFinished(self, _):
        clientApi.RegisterUI(
            modConfig.ModName,
            modConfig.ScreenNodeName,
            modConfig.ScreenNodeClsPath,
            modConfig.ScreenNodeDef
        )

    @ClientItemTryUseEvent
    def ClientItemTryUseEvent(self, event):
        # type: (ClientItemTryUseEvent) -> None
        if event.itemDict_["newItemName"] == "yunear:mob_editor":
            if self.mobEditorScreenNode is None:
                self.mobEditorScreenNode = clientApi.CreateUI(
                    modConfig.ModName,
                    modConfig.ScreenNodeName,
                    {
                        "isHud": 1
                    }
                )
            else:
                self.mobEditorScreenNode.SetRemove()
                self.mobEditorScreenNode = None
