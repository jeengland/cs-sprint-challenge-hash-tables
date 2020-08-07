class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    nodes = {}
    start = None
    for ticket in tickets:
        if ticket.source == 'NONE':
            start = ticket.destination
        else:
            nodes[ticket.source] = ticket.destination
    route = [start]
    while True:
        origin = route[-1]
        if origin == 'NONE':
            break
        route.append(nodes[origin])
    return route
