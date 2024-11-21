from src.core.domain.enums.event_type import EventType
from src.core.domain.service.base.base import BaseService
from src.core.util.logger.logger import Logger
from src.core.util.observer.event import Event


class LogService(BaseService):

    def log_http_request(self, request):
        Logger.info(f"Request: {request}", {"location": "log_service"})

    def handle_event(self, event: Event):
        super().handle_event(event)

        if event.type == EventType.CHANGE_NOMENCLATURE:
            Logger.info(f"Change nomenclature: {event.payload.id}", {"location": "log_service"})

        if event.type == EventType.DUMP_DATA:
            Logger.info(f"Dump data", {"location": "log_service"})

        if event.type == EventType.CHANGE_BLOCK_DATE:
            Logger.info(f"Change block date: {event.payload}", {"location": "log_service"})

        if event.type == EventType.GOT_HTTP_REQUEST:
            self.log_http_request(event.payload)