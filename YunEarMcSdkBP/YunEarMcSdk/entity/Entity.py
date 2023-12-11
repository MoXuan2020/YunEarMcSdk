# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

from YunEarMcSdk.event.ClientEvent import ClientEvent
from YunEarMcSdk.event.ServerEvent import ServerEvent


class Entity(object):

    def __init__(self, event, id):
        self.event = event
        self.id = id

    def GetSystemApi(self):
        if isinstance(self.event, ServerEvent):
            return serverApi
        if isinstance(self.event, ClientEvent):
            return clientApi

    def GetEngineCompFactory(self):
        return self.GetSystemApi().GetEngineCompFactory()

    def CreateEngineType(self):
        return self.GetEngineCompFactory().CreateEngineType(self.id)

    def CreateEntityDefinitions(self):
        return self.GetEngineCompFactory().CreateEntityDefinitions(self.id)

    def CreateAuxValue(self):
        return self.GetEngineCompFactory().CreateAuxValue(self.id)

    def CreateDimension(self):
        return self.GetEngineCompFactory().CreateDimension(self.id)

    def CreateEntityComponent(self):
        return self.GetEngineCompFactory().CreateEntityComponent(self.id)

    def CreateAttr(self):
        return self.GetEngineCompFactory().CreateAttr(self.id)

    def CreateRot(self):
        return self.GetEngineCompFactory().CreateRot(self.id)

    def CreateBreath(self):
        return self.GetEngineCompFactory().CreateBreath(self.id)

    def CreateActorOwner(self):
        return self.GetEngineCompFactory().CreateActorOwner(self.id)

    def CreatePos(self):
        return self.GetEngineCompFactory().CreatePos(self.id)

    def CreateGravity(self):
        return self.GetEngineCompFactory().CreateGravity(self.id)

    def CreateGame(self):
        return self.GetEngineCompFactory().CreateGame(self.GetSystemApi().GetLevelId())

    def CreateName(self):
        return self.GetEngineCompFactory().CreateName(self.id)

    def CreateCollisionBox(self):
        return self.GetEngineCompFactory().CreateCollisionBox(self.id)

    def CreateEntityEvent(self):
        return self.GetEngineCompFactory().CreateEntityEvent(self.id)

    def CreateActorMotion(self):
        return self.GetEngineCompFactory().CreateActorMotion(self.id)

    def CreateRide(self):
        return self.GetEngineCompFactory().CreateRide(self.id)

    def CreateAction(self):
        return self.GetEngineCompFactory().CreateAction(self.id)

    def CreateControlAi(self):
        return self.GetEngineCompFactory().CreateControlAi(self.id)

    def CreateTame(self):
        return self.GetEngineCompFactory().CreateTame(self.id)

    def CreateHurt(self):
        return self.GetEngineCompFactory().CreateHurt(self.id)

    def CreateActorCollidable(self):
        return self.GetEngineCompFactory().CreateActorCollidable(self.id)

    def CreateActorPushable(self):
        return self.GetEngineCompFactory().CreateActorPushable(self.id)

    def CreateInteract(self):
        return self.GetEngineCompFactory().CreateInteract(self.id)

    def CreateShareables(self):
        return self.GetEngineCompFactory().CreateShareables(self.id)

    def CreateMoveTo(self):
        return self.GetEngineCompFactory().CreateMoveTo(self.id)

    def CreatePersistence(self):
        return self.GetEngineCompFactory().CreatePersistence(self.id)

    def CreateEffect(self):
        return self.GetEngineCompFactory().CreateEffect(self.id)

    def CreateActorRender(self):
        return self.GetEngineCompFactory().CreateActorRender(self.id)

    def CreateModel(self):
        return self.GetEngineCompFactory().CreateModel(self.id)

    def CreateHealth(self):
        return self.GetEngineCompFactory().CreateHealth(self.id)

    def CreateItem(self):
        return self.GetEngineCompFactory().CreateItem(self.id)

    def CreateModAttr(self):
        return self.GetEngineCompFactory().CreateModAttr(self.id)

    def CreateExtraData(self):
        return self.GetEngineCompFactory().CreateExtraData(self.id)

    def CreateQueryVariable(self):
        return self.GetEngineCompFactory().CreateQueryVariable(self.id)

    def CreateBulletAttributes(self):
        return self.GetEngineCompFactory().CreateBulletAttributes(self.id)

    def CreateExp(self):
        return self.GetEngineCompFactory().CreateExp(self.id)

    def CreatePet(self):
        return self.GetEngineCompFactory().CreatePet(self.id)

    def CreateTag(self):
        return self.GetEngineCompFactory().CreateTag(self.id)

    def CreateChatExtension(self):
        return self.GetEngineCompFactory().CreateChatExtension(self.id)

    def GetEngineType(self):
        return self.CreateEngineType().GetEngineType()

    def GetEngineTypeStr(self):
        return self.CreateEngineType().GetEngineTypeStr()

    def GetEntityDefinitions(self):
        return self.CreateEntityDefinitions().GetEntityDefinitions()

    def GetAuxValue(self):
        return self.CreateAuxValue().GetAuxValue()

    def ChangeEntityDimension(self, dimensionId, pos=None):
        return self.CreateDimension().ChangeEntityDimension(dimensionId, pos)

    def GetAllComponentsName(self):
        return self.CreateEntityComponent().GetAllComponentsName()

    def GetAttrMaxValue(self, type):
        return self.CreateAttr().GetAttrMaxValue(type)

    def GetAttrValue(self, attrType):
        return self.CreateAttr().GetAttrValue(attrType)

    def GetBodyRot(self):
        return self.CreateRot().GetBodyRot()

    def GetCurrentAirSupply(self):
        if isinstance(self.event, ServerEvent):
            return self.CreateBreath().GetCurrentAirSupply()
        if isinstance(self.event, ClientEvent):
            return self.CreateGame().GetCurrentAirSupply(self.id)

    def GetDeathTime(self):
        return self.CreateEntityDefinitions().GetDeathTime()

    def GetEntityDimensionId(self):
        return self.CreateDimension().GetEntityDimensionId()

    def GetEntityFallDistance(self):
        return self.CreateEntityDefinitions().GetEntityFallDistance()

    def GetEntityLinksTag(self):
        return self.CreateEntityDefinitions().GetEntityLinksTag()

    def GetEntityOwner(self):
        return self.CreateActorOwner().GetEntityOwner()

    def GetFootPos(self):
        return self.CreatePos().GetFootPos()

    def GetGravity(self):
        return self.CreateGravity().GetGravity()

    def GetLoadActors(self):
        return self.CreateGame().GetLoadActors()

    def GetMarkVariant(self):
        return self.CreateEntityDefinitions().GetMarkVariant()

    def GetMaxAirSupply(self):
        if isinstance(self.event, ServerEvent):
            return self.CreateBreath().GetMaxAirSupply()
        if isinstance(self.event, ClientEvent):
            return self.CreateGame().GetMaxAirSupply(self.id)

    def GetMobColor(self):
        return self.CreateEntityDefinitions().GetMobColor()

    def GetMobStrength(self):
        return self.CreateEntityDefinitions().GetMobStrength()

    def GetMobStrengthMax(self):
        return self.CreateEntityDefinitions().GetMobStrengthMax()

    def GetName(self):
        return self.CreateName().GetName()

    def GetPos(self):
        return self.CreatePos().GetPos()

    def GetRiderId(self, playerId):
        return self.CreateGame().GetRiderId(playerId)

    def GetRot(self):
        return self.CreateRot().GetRot()

    def GetSize(self):
        return self.CreateCollisionBox().GetSize()

    def GetTradeLevel(self):
        return self.CreateEntityDefinitions().GetTradeLevel()

    def GetTypeFamily(self):
        return self.CreateAttr().GetTypeFamily()

    def GetUnitBubbleAirSupply(self):
        return self.CreateBreath().GetUnitBubbleAirSupply()

    def GetVariant(self):
        return self.CreateEntityDefinitions().GetVariant()

    def HasChest(self):
        return self.CreateEntityDefinitions().HasChest()

    def HasComponent(self, attrType):
        return self.CreateEntityComponent().HasComponent(attrType)

    def HasShddled(self):
        return self.CreateEntityDefinitions().HasShddled()

    def IsAngry(self):
        return self.CreateEntityDefinitions().IsAngry()

    def IsBaby(self):
        return self.CreateEntityDefinitions().IsBaby()

    def IsConsumingAirSupply(self):
        return self.CreateBreath().IsConsumingAirSupply()

    def IsIllagerCaptain(self):
        return self.CreateEntityDefinitions().IsIllagerCaptain()

    def IsNaturallySpawned(self):
        return self.CreateEntityDefinitions().IsNaturallySpawned()

    def IsOutOfControl(self):
        return self.CreateEntityDefinitions().IsOutOfControl()

    def IsPregnant(self):
        return self.CreateEntityDefinitions().IsPregnant()

    def IsSheared(self):
        return self.CreateEntityDefinitions().IsSheared()

    def IsSitting(self):
        return self.CreateEntityDefinitions().IsSitting()

    def IsTamed(self):
        return self.CreateEntityDefinitions().IsTamed()

    def LockLocalPlayerRot(self, lock):
        return self.CreateRot().LockLocalPlayerRot(lock)

    def PromoteToIllagerCaptain(self):
        return self.CreateEntityDefinitions().PromoteToIllagerCaptain()

    def SetAngry(self, isAngry, targerId=""):
        return self.CreateEntityDefinitions().SetAngry(isAngry, targerId)

    def SetAsAdult(self):
        return self.CreateEntityDefinitions().SetAsAdult()

    def SetAttrMaxValue(self, type, value):
        return self.CreateAttr().SetAttrMaxValue(type, value)

    def SetAttrValue(self, attrType, value):
        return self.CreateAttr().SetAttrValue(attrType, value)

    def SetChest(self, hasChest):
        return self.CreateEntityDefinitions().SetChest(hasChest)

    def SetCurrentAirSupply(self, data):
        return self.CreateBreath().SetCurrentAirSupply(data)

    def SetEntityLookAtPos(self, targetPos, minTime, maxTime, reject):
        return self.CreateRot().SetEntityLookAtPos(targetPos, minTime, maxTime, reject)

    def SetEntityOwner(self, targetId):
        return self.CreateActorOwner().SetEntityOwner(targetId)

    def SetFootPos(self, footPos):
        return self.CreatePos().SetFootPos(footPos)

    def SetGravity(self, gravity):
        return self.CreateGravity().SetGravity(gravity)

    def SetMarkVariant(self, variantType):
        return self.CreateEntityDefinitions().SetMarkVariant(variantType)

    def SetMaxAirSupply(self, data):
        return self.CreateBreath().SetMaxAirSupply(data)

    def SetMobColor(self, colorType):
        return self.CreateEntityDefinitions().SetMobColor(colorType)

    def SetMobStrength(self, strength):
        return self.CreateEntityDefinitions().SetMobStrength(strength)

    def SetMobStrengthMax(self, strength):
        return self.CreateEntityDefinitions().SetMobStrengthMax(strength)

    def SetName(self, name):
        return self.CreateName().SetName(name)

    def SetOutOfControl(self, isOutOfControl):
        return self.CreateEntityDefinitions().SetOutOfControl(isOutOfControl)

    def SetPersistent(self, persistent):
        return self.CreateAttr().SetPersistent(persistent)

    def SetPlayerLookAtPos(self, targetPos, pitchStep, yawStep, blockInput=True):
        return self.CreateRot().SetPlayerLookAtPos(targetPos, pitchStep, yawStep, blockInput)

    def SetPos(self, pos):
        return self.CreatePos().SetPos(pos)

    def SetRecoverTotalAirSupplyTime(self, timeSec):
        return self.CreateBreath().SetRecoverTotalAirSupplyTime(timeSec)

    def SetRot(self, rot):
        return self.CreateRot().SetRot(rot)

    def SetSheared(self, isSheared):
        return self.CreateEntityDefinitions().SetSheared(isSheared)

    def SetSitting(self, shouldSitDown):
        return self.CreateEntityDefinitions().SetSitting(shouldSitDown)

    def SetSize(self, size):
        return self.CreateCollisionBox().SetSize(size)

    def SetTradeLevel(self, holderId):
        return self.CreateEntityDefinitions().SetTradeLevel(holderId)

    def SetVariant(self, variantType):
        return self.CreateEntityDefinitions().SetVariant(variantType)

    def isEntityInLava(self):
        return self.CreateAttr().isEntityInLava()

    def isEntityOnGround(self):
        return self.CreateAttr().isEntityOnGround()

    def AddActorComponentGroup(self, groupName):
        return self.CreateEntityEvent().AddActorComponentGroup(groupName)

    def AddEntityAroundEntityMotion(self, eID, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0, radius=-1):
        return self.CreateActorMotion().AddEntityAroundEntityMotion(
            eID,
            angularVelocity,
            axis,
            lockDir,
            stopRad,
            radius
        )

    def AddEntityAroundPointMotion(self, center, angularVelocity, axis=(0, 1, 0), lockDir=False, stopRad=0):
        return self.CreateActorMotion().AddEntityAroundPointMotion(center, angularVelocity, axis, lockDir, stopRad)

    def AddEntitySeat(self, pos, rot=0, lock_rot=181):
        return self.CreateRide().AddEntitySeat(pos, rot, lock_rot)

    def AddEntityTrackMotion(
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
        return self.CreateActorMotion().AddEntityTrackMotion(
            targetPos,
            duraTime,
            startPos,
            relativeCoord,
            isLoop,
            targetRot,
            startRot,
            useVelocityDir
        )

    def AddEntityVelocityMotion(self, velocity, accelerate=None, useVelocityDir=True):
        return self.CreateActorMotion().AddEntityVelocityMotion(velocity, accelerate, useVelocityDir)

    def ChangeRiderSeat(self, riderIndex):
        return self.CreateRide().ChangeRiderSeat(riderIndex)

    def DeleteEntitySeat(self, seatIndex):
        return self.CreateRide().DeleteEntitySeat(seatIndex)

    def GetAttackTarget(self):
        return self.CreateAction().GetAttackTarget()

    def GetBlockControlAi(self):
        return self.CreateControlAi().GetBlockControlAi()

    def GetCustomGoalCls(self):
        return self.GetSystemApi().GetCustomGoalCls()

    def GetEntityMotions(self):
        return self.CreateActorMotion().GetEntityMotions()

    def GetLeashHolder(self):
        return self.CreateEntityDefinitions().GetLeashHolder()

    def GetMotion(self):
        return self.CreateActorMotion().GetMotion()

    def GetOwnerId(self):
        return self.CreateTame().GetOwnerId()

    def GetRiders(self):
        return self.CreateRide().GetRiders()

    def GetStepHeight(self):
        return self.CreateAttr().GetStepHeight()

    def Hurt(self, damage, cause, attackerId=None, childAttackerId=None, knocked=True):
        return self.CreateHurt().Hurt(damage, cause, attackerId, childAttackerId, knocked)

    def ImmuneDamage(self, immune):
        return self.CreateHurt().ImmuneDamage(immune)

    def IsEating(self):
        return self.CreateEntityDefinitions().IsEating()

    def IsEntityOnFire(self):
        return self.CreateAttr().IsEntityOnFire()

    def IsLootDropped(self):
        return self.CreateEntityDefinitions().IsLootDropped()

    def IsPersistent(self):
        return self.CreateEntityDefinitions().IsPersistent()

    def IsRoaring(self):
        return self.CreateEntityDefinitions().IsRoaring()

    def IsStunned(self):
        return self.CreateEntityDefinitions().IsStunned()

    def RemoveActorComponentGroup(self, groupName):
        return self.CreateEntityEvent().RemoveActorComponentGroup(groupName)

    def RemoveEntityMotion(self, motionId):
        return self.CreateActorMotion().RemoveEntityMotion(motionId)

    def ResetAttackTarget(self):
        return self.CreateAction().ResetAttackTarget()

    def ResetMotion(self):
        return self.CreateActorMotion().ResetMotion()

    def ResetStepHeight(self):
        return self.CreateAttr().ResetStepHeight()

    def SetActorCollidable(self, isCollidable):
        return self.CreateActorCollidable().SetActorCollidable(isCollidable)

    def SetActorPushable(self, isPushable):
        return self.CreateActorPushable().SetActorPushable(isPushable)

    def SetAttackTarget(self, targetId):
        return self.CreateAction().SetAttackTarget(targetId)

    def SetBlockControlAi(self, isBlock, freezeAnim=False):
        return self.CreateControlAi().SetBlockControlAi(isBlock, freezeAnim)

    def SetCanOtherPlayerRide(self, tamedEntityId, canRide):
        return self.CreateRide().SetCanOtherPlayerRide(tamedEntityId, canRide)

    def SetControl(self, tamedEntityId, isControl):
        return self.CreateRide().SetControl(tamedEntityId, isControl)

    def SetEntityInteractFilter(self, index, interactFilter):
        return self.CreateInteract().SetEntityInteractFilter(index, interactFilter)

    def SetEntityLockRider(self, isLock):
        return self.CreateRide().SetEntityLockRider(isLock)

    def SetEntityOnFire(self, seconds, burn_damage=1):
        return self.CreateAttr().SetEntityOnFire(seconds, burn_damage)

    def SetEntityRide(self, playerId, tamedEntityId):
        return self.CreateRide().SetEntityRide(playerId, tamedEntityId)

    def SetEntitySeat(self, seatIndex, pos, rot=0, lock_rot=181):
        return self.CreateRide().SetEntitySeat(seatIndex, pos, rot, lock_rot)

    def SetEntityShareablesItems(self, items):
        return self.CreateShareables().SetEntityShareablesItems(items)

    def SetEntityTamed(self, playerId, tamedId):
        return self.CreateTame().SetEntityTamed(playerId, tamedId)

    def SetJumpPower(self, jumpPower):
        return self.CreateGravity().SetJumpPower(jumpPower)

    def SetLeashHolder(self, holderId):
        return self.CreateEntityDefinitions().SetLeashHolder(holderId)

    def SetLootDropped(self, isLootDropped):
        return self.CreateEntityDefinitions().SetLootDropped(isLootDropped)

    def SetMobKnockback(self, xd=0.1, zd=0.1, power=1.0, height=1.0, heightCap=1.0):
        return self.CreateAction().SetMobKnockback(xd, zd, power, height, heightCap)

    def SetMotion(self, motion):
        return self.CreateActorMotion().SetMotion(motion)

    def SetMoveSetting(self, pos, speed, maxIteration, callback=None):
        return self.CreateMoveTo().SetMoveSetting(pos, speed, maxIteration, callback)

    def SetPersistence(self, isPersistent):
        return self.CreatePersistence().SetPersistence(isPersistent)

    def SetRidePos(self, tamedEntityId, pos):
        return self.CreateRide().SetRidePos(tamedEntityId, pos)

    def SetRiderRideEntity(self, riderId, riddenEntityId, riderIndex=-1):
        return self.CreateRide().SetRiderRideEntity(riderId, riddenEntityId, riderIndex)

    def SetStepHeight(self, stepHeight):
        return self.CreateAttr().SetStepHeight(stepHeight)

    def StartEntityMotion(self, motionId):
        return self.CreateActorMotion().StartEntityMotion(motionId)

    def StopEntityMotion(self, motionId):
        return self.CreateActorMotion().StopEntityMotion(motionId)

    def TriggerCustomEvent(self, entityId, eventName):
        return self.CreateEntityEvent().TriggerCustomEvent(entityId, eventName)

    def AddEffectToEntity(self, effectName, duration, amplifier, showParticles):
        return self.CreateEffect().AddEffectToEntity(effectName, duration, amplifier, showParticles)

    def GetAllEffects(self):
        return self.CreateEffect().GetAllEffects()

    def HasEffect(self, effectName):
        return self.CreateEffect().HasEffect(effectName)

    def RemoveEffectFromEntity(self, effectName):
        return self.CreateEffect().RemoveEffectFromEntity(effectName)

    def AddActorAnimation(self, actorIdentifier, animationKey, animationName):
        return self.CreateActorRender().AddActorAnimation(actorIdentifier, animationKey, animationName)

    def AddActorAnimationController(self, actorIdentifier, animationControllerKey, animationControllerName):
        return self.CreateActorRender().AddActorAnimationController(
            actorIdentifier,
            animationControllerKey,
            animationControllerName
        )

    def AddActorBlockGeometry(self, geometryName, offset=(0, 0, 0), rotation=(0, 0, 0)):
        return self.CreateActorRender().AddActorBlockGeometry(geometryName, offset, rotation)

    def AddActorGeometry(self, actorIdentifier, geometryKey, geometryName):
        return self.CreateActorRender().AddActorGeometry(actorIdentifier, geometryKey, geometryName)

    def AddActorParticleEffect(self, actorIdentifier, effectKey, effectName):
        return self.CreateActorRender().AddActorParticleEffect(actorIdentifier, effectKey, effectName)

    def AddActorRenderController(self, actorIdentifier, renderControllerName, condition=""):
        return self.CreateActorRender().AddActorRenderController(actorIdentifier, renderControllerName, condition)

    def AddActorRenderControllerArray(self, actorIdentifier, renderControllerName, arrayType, arrayName, expression):
        return self.CreateActorRender().AddActorRenderControllerArray(
            actorIdentifier,
            renderControllerName,
            arrayType,
            arrayName,
            expression
        )

    def AddActorRenderMaterial(self, actorIdentifier, materialKey, materialName):
        return self.CreateActorRender().AddActorRenderMaterial(actorIdentifier, materialKey, materialName)

    def AddActorScriptAnimate(self, actorIdentifier, animateName, condition="", autoReplace=False):
        return self.CreateActorRender().AddActorScriptAnimate(actorIdentifier, animateName, condition, autoReplace)

    def AddActorSoundEffect(self, actorIdentifier, soundKey, soundName):
        return self.CreateActorRender().AddActorSoundEffect(actorIdentifier, soundKey, soundName)

    def AddActorTexture(self, actorIdentifier, textureKey, texturePath):
        return self.CreateActorRender().AddActorTexture(actorIdentifier, textureKey, texturePath)

    def BindEntityToEntity(self, bindEntityId):
        return self.CreateModel().BindEntityToEntity(bindEntityId)

    def ClearActorBlockGeometry(self):
        return self.CreateActorRender().ClearActorBlockGeometry()

    def CopyActorGeometryFromPlayer(self, fromPlayerId, toActorIdentifier, fromGeometryKey, newGeometryKey):
        return self.CreateActorRender().CopyActorGeometryFromPlayer(
            fromPlayerId,
            toActorIdentifier,
            fromGeometryKey,
            newGeometryKey
        )

    def CopyActorRenderMaterialFromPlayer(self, fromPlayerId, toActorIdentifier, fromMaterialKey, newMaterialKey):
        return self.CreateActorRender().CopyActorRenderMaterialFromPlayer(
            fromPlayerId,
            toActorIdentifier,
            fromMaterialKey,
            newMaterialKey
        )

    def CopyActorTextureFromPlayer(self, fromPlayerId, toActorIdentifier, fromTextureKey, newTextureKey):
        return self.CreateActorRender().CopyActorTextureFromPlayer(
            fromPlayerId,
            toActorIdentifier,
            fromTextureKey,
            newTextureKey
        )

    def DeleteActorBlockGeometry(self, geometryName):
        return self.CreateActorRender().DeleteActorBlockGeometry(geometryName)

    def GetActorRenderParams(self, entityId, paramTypeStr):
        return self.CreateActorRender().GetActorRenderParams(entityId, paramTypeStr)

    def GetEntityExtraUniforms(self, uniformIndex):
        return self.CreateActorRender().GetEntityExtraUniforms(uniformIndex)

    def GetEntityRenderDistance(self):
        return self.CreateActorRender().GetEntityRenderDistance()

    def GetEntityUIExtraUniforms(self, entityIdentifier, uniformIndex):
        return self.CreateActorRender().GetEntityUIExtraUniforms(entityIdentifier, uniformIndex)

    def GetNotRenderAtAll(self):
        return self.CreateActorRender().GetNotRenderAtAll()

    def RebuildActorRender(self, actorIdentifier):
        return self.CreateActorRender().RebuildActorRender(actorIdentifier)

    def RemoveActorAnimationController(self, actorIdentifier, animationControllKey):
        return self.CreateActorRender().RemoveActorAnimationController(actorIdentifier, animationControllKey)

    def RemoveActorGeometry(self, actorIdentifier, geometryKey):
        return self.CreateActorRender().RemoveActorGeometry(actorIdentifier, geometryKey)

    def RemoveActorRenderController(self, actorIdentifier, renderControllerName):
        return self.CreateActorRender().RemoveActorRenderController(actorIdentifier, renderControllerName)

    def RemoveActorTexture(self, actorIdentifier, textureKey):
        return self.CreateActorRender().RemoveActorTexture(actorIdentifier, textureKey)

    def ResetBindEntity(self):
        return self.CreateModel().ResetBindEntity()

    def SetActorAllBlockGeometryVisible(self, visible):
        return self.CreateActorRender().SetActorAllBlockGeometryVisible(visible)

    def SetActorBlockGeometryVisible(self, geometryName, visible):
        return self.CreateActorRender().SetActorBlockGeometryVisible(geometryName, visible)

    def SetAlwaysShowName(self, show):
        return self.CreateName().SetAlwaysShowName(show)

    def SetColor(self, front, back):
        return self.CreateHealth().SetColor(front, back)

    def SetEntityExtraUniforms(self, uniformIndex, data):
        return self.CreateActorRender().SetEntityExtraUniforms(uniformIndex, data)

    def SetEntityRenderDistance(self, distance):
        return self.CreateActorRender().SetEntityRenderDistance(distance)

    def SetEntityUIExtraUniforms(self, entityIdentifier, uniformIndex, data):
        return self.CreateActorRender().SetEntityUIExtraUniforms(entityIdentifier, uniformIndex, data)

    def SetHealthBarDeviation(self, health_bar_deviation):
        return self.CreateHealth().SetHealthBarDeviation(health_bar_deviation)

    def SetNameDeeptest(self, deeptest):
        return self.CreateGame().SetNameDeeptest(deeptest)

    def SetNotRenderAtAll(self, notRender):
        return self.CreateActorRender().SetNotRenderAtAll(notRender)

    def SetRenderLocalPlayer(self, render):
        return self.CreateGame().SetRenderLocalPlayer(render)

    def SetShowName(self, show):
        return self.CreateName().SetShowName(show)

    def ShowHealth(self, show):
        return self.CreateHealth().ShowHealth(show)

    def ShowHealthBar(self, show):
        return self.CreateGame().ShowHealthBar(show)

    def GetEntityItem(self, posType, slotPos=0, getUserData=False):
        return self.CreateItem().GetEntityItem(posType, slotPos, getUserData)

    def GetEquItemEnchant(self, slotPos):
        return self.CreateItem().GetEquItemEnchant(slotPos)

    def GetEquItemModEnchant(self, slotPos):
        return self.CreateItem().GetEquItemModEnchant(slotPos)

    def SetEntityItem(self, posType, itemDict, slotPos=0):
        return self.CreateItem().SetEntityItem(posType, itemDict, slotPos)

    def GetAttr(self, paramName, defaultValue=None):
        return self.CreateModAttr().GetAttr(paramName, defaultValue)

    def RegisterUpdateFunc(self, paramName, func):
        return self.CreateModAttr().RegisterUpdateFunc(paramName, func)

    def SetAttr(self, paramName, paramValue, needRestore=False):
        if isinstance(self.event, ServerEvent):
            return self.CreateModAttr().SetAttr(paramName, paramValue, needRestore)
        if isinstance(self.event, ClientEvent):
            return self.CreateModAttr().SetAttr(paramName, paramValue)

    def UnRegisterUpdateFunc(self, paramName, func):
        return self.CreateModAttr().UnRegisterUpdateFunc(paramName, func)

    def CleanExtraData(self, key):
        return self.CreateExtraData().CleanExtraData(key)

    def GetExtraData(self, key):
        return self.CreateExtraData().GetExtraData(key)

    def GetWholeExtraData(self):
        return self.CreateExtraData().GetWholeExtraData()

    def SaveExtraData(self):
        return self.CreateExtraData().SaveExtraData()

    def SetExtraData(self, key, value, autoSave):
        return self.CreateExtraData().SetExtraData(key, value, autoSave)

    def Get(self, variableName):
        return self.CreateQueryVariable().Get(variableName)

    def GetMolangValue(self, molangName):
        return self.CreateQueryVariable().GetMolangValue(molangName)

    def GetStringHash64(self, key):
        return self.CreateQueryVariable().GetStringHash64(key)

    def Register(self, variableName, defalutValue):
        return self.CreateQueryVariable().Register(variableName, defalutValue)

    def Set(self, variableName, value):
        return self.CreateQueryVariable().Set(variableName, value)

    def UnRegister(self, variableName):
        return self.CreateQueryVariable().UnRegister(variableName)

    def GetSourceEntityId(self):
        return self.CreateBulletAttributes().GetSourceEntityId()

    def GetOrbExperience(self):
        return self.CreateExp().GetOrbExperience()

    def SetOrbExperience(self, exp):
        return self.CreateExp().SetOrbExperience(exp)

    def DisablePet(self):
        return self.CreatePet().Disable()

    def EnablePet(self):
        return self.CreatePet().Enable()

    def AddEntityTag(self, tag):
        return self.CreateTag().AddEntityTag(tag)

    def EntityHasTag(self, tag):
        return self.CreateTag().EntityHasTag(tag)

    def GetEntityTags(self):
        return self.CreateTag().GetEntityTags()

    def RemoveEntityTag(self, tag):
        return self.CreateTag().RemoveEntityTag(tag)

    def AddCommonPhrases(self, id, content):
        return self.CreateChatExtension().AddCommonPhrases(id, content)

    def Disable(self):
        return self.CreateChatExtension().Disable()

    def Enable(self):
        return self.CreateChatExtension().Enable()

    def RegisterChatPrefix(self, prefix, prefixColor):
        return self.CreateChatExtension().RegisterChatPrefix(prefix, prefixColor)

    def RemoveCommonPhrases(self, id):
        return self.CreateChatExtension().RemoveCommonPhrases(id)

    def SetShowOfficialPhrases(self, show):
        return self.CreateChatExtension().SetShowOfficialPhrases(show)

    def SetShowSocialNearbyInfo(self, show):
        return self.CreateChatExtension().SetShowSocialNearbyInfo(show)
