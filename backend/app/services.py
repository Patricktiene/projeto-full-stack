from app.database import get_summary, list_demands


def normalize_status(status: str) -> str:
    value = status.strip().lower()

    valid_status = [
        "pendente",
        "em andamento",
        "concluída",
    ]

    if value not in valid_status:
        return "pendente"

    return value


def build_summary():
    return get_summary()


def list_all_demands():
    return list_demands()


def convert_event_to_demand(event):
    return {
        "title": "Verificar evento escolar",
        "category": event["type"],
        "description": f"Evento recebido de {event['source']}",
        "status": "pendente",
        "owner": "Sistema",
        "created_at": event["created_at"],
    }