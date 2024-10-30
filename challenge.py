def overlap_time(hour: int) -> str:
    
    # Generates all data across all hours
    def calculate_overlap():
        for h in range(12):  # Corrected range to cover 0-11
            m = (h % 12) * 30 / 5.5  # Calculates the minutes angle
            if m < 60:  # Ensure the minute is within range
                yield h, int(m), int((m - int(m)) * 60)

    # Filters out all hours where there is no overlap
    for h, m, s in calculate_overlap():
        if h == hour:
            return f"{h}:{m:02d}:{s:02d}"
    
    return None  # Return None if no overlap is found for the given hour

# Print the final result for each hour
for i in range(12):
    result = overlap_time(i)
    if result:
        print(result)
