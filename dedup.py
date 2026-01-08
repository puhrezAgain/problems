events = [
    {"id": "a", "value": 1},
    {"id": "b", "value": 2},
    {"id": "a", "value": 3},
]
expected = {
    "a": 1,
    "b": 2
}


def dedup(events):
    result_keys = set()
    result = {}
    for e in events:
        if e['id'] not in result_keys:
            result_keys.add(e['id'])
            result[e['id']] = e['value']
    return result

assert dedup(events) == expected