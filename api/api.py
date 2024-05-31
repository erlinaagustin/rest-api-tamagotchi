from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import app
from utils import get_async_session, respOutCustom
from schema import PilihMonsterMusuh, tambahMonster, tambahMusuh, cariMonster, makan, latihan, latihanExtra, bertarung

router = APIRouter()

@router.post("/pilih-monster-musuh/")
async def pilihMonsterMusuhRouter(
    request:PilihMonsterMusuh,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await app.pilihMonsterMusuh(request, db)
    if err != None:
        return respOutCustom("02", f"registration failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)

@router.post("/tambah-monster/")
async def tambahMonsterRouter(
    request:tambahMonster,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await app.tambahDataMonster(request, db)
    if err != None:
        return respOutCustom("02", f"registration failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)

@router.post("/tambah-musuh/")
async def tambahMusuhRouter(
    request:tambahMusuh,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await app.tambahDataMusuh(request, db)
    if err != None:
        return respOutCustom("02", f"registration failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)

@router.get("/lihat-data-monster/")
async def lihatMonsterRouter(
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await app.lihatMonster(db)
    if err !=None:
        return respOutCustom("02", f"registration failed: {err}", None)
    return respOutCustom("00", "success", outResponse)

@router.post("/cari-data-monster/")
async def cariMonsterRouter(
    request:cariMonster,
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await app.cariMonster(request, db)
    if err != None:
        return respOutCustom("02", f"registration failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)

@router.post("/monster-makan/")
async def monsterMakanRouter(
    request:makan,
    db:AsyncSession = Depends(get_async_session)
):
    outResponse, err = await app.monsterMakan(request, db)
    if err != None:
        return respOutCustom("02", f"registration failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)

@router.post("/monster-latihan/")
async def monsterLatihanRouter(
    request:latihan,
    db:AsyncSession = Depends(get_async_session)
):
    outResponse, err = await app.monsterLatihan(request, db)
    if err != None:
        return respOutCustom("02", f"registration failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)

@router.post("/monster-latihan-extra/")
async def monsterLatihanExtraRouter(
    request:latihanExtra,
    db:AsyncSession = Depends(get_async_session)
):
    outResponse, err = await app.monsterLatihanExtra(request, db)
    if err != None:
        return respOutCustom("02", f"registration failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)

@router.post("/monster-bertarung/")
async def monsterbertarungRouter(
    request:bertarung,
    db:AsyncSession = Depends(get_async_session)
):
    outResponse, err = await app.gameBertarung(request, db)
    if err != None:
        return respOutCustom("02", f"registration failed: {err}", None)
    
    return respOutCustom("00", "success", outResponse)


@router.get("/lihat-data-riwayat/")
async def lihatRiwayatRouter(
    db: AsyncSession = Depends(get_async_session)
):
    outResponse, err = await app.lihatRiwayat(db)
    if err !=None:
        return respOutCustom("02", f"registration failed: {err}", None)
    return respOutCustom("00", "success", outResponse)
