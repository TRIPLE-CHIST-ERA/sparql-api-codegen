"""Example class."""

from typing import Optional

from sparql_void_to_python.settings import Settings, log


def generate_code_for_endpoint(endpoint: str) -> None:
    print("Querying the endpoint", endpoint)
    # TODO: create file


# TODO: This is a placeholder, to be removed
class Api:
    def __init__(self, settings: Optional[Settings] = None) -> None:
        self.settings = settings if settings else Settings()
        log.info(self.settings)

    def hello_world(self, label: Optional[str] = None) -> str:
        label = label if label else self.settings.greet
        out = ""
        for i in range(self.settings.many_times):
            out += f"[{i}] Hello {label} "
        return out
