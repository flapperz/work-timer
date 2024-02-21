import datetime
import calendar

log_fname = "/Users/flap/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/work-timer-log.txt"

read_data = {
    '0' : [],
    '1' : []
}

parse_data = []

def main():
    with open(log_fname, 'r') as file:
        for line in file:
            op, timestr = line.strip().split("|")
            x = datetime.datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S%z")
            
            read_data[op].append(x)
    
    N = len(read_data['0'])       
    if N == 0:
        return 
         
    # parse read_data

    
    for start_t, stop_t in zip(read_data['1'], read_data['0']):
        
        duration = stop_t - start_t
        year = start_t.year
        month = start_t.month
        day = start_t.day
        weekday = start_t.weekday()
        
        parse_data.append(((year, month, day), weekday, duration))
    
    curr_year = None
    curr_month = None
    curr_day = None
    for ((year, month, day), weekday, duration) in parse_data:
        if year != curr_year:
            curr_year = year
            print(f"{year}:")
        if month != curr_month:
            curr_month = month
            month_name = calendar.month_name[month]
            print(f"  {month_name}:")
            curr_month == month
        if day != curr_day:
            curr_day = day
            weekday_name = calendar.day_name[weekday]
            print(f"    {weekday_name} - {day}:")
        print(f"      {duration}")
            


if __name__ == "__main__":
    main()
