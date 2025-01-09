
def has_overlap(visit_a: dict, visit_b: dict) -> bool:
    """
    Checks whether two visits overlap in time, considering date and time slots.
    """
    date_a = visit_a["date"]
    date_b = visit_b["date"]
    if date_a != date_b:
        return False
    
    start_a = visit_a["time"]["startSlot"]
    end_a   = visit_a["time"]["endSlot"]
    start_b = visit_b["time"]["startSlot"]
    end_b   = visit_b["time"]["endSlot"]

    # Two intervals [start_a, end_a] and [start_b, end_b] overlap if:
    # start_a < end_b and start_b < end_a
    # return not (end_a < start_b or end_b < start_a)
    return (start_a < end_b) and (start_b < end_a)


def getOverlappedVisits(list_of_visits: list) -> list:
    """
    Groups visits that overlap into a single object containing:
      - visits (array of names)
      - time (startSlot, endSlot)
    Skips any group containing exactly one visit.
    """

    # 1) Sort by date, then startSlot, then endSlot
    sorted_visits = sorted(
        list_of_visits,
        key=lambda x: (x["date"], x["time"]["startSlot"], x["time"]["endSlot"])
    )

    result = []
    n = len(sorted_visits)
    i = 0

    # 2) Iterate over sorted visits with a while-loop
    while i < n:
        current = sorted_visits[i]
        # Initialize a new group with the current visit
        group_visits = [current]
        
        # We'll track the merged time range as we add more overlaps
        group_date      = current["date"]
        group_startSlot = current["time"]["startSlot"]
        group_endSlot   = current["time"]["endSlot"]
        
        j = i + 1
        # 3) "Pull in" any subsequent visits that overlap
        while j < n and has_overlap(sorted_visits[j - 1], sorted_visits[j]):
            # Also ensure they’re on the same date
            if sorted_visits[j]["date"] != group_date:
                break
            
            # If they overlap, add them to the group
            group_visits.append(sorted_visits[j])
            # Extend the endSlot if needed
            group_endSlot = max(group_endSlot, sorted_visits[j]["time"]["endSlot"])
            j += 1

        # Now we have a group from i..(j-1). 
        # 4) Only add if there's more than 1 visit
        if len(group_visits) > 1:
            result.append({
                "visits": [v["name"] for v in group_visits],
                "time": {
                    "startSlot": group_startSlot,
                    "endSlot": group_endSlot
                }
            })
        
        # Move i forward to j
        i = j

    return result


list_of_visits =  [
    {
    "name":"visit02",
    "date": "2024-11-13",
    "time": {
        "startSlot": 5,
        "endSlot": 8
        }
    },
    {
    "name":"visit01",
    "date": "2024-11-13",
    "time": {
        "startSlot": 5,
        "endSlot": 7
        }
    },
    {
    "name":"visit03",
    "date": "2024-11-13",
    "time": {
        "startSlot": 9,
        "endSlot": 10
        }
    },
    {
    "name":"visit04",
    "date": "2024-11-13",
    "time": {
        "startSlot": 6,
        "endSlot": 9
        }
    }
]
result = getOverlappedVisits(list_of_visits)
print(result)
