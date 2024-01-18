from tambola_ticket import TambolaTicket

def get_all_tambola_tickets(page = 1, page_limit = 5):
    data = list(TambolaTicket.select().order_by(TambolaTicket.set_id, TambolaTicket.ticket_number).dicts())
    # print(data)
    return data