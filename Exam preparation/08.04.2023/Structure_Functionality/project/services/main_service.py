from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, 30)

    def details(self):
        if not self.robots:
            result = "none"
        else:
            result = " ".join([r.name for r in self.robots])
        return (f"{self.name} Main Service:\n"
                f"Robots: {result}")
