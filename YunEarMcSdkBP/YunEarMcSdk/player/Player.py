# -*- coding: utf-8 -*-

from YunEarMcSdk.entity.Entity import Entity
from YunEarMcSdk.event.ClientEvent import ClientEvent
from YunEarMcSdk.event.ServerEvent import ServerEvent


class Player(Entity):

    def __init__(self, event, id):
        super(Player, self).__init__(event, id)

    def CreateLv(self):
        return self.GetEngineCompFactory().CreateLv(self.id)

    def CreatePlayer(self):
        return self.GetEngineCompFactory().CreatePlayer(self.id)

    def CreateFly(self):
        return self.GetEngineCompFactory().CreateFly(self.id)

    def CreateBlockInfo(self):
        return self.GetEngineCompFactory().CreateBlockInfo(self.id)

    def CreateCamera(self):
        return self.GetEngineCompFactory().CreateCamera(self.id)

    def CreatePlayerView(self):
        return self.GetEngineCompFactory().CreatePlayerView(self.id)

    def CreatePlayerAnim(self):
        return self.GetEngineCompFactory().CreatePlayerAnim(self.id)

    def CreateOperation(self):
        return self.GetEngineCompFactory().CreateOperation(self.GetSystemApi().GetLevelId())

    def CreateDevice(self):
        return self.GetEngineCompFactory().CreateDevice(self.GetSystemApi().GetLevelId())

    def AddPlayerExperience(self, exp):
        return self.CreateExp().AddPlayerExperience(exp)

    def AddPlayerLevel(self, level):
        return self.CreateLv().AddPlayerLevel(level)

    def CollectOnlineClientData(self, collectTypes, callback, extraArgs=None):
        return self.CreatePlayer().CollectOnlineClientData(collectTypes, callback, extraArgs)

    def GetArmorValue(self, playerId):
        return self.CreateGame().GetArmorValue(playerId)

    def GetEnchantmentSeed(self):
        return self.CreatePlayer().GetEnchantmentSeed()

    def GetPlayerCurLevelExp(self, playerId):
        return self.CreateGame().GetPlayerCurLevelExp(playerId)

    def GetPlayerExp(self, playerId=None, isPercent=True):
        if isinstance(self.event, ServerEvent):
            return self.CreateExp().GetPlayerExp(isPercent)
        if isinstance(self.event, ClientEvent):
            return self.CreateGame().GetPlayerExp(playerId, isPercent)

    def GetPlayerHealthLevel(self):
        return self.CreatePlayer().GetPlayerHealthLevel()

    def GetPlayerHealthTick(self):
        return self.CreatePlayer().GetPlayerHealthTick()

    def GetPlayerHunger(self):
        return self.CreatePlayer().GetPlayerHunger()

    def GetPlayerLevel(self):
        return self.CreateLv().GetPlayerLevel()

    def GetPlayerMaxExhaustionValue(self):
        return self.CreatePlayer().GetPlayerMaxExhaustionValue()

    def GetPlayerStarveLevel(self):
        return self.CreatePlayer().GetPlayerStarveLevel()

    def GetPlayerStarveTick(self):
        return self.CreatePlayer().GetPlayerStarveTick()

    def GetPlayerTotalExp(self, playerId=None):
        if isinstance(self.event, ServerEvent):
            return self.CreateExp().GetPlayerTotalExp()
        if isinstance(self.event, ClientEvent):
            return self.CreateGame().GetPlayerTotalExp(playerId)

    def IsPlayerNaturalRegen(self):
        return self.CreatePlayer().IsPlayerNaturalRegen()

    def IsPlayerNaturalStarve(self):
        return self.CreatePlayer().IsPlayerNaturalStarve()

    def SetEnchantmentSeed(self, enchantmentSeed):
        return self.CreatePlayer().SetEnchantmentSeed(enchantmentSeed)

    def SetPlayerHealthLevel(self, healthLevel):
        return self.CreatePlayer().SetPlayerHealthLevel(healthLevel)

    def SetPlayerHealthTick(self, healthTick):
        return self.CreatePlayer().SetPlayerHealthTick(healthTick)

    def SetPlayerHunger(self, value):
        return self.CreatePlayer().SetPlayerHunger(value)

    def SetPlayerMaxExhaustionValue(self, value):
        return self.CreatePlayer().SetPlayerMaxExhaustionValue(value)

    def SetPlayerNaturalRegen(self, value):
        return self.CreatePlayer().SetPlayerNaturalRegen(value)

    def SetPlayerNaturalStarve(self, value):
        return self.CreatePlayer().SetPlayerNaturalStarve(value)

    def SetPlayerPrefixAndSuffixName(self, prefix, prefixColor, suffix, suffixColor):
        return self.CreateName().SetPlayerPrefixAndSuffixName(prefix, prefixColor, suffix, suffixColor)

    def SetPlayerStarveLevel(self, starveLevel):
        return self.CreatePlayer().SetPlayerStarveLevel(starveLevel)

    def SetPlayerStarveTick(self, starveTick):
        return self.CreatePlayer().SetPlayerStarveTick(starveTick)

    def SetPlayerTotalExp(self, exp):
        return self.CreateExp().SetPlayerTotalExp(exp)

    def Swing(self):
        return self.CreatePlayer().Swing()

    def getUid(self):
        return self.CreatePlayer().getUid()

    def AddPlayerAroundEntityMotion(self, eID, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0, radius=-1):
        return self.CreateActorMotion().AddPlayerAroundEntityMotion(
            eID,
            angularVelocity,
            axis,
            lockDir,
            stopRad,
            radius
        )

    def AddPlayerAroundPointMotion(self, center, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0):
        return self.CreateActorMotion().AddPlayerAroundPointMotion(center, angularVelocity, axis, lockDir, stopRad)

    def AddPlayerTrackMotion(
            self,
            targetPos,
            duraTime,
            startPos=None,
            relativeCoord=False,
            isLoop=False,
            targetRot=None,
            startRot=None,
            useVelocityDir=False
    ):
        return self.CreateActorMotion().AddPlayerTrackMotion(
            targetPos,
            duraTime,
            startPos,
            relativeCoord,
            isLoop,
            targetRot,
            startRot,
            useVelocityDir
        )

    def AddPlayerVelocityMotion(self, velocity, accelerate=None, useVelocityDir=True):
        return self.CreateActorMotion().AddPlayerVelocityMotion(velocity, accelerate, useVelocityDir)

    def BeginSprinting(self):
        return self.CreateActorMotion().BeginSprinting()

    def ChangePlayerDimension(self, dimensionId, pos):
        return self.CreateDimension().ChangePlayerDimension(dimensionId, pos)

    def ChangePlayerFlyState(self, isFly):
        return self.CreateFly().ChangePlayerFlyState(isFly)

    def EnableKeepInventory(self, enable):
        return self.CreatePlayer().EnableKeepInventory(enable)

    def EndSprinting(self):
        return self.CreateActorMotion().EndSprinting()

    def GetEntityRider(self):
        return self.CreateRide().GetEntityRider()

    def GetInteracteCenterOffset(self):
        return self.CreatePlayer().GetInteracteCenterOffset()

    def GetIsBlocking(self):
        return self.CreatePlayer().GetIsBlocking()

    def GetPickCenterOffset(self):
        return self.CreatePlayer().GetPickCenterOffset()

    def GetPickRange(self):
        return self.CreatePlayer().GetPickRange()

    def GetPlayerExhaustionRatioByType(self, type):
        return self.CreatePlayer().GetPlayerExhaustionRatioByType(type)

    def GetPlayerInteracteRange(self):
        return self.CreatePlayer().GetPlayerInteracteRange()

    def GetPlayerMotions(self):
        return self.CreateActorMotion().GetPlayerMotions()

    def GetPlayerRespawnPos(self):
        return self.CreatePlayer().GetPlayerRespawnPos()

    def GetRelevantPlayer(self, exceptList=None):
        return self.CreatePlayer().GetRelevantPlayer(exceptList)

    def IsEntityRiding(self):
        return self.CreateRide().IsEntityRiding()

    def IsPlayerFlying(self):
        return self.CreateFly().IsPlayerFlying()

    def OpenWorkBench(self):
        return self.CreateBlockInfo().OpenWorkBench()

    def PickUpItemEntity(self, playerEntityId, itemEntityId):
        return self.CreateGame().PickUpItemEntity(playerEntityId, itemEntityId)

    def PlayerDestoryBlock(self, pos, particle=1, sendInv=False):
        return self.CreateBlockInfo().PlayerDestoryBlock(pos, particle, sendInv)

    def PlayerUseItemToEntity(self, entityId):
        return self.CreateBlockInfo().PlayerUseItemToEntity(entityId)

    def PlayerUseItemToPos(self, pos, posType, slotPos=0, facing=1):
        return self.CreateBlockInfo().PlayerUseItemToPos(pos, posType, slotPos, facing)

    def RemovePlayerMotion(self, motionId):
        return self.CreateActorMotion().RemovePlayerMotion(motionId)

    def SetBanPlayerFishing(self, isBan):
        return self.CreatePlayer().SetBanPlayerFishing(isBan)

    def SetInteracteCenterOffset(self, offset):
        return self.CreatePlayer().SetInteracteCenterOffset(offset)

    def SetPickCenterOffset(self, offset):
        return self.CreatePlayer().SetPickCenterOffset(offset)

    def SetPickRange(self, pickRange):
        return self.CreatePlayer().SetPickRange(pickRange)

    def SetPickUpArea(self, area):
        return self.CreatePlayer().SetPickUpArea(area)

    def SetPlayerAttackSpeedAmplifier(self, amplifier):
        return self.CreatePlayer().SetPlayerAttackSpeedAmplifier(amplifier)

    def SetPlayerExhaustionRatioByType(self, type, ratio):
        return self.CreatePlayer().SetPlayerExhaustionRatioByType(type, ratio)

    def SetPlayerInteracteRange(self, interacteRange):
        return self.CreatePlayer().SetPlayerInteracteRange(interacteRange)

    def SetPlayerJumpable(self, isJumpable):
        return self.CreatePlayer().SetPlayerJumpable(isJumpable)

    def SetPlayerMotion(self, motion):
        return self.CreateActorMotion().SetPlayerMotion(motion)

    def SetPlayerMovable(self, isMovable):
        return self.CreatePlayer().SetPlayerMovable(isMovable)

    def SetPlayerRespawnPos(self, pos, dimensionId=0):
        return self.CreatePlayer().SetPlayerRespawnPos(pos, dimensionId)

    def SetPlayerRideEntity(self, playerId, rideEntityId, riderIndex=-1):
        return self.CreateRide().SetPlayerRideEntity(playerId, rideEntityId, riderIndex)

    def StartPlayerMotion(self, motionId):
        return self.CreateActorMotion().StartPlayerMotion(motionId)

    def StopEntityRiding(self):
        return self.CreateRide().StopEntityRiding()

    def StopPlayerMotion(self, motionId):
        return self.CreateActorMotion().StopPlayerMotion(motionId)

    def isGliding(self):
        return self.CreatePlayer().isGliding()

    def isInWater(self):
        return self.CreatePlayer().isInWater()

    def isMoving(self):
        return self.CreatePlayer().isMoving()

    def isRiding(self):
        return self.CreatePlayer().isRiding()

    def isSneaking(self):
        return self.CreatePlayer().isSneaking()

    def isSprinting(self):
        return self.CreatePlayer().isSprinting()

    def isSwimming(self):
        return self.CreatePlayer().isSwimming()

    def setMoving(self):
        return self.CreatePlayer().setMoving()

    def setSneaking(self):
        return self.CreatePlayer().setSneaking()

    def setSprinting(self):
        return self.CreatePlayer().setSprinting()

    def setUsingShield(self, flag=True):
        return self.CreatePlayer().setUsingShield(flag)

    def AddPlayerAnimation(self, animationKey, animationName):
        return self.CreateActorRender().AddPlayerAnimation(animationKey, animationName)

    def AddPlayerAnimationController(self, animationControllerKey, animationControllerName):
        return self.CreateActorRender().AddPlayerAnimationController(animationControllerKey, animationControllerName)

    def AddPlayerAnimationIntoState(self, animationControllerName, stateName, animationName, condition=""):
        return self.CreateActorRender().AddPlayerAnimationIntoState(
            animationControllerName,
            stateName,
            animationName,
            condition
        )

    def AddPlayerGeometry(self, geometryKey, geometryName):
        return self.CreateActorRender().AddPlayerGeometry(geometryKey, geometryName)

    def AddPlayerParticleEffect(self, effectKey, effectName):
        return self.CreateActorRender().AddPlayerParticleEffect(effectKey, effectName)

    def AddPlayerRenderController(self, renderControllerName, condition=""):
        return self.CreateActorRender().AddPlayerRenderController(renderControllerName, condition)

    def AddPlayerRenderMaterial(self, materialKey, materialName):
        return self.CreateActorRender().AddPlayerRenderMaterial(materialKey, materialName)

    def AddPlayerScriptAnimate(self, animateName, condition="", autoReplace=False):
        return self.CreateActorRender().AddPlayerScriptAnimate(animateName, condition, autoReplace)

    def AddPlayerSoundEffect(self, soundKey, soundName):
        return self.CreateActorRender().AddPlayerSoundEffect(soundKey, soundName)

    def AddPlayerTexture(self, geometryKey, geometryName):
        return self.CreateActorRender().AddPlayerTexture(geometryKey, geometryName)

    def RebuildPlayerRender(self):
        return self.CreateActorRender().RebuildPlayerRender()

    def RemovePlayerAnimationController(self, animationControllKey):
        return self.CreateActorRender().RemovePlayerAnimationController(animationControllKey)

    def RemovePlayerGeometry(self, geometryKey):
        return self.CreateActorRender().RemovePlayerGeometry(geometryKey)

    def RemovePlayerRenderController(self, renderControllerName):
        return self.CreateActorRender().RemovePlayerRenderController(renderControllerName)

    def ResetSkin(self):
        return self.CreateModel().ResetSkin()

    def SetPlayerItemInHandVisible(self, visible, mode=0):
        return self.CreateActorRender().SetPlayerItemInHandVisible(visible, mode)

    def SetSkin(self, skin):
        return self.CreateModel().SetSkin(skin)

    def AddEnchantToInvItem(self, slotPos, enchantType, level):
        return self.CreateItem().AddEnchantToInvItem(slotPos, enchantType, level)

    def AddModEnchantToInvItem(self, slotPos, modEnchantId, level):
        return self.CreateItem().AddModEnchantToInvItem(slotPos, modEnchantId, level)

    def ChangePlayerItemTipsAndExtraId(self, posType, slotPos=0, customTips="", extraId=""):
        return self.CreateItem().ChangePlayerItemTipsAndExtraId(posType, slotPos, customTips, extraId)

    def ChangeSelectSlot(self, slot):
        return self.CreatePlayer().ChangeSelectSlot(slot)

    def GetCarriedItem(self, getUserData=False):
        return self.CreateItem().GetCarriedItem(getUserData)

    def GetInvItemEnchantData(self, slotPos):
        return self.CreateItem().GetInvItemEnchantData(slotPos)

    def GetInvItemModEnchantData(self, slotPos):
        return self.CreateItem().GetInvItemModEnchantData(slotPos)

    def GetOffhandItem(self, getUserData=False):
        return self.CreateItem().GetOffhandItem(getUserData)

    def GetPlayerAllItems(self, posType, getUserData=False):
        return self.CreateItem().GetPlayerAllItems(posType, getUserData)

    def GetPlayerItem(self, posType, slotPos=0, getUserData=False):
        return self.CreateItem().GetPlayerItem(posType, slotPos, getUserData)

    def GetSelectSlotId(self):
        return self.CreateItem().GetSelectSlotId()

    def GetSlotId(self):
        return self.CreateItem().GetSlotId()

    def RemoveEnchantToInvItem(self, slotPos, enchantType):
        return self.CreateItem().RemoveEnchantToInvItem(slotPos, enchantType)

    def RemoveModEnchantToInvItem(self, slotPos, modEnchantId):
        return self.CreateItem().RemoveModEnchantToInvItem(slotPos, modEnchantId)

    def SetInvItemExchange(self, pos1, pos2):
        return self.CreateItem().SetInvItemExchange(pos1, pos2)

    def SetInvItemNum(self, slotPos, num):
        return self.CreateItem().SetInvItemNum(slotPos, num)

    def SetPlayerAllItems(self, itemsDictMap):
        return self.CreateItem().SetPlayerAllItems(itemsDictMap)

    def SpawnItemToPlayerCarried(self, itemDict, playerId):
        return self.CreateItem().SpawnItemToPlayerCarried(itemDict, playerId)

    def SpawnItemToPlayerInv(self, itemDict, playerId, slotPos=-1):
        return self.CreateItem().SpawnItemToPlayerInv(itemDict, playerId, slotPos)

    def AddCameraAroundEntityMotion(self, eID, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0, radius=-1):
        return self.CreateCamera().AddCameraAroundEntityMotion(eID, angularVelocity, axis, lockDir, stopRad, radius)

    def AddCameraAroundPointMotion(self, center, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0):
        return self.CreateCamera().AddCameraAroundPointMotion(center, angularVelocity, axis, lockDir, stopRad)

    def AddCameraTrackMotion(
            self,
            targetPos,
            duraTime,
            startPos=None,
            relativeCoord=False,
            isLoop=False,
            targetRot=None,
            startRot=None,
            useVelocityDir=False
    ):
        return self.CreateCamera().AddCameraTrackMotion(
            targetPos,
            duraTime,
            startPos,
            relativeCoord,
            isLoop,
            targetRot,
            startRot,
            useVelocityDir
        )

    def AddCameraVelocityMotion(self, velocity, accelerate=None, useVelocityDir=True):
        return self.CreateCamera().AddCameraVelocityMotion(velocity, accelerate, useVelocityDir)

    def DepartCamera(self):
        return self.CreateCamera().DepartCamera()

    def GetCameraAnchor(self):
        return self.CreateCamera().GetCameraAnchor()

    def GetCameraMotions(self):
        return self.CreateCamera().GetCameraMotions()

    def GetCameraOffset(self):
        return self.CreateCamera().GetCameraOffset()

    def GetCameraPitchLimit(self):
        return self.CreateCamera().GetCameraPitchLimit()

    def GetCameraRotation(self):
        return self.CreateCamera().GetCameraRotation()

    def GetForward(self):
        return self.CreateCamera().GetForward()

    def GetFov(self):
        return self.CreateCamera().GetFov()

    def GetFpHeight(self):
        return self.CreateCamera().GetFpHeight()

    def GetPerspective(self):
        return self.CreatePlayerView().GetPerspective()

    def GetPosition(self):
        return self.CreateCamera().GetPosition()

    def IsModCameraLockPitch(self):
        return self.CreateCamera().IsModCameraLockPitch()

    def IsModCameraLockYaw(self):
        return self.CreateCamera().IsModCameraLockYaw()

    def LockCamera(self, lockPos, lockRot):
        return self.CreateCamera().LockCamera(lockPos, lockRot)

    def LockModCameraPitch(self, enable):
        return self.CreateCamera().LockModCameraPitch(enable)

    def LockModCameraYaw(self, enable):
        return self.CreateCamera().LockModCameraYaw(enable)

    def LockPerspective(self, lock):
        return self.CreatePlayerView().LockPerspective(lock)

    def RemoveCameraMotion(self, motionId):
        return self.CreateCamera().RemoveCameraMotion(motionId)

    def ResetCameraBindActorId(self):
        return self.CreateCamera().ResetCameraBindActorId()

    def SetCameraAnchor(self, offset):
        return self.CreateCamera().SetCameraAnchor(offset)

    def SetCameraBindActorId(self, targetId):
        return self.CreateCamera().SetCameraBindActorId(targetId)

    def SetCameraDistanceFixed(self, isFixed):
        return self.CreateCamera().SetCameraDistanceFixed(isFixed)

    def SetCameraOffset(self, offset):
        return self.CreateCamera().SetCameraOffset(offset)

    def SetCameraPitchLimit(self, limit):
        return self.CreateCamera().SetCameraPitchLimit(limit)

    def SetCameraPos(self, pos):
        return self.CreateCamera().SetCameraPos(pos)

    def SetCameraRotation(self, rot):
        return self.CreateCamera().SetCameraRotation(rot)

    def SetFov(self, fov):
        return self.CreateCamera().SetFov(fov)

    def SetPerspective(self, persp):
        return self.CreatePlayerView().SetPerspective(persp)

    def SetSpeedFovLock(self, isLocked):
        return self.CreateCamera().SetSpeedFovLock(isLocked)

    def StartCameraMotion(self, motionId):
        return self.CreateCamera().StartCameraMotion(motionId)

    def StopCameraMotion(self, motionId):
        return self.CreateCamera().StopCameraMotion(motionId)

    def UnDepartCamera(self):
        return self.CreateCamera().UnDepartCamera()

    def UnLockCamera(self):
        return self.CreateCamera().UnLockCamera()

    def PlayTpAnimation(self, anim):
        return self.CreatePlayerAnim().PlayTpAnimation(anim)

    def StopAnimation(self, anim):
        return self.CreatePlayerAnim().StopAnimation(anim)

    def GetPlayerGameType(self, playerId):
        return self.CreateGame().GetPlayerGameType(playerId)

    def SetPlayerGameType(self, gameType):
        return self.CreatePlayer().SetPlayerGameType(gameType)

    def GetPlayerAbilities(self):
        return self.CreatePlayer().GetPlayerAbilities()

    def GetPlayerOperation(self):
        return self.CreatePlayer().GetPlayerOperation()

    def SetAttackMobsAbility(self, canAttack):
        return self.CreatePlayer().SetAttackMobsAbility(canAttack)

    def SetAttackPlayersAbility(self, canAttack):
        return self.CreatePlayer().SetAttackPlayersAbility(canAttack)

    def SetBuildAbility(self, canBuild):
        return self.CreatePlayer().SetBuildAbility(canBuild)

    def SetMineAbility(self, canMine):
        return self.CreatePlayer().SetMineAbility(canMine)

    def SetOpenContainersAbility(self, canOpen):
        return self.CreatePlayer().SetOpenContainersAbility(canOpen)

    def SetOperateDoorsAndSwitchesAbility(self, canOperate):
        return self.CreatePlayer().SetOperateDoorsAndSwitchesAbility(canOperate)

    def GetNavPath(self, pos, maxTrimNode=16, maxIteration=800, isSwimmer=False):
        return self.GetSystemApi().GetNavPath(pos, maxTrimNode, maxIteration, isSwimmer)

    def StartNavTo(
            self,
            pos,
            sfxPath,
            callback=None,
            sfxIntl=2,
            sfxMaxNum=16,
            sfxScale=(0.5, 0.5),
            maxIteration=800,
            isSwimmer=False,
            fps=20,
            playIntl=8,
            duration=60,
            oneTurnDuration=90,
            sfxDepthTest=False
    ):
        return self.GetSystemApi().StartNavTo(
            pos,
            sfxPath,
            callback,
            sfxIntl,
            sfxMaxNum,
            sfxScale,
            maxIteration,
            isSwimmer,
            fps,
            playIntl,
            duration,
            oneTurnDuration,
            sfxDepthTest
        )

    def StopNav(self):
        return self.GetSystemApi().StopNav()

    def AddPickBlacklist(self, entityId):
        return self.CreateGame().AddPickBlacklist(entityId)

    def ClearPickBlacklist(self):
        return self.CreateGame().ClearPickBlacklist()

    def GetChosen(self):
        return self.CreateCamera().GetChosen()

    def GetChosenEntity(self):
        return self.CreateCamera().GetChosenEntity()

    def GetHoldTimeThresholdInMs(self):
        return self.CreateOperation().GetHoldTimeThresholdInMs()

    def GetInputVector(self):
        return self.CreateActorMotion().GetInputVector()

    def GetMousePosition(self):
        return self.CreateActorMotion().GetMousePosition()

    def GetTouchPos(self):
        return self.GetSystemApi().GetTouchPos()

    def LockInputVector(self, inputVector):
        return self.CreateActorMotion().LockInputVector(inputVector)

    def LockVerticalMove(self, flag):
        return self.CreateActorMotion().LockVerticalMove(flag)

    def PickFacing(self):
        return self.CreateCamera().PickFacing()

    def SetCanAll(self, all):
        return self.CreateOperation().SetCanAll(all)

    def SetCanAttack(self, attack):
        return self.CreateOperation().SetCanAttack(attack)

    def SetCanChat(self, chat):
        return self.CreateOperation().SetCanChat(chat)

    def SetCanDrag(self, drag):
        return self.CreateOperation().SetCanDrag(drag)

    def SetCanInair(self, inair):
        return self.CreateOperation().SetCanInair(inair)

    def SetCanJump(self, jump):
        return self.CreateOperation().SetCanJump(jump)

    def SetCanMove(self, move):
        return self.CreateOperation().SetCanMove(move)

    def SetCanOpenInv(self, open):
        return self.CreateOperation().SetCanOpenInv(open)

    def SetCanPause(self, pause):
        return self.CreateOperation().SetCanPause(pause)

    def SetCanPerspective(self, persp):
        return self.CreateOperation().SetCanPerspective(persp)

    def SetCanScreenShot(self, shot):
        return self.CreateOperation().SetCanScreenShot(shot)

    def SetCanWalkMode(self, walkmode):
        return self.CreateOperation().SetCanWalkMode(walkmode)

    def SetDeviceVibrate(self, milliSeconds):
        return self.CreateDevice().SetDeviceVibrate(milliSeconds)

    def SetHoldTimeThreshold(self, time):
        return self.CreateOperation().SetHoldTimeThreshold(time)

    def SetMoveLock(self, movelock):
        return self.CreateOperation().SetMoveLock(movelock)

    def SetShowRideUI(self, tamedEntityId, isShowUI):
        return self.CreateRide().SetShowRideUI(tamedEntityId, isShowUI)

    def SimulateTouchWithMouse(self, touch):
        return self.CreateGame().SimulateTouchWithMouse(touch)

    def UnLockVerticalMove(self):
        return self.CreateActorMotion().UnLockVerticalMove()

    def UnlockInputVector(self):
        return self.CreateActorMotion().UnlockInputVector()
