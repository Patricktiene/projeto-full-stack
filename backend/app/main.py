from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.database import (
    init_db,
    list_demands,
    get_demand_by_id,
    create_demand,
    update_demand,
    delete_demand,
    create_event,
    list_events,
)

from app.schemas import (
    DemandCreate,
    DemandUpdate,
    EventCreate,
)

from app.services import (
    build_summary,
    normalize_status,
    convert_event_to_demand,
)


app = FastAPI(
    title="Central Escolar API",
    description="Sistema de controle de demandas e eventos escolares",
    version="3.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/demands")
def get_demands():
    return {
        "demands": list_demands()
    }


@app.get("/summary")
def get_summary_route():
    return build_summary()


@app.get("/events")
def get_events():
    return {
        "events": list_events()
    }


@app.post("/demands")
def create_demand_route(demand: DemandCreate):

    new_demand = create_demand(
        title=demand.title,
        category=demand.category,
        description=demand.description,
        status=normalize_status(demand.status),
        owner=demand.owner,
        created_at=demand.created_at,
    )

    return {
        "message": "Demanda criada com sucesso.",
        "demand": new_demand,
    }


@app.post("/event")
def receive_event(event: EventCreate):

    new_event = create_event(
        source=event.source,
        type=event.type,
        value=event.value,
        created_at=event.created_at,
    )

    demand_data = convert_event_to_demand(
        {
            "source": event.source,
            "type": event.type,
            "value": event.value,
            "created_at": event.created_at,
        }
    )

    create_demand(
        title=demand_data["title"],
        category=demand_data["category"],
        description=demand_data["description"],
        status=demand_data["status"],
        owner=demand_data["owner"],
        created_at=demand_data["created_at"],
    )

    return {
        "message": "Evento recebido e demanda criada.",
        "event": new_event,
    }


@app.put("/demands/{demand_id}")
def update_demand_route(
    demand_id: int,
    demand: DemandUpdate,
):

    existing = get_demand_by_id(demand_id)

    if not existing:
        raise HTTPException(
            status_code=404,
            detail="Demanda não encontrada.",
        )

    updated = update_demand(
        demand_id=demand_id,
        title=demand.title,
        category=demand.category,
        description=demand.description,
        status=normalize_status(demand.status),
        owner=demand.owner,
        created_at=demand.created_at,
    )

    return {
        "message": "Demanda atualizada com sucesso.",
        "demand": updated,
    }


@app.delete("/demands/{demand_id}")
def delete_demand_route(demand_id: int):

    existing = get_demand_by_id(demand_id)

    if not existing:
        raise HTTPException(
            status_code=404,
            detail="Demanda não encontrada.",
        )

    delete_demand(demand_id)

    return {
        "message": "Demanda removida com sucesso."
    }