from fastapi import Path

class IdParam:
    def __init__(self, id: int = Path(..., gt=0)):
        self.id = id

