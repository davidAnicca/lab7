from repo.event_repo import EventRepo


class EventLogic(object):
    def __init__(self, event_repo: EventRepo):
        self.__event_repo = event_repo

    def get_event_with_max_duration(self):
        events = self.__event_repo.get_all()
        if len(events) == 0:
            return None
        max_duration = events[0].get_duration()
        event_w_max_duration = events[0]
        for event in events:
            if event.get_duration() > max_duration:
                max_duration = event.get_duration()
                event_w_max_duration = event
        return event_w_max_duration