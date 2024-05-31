from schema import PilihMonsterMusuh, tambahMonster, tambahMusuh, cariMonster, makan, latihan, latihanExtra, bertarung
from model import Monsters, Musuhs, Riwayats
from sqlalchemy import select,  update
import datetime

async def pilihMonsterMusuh(data:PilihMonsterMusuh, session):
    try:
        # Query for the monster
        query_monster = select(Monsters).where(Monsters.id == data.id_monster)
        result_monster = await session.execute(query_monster)
        monster = result_monster.scalar_one_or_none()
        
        # Query for the musuh
        query_musuh = select(Musuhs).where(Musuhs.id == data.id_monster)
        result_musuh = await session.execute(query_musuh)
        musuh = result_musuh.scalar_one_or_none()
        
        return {
            "monster": monster,
            "musuh": musuh
        }, None
    except Exception as e:
        return None, e
    
async def tambahDataMonster(data:tambahMonster, session):
    try:
        paramsInsert = Monsters(
            nama = data.nama,
            power = 0,
            strength = 0,
            stamina = 0
            )

        session.add(paramsInsert)
        return data, None
    
    except Exception as e:
        return None, e

async def tambahDataMusuh(data:tambahMusuh, session):
    try:
        paramsInsert = Musuhs(
            nama = data.nama,
            power = 1000,
            strength = 10000,
            stamina = 2000
            )

        session.add(paramsInsert)
        return data, None
    
    except Exception as e:
        return None, e

async def lihatMonster(session):
    try:
        query = select(Monsters)
        result = await session.execute(query)
        monster = result.scalars().all()

        return {"monster":monster}, None
    except Exception as e:
        return None, e
    
async def cariDataMonster(data:cariMonster, session):
    try:
        query = select(Monsters).where(Monsters.nama.ilike(f"%{data.nama}%"))
        result = await session.execute(query)
        monster = result.scalars().all()

        return {"monster":monster}, None
    except Exception as e:
        return None, e
    
async def monsterMakan(data:makan, session):
    try:
        query = update(Monsters).where(Monsters.id == data.id_monster).values(
            power = Monsters.power+10, 
            strength = Monsters.strength+50, 
            stamina = Monsters.stamina+50)
        
        await session.execute(query)
        await session.commit()
        return data, None
    except Exception as e:
        return None, e
    
async def monsterLatihan(data:latihan, session):
    try:
        query = update(Monsters).where(Monsters.id == data.id_monster).values(
            power = Monsters.power*2, 
            strength = Monsters.strength*2, 
            stamina = Monsters.stamina-20)
        
        await session.execute(query)
        await session.commit()
        return data, None
    except Exception as e:
        return None, e
    

async def monsterLatihanExtra(data:latihanExtra, session):
    try:
        query = update(Monsters).where(Monsters.id == data.id_monster).values(
            power = Monsters.power*3, 
            strength = Monsters.strength*3, 
            stamina = Monsters.stamina+200)
        
        await session.execute(query)
        await session.commit()
        return data, None
    except Exception as e:
        return None, e
    
async def monsterBertarung(data: bertarung, session):
    try:
        query_monster = update(Monsters).where(Monsters.id == data.id_monster).values(
            stamina = Monsters.stamina - 100
        )
        await session.execute(query_monster)
        
        query_musuh = update(Musuhs).where(Musuhs.id == data.id_musuh).values(
            stamina = Musuhs.stamina - 100
        )
        await session.execute(query_musuh)

        # Mengambil data terbaru setelah update
        monster = await session.get(Monsters, data.id_monster)
        musuh = await session.get(Musuhs, data.id_musuh)
        
        totalMonster = monster.power + monster.stamina
        totalMusuh = musuh.power + musuh.stamina
        
        if totalMonster > totalMusuh:
            pemenang = "monster"
        else:
            pemenang = "musuh"

        paramsInsert = Riwayats(
            idMusuh=data.id_musuh,
            idMonster=data.id_monster,
            tanggal = datetime.datetime.now(),
            totalPowerMusuh=totalMusuh,
            totalPowerMonster=totalMonster,
            pemenang=pemenang
        )
        session.add(paramsInsert)

        return data, None

    except Exception as e:
        return None, e

async def lihatRiwayat(session):
    try:
        stmt = select(Riwayats)
        result = await session.execute(stmt)
        riwayats = result.scalars().all()

        return {"riwayat": riwayats}, None
    except Exception as e:
        return None, e
        
  

        
    
    
