from pydantic import BaseModel

class PilihMonsterMusuh(BaseModel):
    id_monster:int
    id_musuh:int

class tambahMonster(BaseModel):
    nama:str

class tambahMusuh(BaseModel):
    nama:str

class cariMonster(BaseModel):
    nama:str

class makan(BaseModel):
    id_monster:int

class latihan(BaseModel):
    id_monster:int

class latihanExtra(BaseModel):
    id_monster:int

class bertarung(BaseModel):
    id_monster:int
    id_musuh:int
