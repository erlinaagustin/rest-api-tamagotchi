from sqlalchemy import(
  Column, String, Integer, Date, ForeignKey
)
from sqlalchemy.orm import relationship

from utils import Base

class Monsters(Base):
    __tablename__ = "monsters"
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    power = Column(Integer)
    strength = Column(Integer)
    stamina = Column(Integer)
    riwayats = relationship("Riwayats", back_populates="monster")  

class Musuhs(Base):
    __tablename__ = "musuhs"
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    power = Column(Integer)
    strength = Column(Integer)
    stamina = Column(Integer)
    riwayats = relationship("Riwayats", back_populates="musuh")  

class Riwayats(Base):
    __tablename__ = "riwayats"
    
    id = Column(Integer, primary_key=True, index=True)
    tanggal = Column(Date)
    idMusuh = Column(Integer, ForeignKey('musuhs.id'))
    idMonster = Column(Integer, ForeignKey('monsters.id'))
    totalPowerMusuh = Column(Integer)
    totalPowerMonster = Column(Integer)
    pemenang = Column(String)

    musuh = relationship("Musuhs", back_populates="riwayats")  
    monster = relationship("Monsters", back_populates="riwayats")  
