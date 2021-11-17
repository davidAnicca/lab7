from repo.event_repo import EventRepo
from repo.sale_repo import SaleRepo


def int_20_p(value):
    return int((20 * value) / 100) + 1


def sec(el):
    return el[1]


class EventLogic(object):
    def __init__(self, event_repo: EventRepo, sale_repo: SaleRepo):
        self.__sale_repo = sale_repo
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

    def get_first_20_p_with_participants(self):
        """
        finds first 20% of events with a big number of participants
        :return: a list of events
        """
        events_w_participants = []
        events = self.__event_repo.get_all()
        sales = self.__sale_repo.get_all()
        for event in events:
            participants = 0
            for sale in sales:
                if sale.get_event() == event:
                    participants += 1
            events_w_participants.append((event, participants))
        events_w_participants.sort(reverse=True, key=sec)
        first_events = []
        for events_w_participant in events_w_participants:
            first_events.append(events_w_participant[0])
        return first_events[0:int_20_p(len(first_events))]
