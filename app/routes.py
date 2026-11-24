import json
from fastapi import APIRouter, HTTPException
from app.models import Parada
from app.database import redis_client

router = APIRouter(prefix="/paradas", tags=["Paradas"])


# HU-01: Crear parada
@router.post("")
def crear_parada(parada: Parada):
    clave = f"parada:{parada.id}"
    if redis_client.exists(clave):
        raise HTTPException(status_code=409, detail="La parada ya existe")
    redis_client.set(clave, parada.model_dump_json())
    return {"mensaje": "Parada creada", "id": parada.id}


# HU-03: Listar paradas
@router.get("")
def listar_paradas():
    paradas = []
    for clave in redis_client.scan_iter(match="parada:*"):
        dato = redis_client.get(clave)
        if dato:
            paradas.append(json.loads(dato))
    paradas.sort(key=lambda p: p.get("creado_en", ""))
    return {"total": len(paradas), "paradas": paradas}


# HU-02: Obtener una parada
@router.get("/{parada_id}")
def obtener_parada(parada_id: str):
    datos = redis_client.get(f"parada:{parada_id}")
    if not datos:
        raise HTTPException(status_code=404, detail="Parada no encontrada")
    return json.loads(datos)


# HU-04: Actualizar parada
@router.put("/{parada_id}")
def actualizar_parada(parada_id: str, parada: Parada):
    clave = f"parada:{parada_id}"
    existente = redis_client.get(clave)
    if not existente:
        raise HTTPException(status_code=404, detail="Parada no encontrada")
    parada.id = parada_id
    # Se conserva la fecha de creación original
    parada.creado_en = json.loads(existente)["creado_en"]
    redis_client.set(clave, parada.model_dump_json())
    return {"mensaje": "Parada actualizada", "parada": json.loads(parada.model_dump_json())}


# HU-05: Eliminar parada
@router.delete("/{parada_id}")
def eliminar_parada(parada_id: str):
    clave = f"parada:{parada_id}"
    if not redis_client.exists(clave):
        raise HTTPException(status_code=404, detail="Parada no encontrada")
    redis_client.delete(clave)
    return {"mensaje": "Parada eliminada", "id": parada_id}