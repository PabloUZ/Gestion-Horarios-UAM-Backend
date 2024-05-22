from fastapi import Depends, HTTPException
from src.api.middlewares.has_access import has_access


class HasPermission:
    def __init__(self, name: str, allow_own = False):
        self.name = name
        self.allow_own = allow_own
    def __call__(self, data = Depends(has_access)):
        try:
            print(data)
            if data['payload']['role'] is not None and self.name not in data['payload']['role']['permissions']:
                if not self.allow_own:
                    raise HTTPException(status_code=403, detail="Forbidden")
                elif data['req'].path_params['cc'] != data['payload']['cc']:
                    raise HTTPException(status_code=403, detail="Forbidden")
            elif data['payload']['role'] is None:
                if not self.allow_own:
                    raise HTTPException(status_code=403, detail="Forbidden")
                elif data['req'].path_params['cc'] != data['payload']['cc']:
                    raise HTTPException(status_code=403, detail="Forbidden")
            return data['payload']
        except:
            print(7)
            raise HTTPException(status_code=403, detail="Forbidden")