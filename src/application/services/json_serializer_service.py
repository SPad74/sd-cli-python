import json

def to_dict(obj):
    if isinstance(obj, list):
        return [to_dict(item) for item in obj]
    elif hasattr(obj, "__dict__"):
        result = {}
        for key, value in obj.__dict__.items():
            if not key.startswith('_'):
                result[key] = to_dict(value)
        return result
    else:
        return obj

def to_json(obj, indent=2):
    """
    Convierte un objeto complejo en un string JSON formateado,
    usando to_dict internamente.
    """
    dict_obj = to_dict(obj)
    return json.dumps(dict_obj, indent=indent)