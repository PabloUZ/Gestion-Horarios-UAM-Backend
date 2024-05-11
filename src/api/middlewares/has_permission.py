from fastapi import Depends, HTTPException
from src.api.middlewares.has_access import has_access


class HasPermission:
    def __init__(self, name: str):
        self.name = name
    def __call__(self, payload = Depends(has_access)):
        try:
            if self.name not in payload['role']['permissions']:
                raise HTTPException(status_code=403, detail="Forbidden")
            return payload
        except:
            raise HTTPException(status_code=403, detail="Forbidden")