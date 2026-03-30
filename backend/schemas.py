from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# ================= PRODUTO =================
class ProdutoBase(BaseModel):
    nome: str
    preco: float
    estoque: int


class ProdutoCreate(ProdutoBase):
    pass


class Produto(ProdutoBase):
    id: int
    data_cadastro: datetime

    class Config:
        from_attributes = True


# ================= CLIENTE =================
class ClienteBase(BaseModel):
    nome: str
    telefone: Optional[str]
    limite_fiado: float


class ClienteCreate(ClienteBase):
    pass


class Cliente(ClienteBase):
    id: int
    divida: float
    data_cadastro: datetime

    class Config:
        from_attributes = True


# ================= ITEM VENDA =================
class ItemVendaBase(BaseModel):
    produto_id: int
    quantidade: int
    preco: float


class ItemVenda(ItemVendaBase):
    id: int
    venda_id: int

    class Config:
        from_attributes = True


# ================= VENDA =================
class Venda(BaseModel):
    cliente_id: Optional[int]
    tipo: str  # cartao ou fiado
    itens: List[ItemVendaBase]


class VendaResponse(BaseModel):
    id: int
    cliente_id: Optional[int]
    tipo: str
    total: float
    data: datetime

    class Config:
        from_attributes = True


class ItemVendaCreate(ItemVendaBase):
    pass
    data: datetime
    itens: List[ItemVenda]

    class Config:
        from_attributes = True


# ================= PAGAMENTO =================
class PagamentoCreate(BaseModel):
    cliente_id: int
    valor: float