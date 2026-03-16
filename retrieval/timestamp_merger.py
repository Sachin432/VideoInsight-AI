def merge_timestamps(timestamps, gap=2):

    timestamps = sorted(timestamps)

    merged = []

    start = timestamps[0]
    prev = timestamps[0]

    for t in timestamps[1:]:

        if t - prev <= gap:

            prev = t

        else:

            merged.append((start, prev))

            start = t
            prev = t

    merged.append((start, prev))

    return merged