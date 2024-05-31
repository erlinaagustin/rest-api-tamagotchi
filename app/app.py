import datastore
from sqlalchemy.ext.asyncio import AsyncSession
from schema import PilihMonsterMusuh, tambahMonster, tambahMusuh, cariMonster, makan, latihan, latihanExtra, bertarung


async def pilihMonsterMusuh(data:PilihMonsterMusuh, db:AsyncSession):
    async with db as session:
        try:
            if data.id_monster == "" and data.id_musuh =="":
                raise Exception(f"id harus diisi")
            res, err = await datastore.pilihMonsterMusuh(data, session)
            if err != None:
                raise Exception(err)
            await session.commit()

            return res, None
        
        except Exception as e:
            return None, e

async def tambahDataMonster(data:tambahMonster, db:AsyncSession):
    async with db as session:
        try:
            if data.nama == "":
                raise Exception(f"nama harus diisi")
            res, err = await datastore.tambahDataMonster(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
            
        except Exception as e:
            return None, e
        
async def tambahDataMusuh(data:tambahMusuh, db:AsyncSession):
    async with db as session:
        try:
            if data.nama=="":
                raise Exception(f"nama harus diisi")
            res, err = await datastore.tambahDataMusuh(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
            
        except Exception as e:
            return None, e
        
async def lihatMonster(db:AsyncSession):
    async with db as session:
        try:
            res, err = await datastore.lihatMonster(session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
        
        except Exception as e:
            return None, e
        
async def cariMonster(data:cariMonster, db:AsyncSession):
    async with db as session:
        try:
            if data.nama=="":
                raise Exception(f"nama harus diisi")
            res, err = await datastore.cariDataMonster(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
            
        except Exception as e:
            return None, e
        
async def monsterMakan(data:makan, db:AsyncSession):
    async with db as session:
        try:
            if data.id_monster=="":
                raise Exception(f"id harus diisi")
            res, err = await datastore.monsterMakan(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
        
        except Exception as e:
            return None, e

async def monsterLatihan(data:latihan, db:AsyncSession):
    async with db as session:
        try:
            if data.id_monster=="":
                raise Exception(f"id harus diisi")
            res, err = await datastore.monsterLatihan(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
        
        except Exception as e:
            return None, e
        
async def monsterLatihanExtra(data:latihanExtra, db:AsyncSession):
    async with db as session:
        try:
            if data.id_monster=="":
                raise Exception(f"id harus diisi")
            res, err = await datastore.monsterLatihanExtra(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
        
        except Exception as e:
            return None, e
        

async def gameBertarung(data:bertarung, db:AsyncSession):
    async with db as session:
        try:
            if data.id_monster=="" and data.id_musuh=="":
                raise Exception(f"id harus diisi")
            res, err = await datastore.monsterBertarung(data, session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
        
        except Exception as e:
            return None, e
        

async def lihatRiwayat(db:AsyncSession):
    async with db as session:
        try:
            res, err = await datastore.lihatRiwayat(session)
            if err !=None:
                raise Exception(err)
            await session.commit()
            return res, None
        
        except Exception as e:
            return None, e
        