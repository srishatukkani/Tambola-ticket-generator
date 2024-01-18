import random
from tambola_ticket import TambolaTicket
import datetime

def get_unique_set_id():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    return timestamp

def numofelement(arr):
    total_elements = 0
    for row in arr:
        total_elements += len(row)

    return total_elements

def rowcount(row):
    ans = 0
    for i in row:
        if i:
            ans += 1
    return ans

def generate_tambola_ticket_set():
    col_vals = [[10*y + x for x in range(10)] for y in range(9)]
    col_vals[0].pop(0)
    col_vals[-1].append(90)

    all_tics = [[[] for _ in range(9)] for _ in range(6)]

    for i in range(9):
        col = col_vals[i]
        for j in range(6):
            random_index = random.randrange(len(col))
            all_tics[j][i].append(col.pop(random_index))

    random_index = random.randrange(len(col_vals[8]))
    all_tics[random.randrange(6)][8].append(col_vals[8].pop(random_index))

    for i in range(3):
        for j in range(9):
            col = col_vals[j]
            if not len(col):
                continue
            random_index = random.randrange(len(col))
            random_number = col[random_index]

            found = 1
            while found:
                tic = all_tics[random.randrange(6)]

                if numofelement(tic) != 15 and len(tic[j]) != 2:
                    found = 0
                    tic[j].append(random_number)
                    col.pop(random_index)

    for j in range(9):
        col = col_vals[j]
        if not len(col):
            continue
        random_index = random.randrange(len(col))
        random_number = col[random_index]

        found = 1
        while found:
            tic = all_tics[random.randrange(6)]

            if numofelement(tic) != 15 and len(tic[j]) != 3:
                found = 0
                tic[j].append(random_number)
                col.pop(random_index)

    for i in range(6):
        for j in range(9):
            all_tics[i][j].sort()

    final_tickets = [[[0] * 9 for _ in range(3)] for _ in range(6)]
    for i in range(6):
        current = all_tics[i]
        for col_size in range(3,0,-1):
            if rowcount(final_tickets[i][0]) == 5:
                break
            for j in range(9):
                if rowcount(final_tickets[i][0]) == 5:
                    break
                if final_tickets[i][0][j] != 0:
                    continue
                if len(current[j]) != col_size:
                    continue
                final_tickets[i][0][j] = current[j].pop(0)
        for col_size in range(2,0,-1):
            if rowcount(final_tickets[i][1]) == 5:
                break
            for j in range(9):
                if rowcount(final_tickets[i][1]) == 5:
                    break

                if final_tickets[i][1][j] != 0:
                    continue
                if len(current[j]) != col_size:
                    continue
                final_tickets[i][1][j] = current[j].pop(0)
        for col_size in range(1,0,-1):
            if rowcount(final_tickets[i][2]) == 5:
                break
            for j in range(9):
                if rowcount(final_tickets[i][2]) == 5:
                    break

                if final_tickets[i][2][j] != 0:
                    continue
                if len(current[j]) != col_size:
                    continue
                final_tickets[i][2][j] = current[j].pop(0)
    # print(col_vals)
    # print(all_tics)
    # print(final_tickets)

    for ticket in final_tickets:
        for row in ticket:
            print(row)
        print("  ")

    print("-------------------------")
                
    for ticket in final_tickets:
        if TambolaTicket.select().where(
            TambolaTicket.row1 == str(ticket[0]),
            TambolaTicket.row2 == str(ticket[1]),
            TambolaTicket.row3 == str(ticket[2]),
        ).exists():
            return generate_tambola_ticket_set()

    set_id = get_unique_set_id()
    generated_tickets = {}
    print(type(set_id))
    for i, ticket in enumerate(final_tickets):
        params = {
            # "id": uuid.uuid4(),
            "set_id": str(set_id),
            "ticket_number": i + 1,
            "row1": str(ticket[0]),
            "row2": str(ticket[1]),
            "row3": str(ticket[2]),
        }
        tambola_object = TambolaTicket(**params)
        tambola_object.save()
        generated_tickets[str(tambola_object.id)] = ticket

    return generated_tickets