from .models import Reservation


def check_availability(table, time_start, time_end):
    """
    to check if a table number for a specific number of
    persons is available within the start and end time
    """
    avail_list = []
    reservation_list = Reservation.objects.filter(table=table)
    for reservation in reservation_list:
        if (reservation.time_start > time_end or
                reservation.time_end < time_start):
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
