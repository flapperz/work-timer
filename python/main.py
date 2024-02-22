import datetime
# import calendar
import argparse

log_fname = "/Users/flap/Library/Mobile Documents/iCloud~is~workflow~my~workflows/Documents/work-timer-log.txt"


weekday_abbr_map = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

TODAY_BANNER = \
'''-----
TODAY
-----
'''

def read_data(fname):
    raw_data = {
    '0' : [],
    '1' : []
    }
    
    with open(fname, 'r') as file:
        for line in file:
            op, timestr = line.strip().split("|")
            x = datetime.datetime.strptime(timestr, "%Y-%m-%dT%H:%M:%S%z")
            raw_data[op].append(x)
            
    return raw_data
        

def parse_data(data):
    parse_data = dict()
    for start_t, stop_t in zip(data['1'], data['0']):
            
            duration = stop_t - start_t
            year = start_t.year
            month = start_t.month
            day = start_t.day
            weekday = start_t.weekday()
            
            # parse_data.append(((year, month, day), weekday, duration))
            key = (year, month, day)
            if key not in parse_data:
                parse_data[key] = {
                    'weekday'   : weekday,
                    'durations' : [],
                    'startdts'  : []
                }
            parse_data[key]['durations'].append(duration)
            parse_data[key]['startdts'].append(start_t)
    return parse_data

def format_timedelta(td):
    return ':'.join([f"{int(s):02}" for s in str(td).split(':')[:2]])

def generate_report(data, today_ymd, is_verbose):
    
    outstr = ""
    
    
    for ymd, v in data.items():
        
        if not is_verbose and ymd != today_ymd:
            continue
            
        y,m,d = ymd
        weekday = v['weekday']
        weekday_abbr = weekday_abbr_map[weekday]
        durations = v['durations']
        sum_durations = sum(durations, datetime.timedelta())
        sum_durations_format = format_timedelta(sum_durations)
        
        dayheader = f"{weekday_abbr} {d:02}-{m:02}-{y:04}:"
        
        if ymd != today_ymd:
            outstr += f"{dayheader} {sum_durations_format}\n"
        else:
            outstr += TODAY_BANNER
            outstr += f"{dayheader} {sum_durations_format} - sum\n"
                
            for i, duration in enumerate(durations):
                duration_format = format_timedelta(duration)
                outstr += f"{' '*len(dayheader)} {duration_format} - session {i+1}\n"
            
            
    outstr = outstr.strip()
    return outstr
    


def get_today_ymd():
    date_time_now = datetime.datetime.now()
    today_y = date_time_now.year
    today_m = date_time_now.month
    today_d = date_time_now.day
    # print(date_time_now.timetuple())
    
    return (today_y, today_m, today_d) 


def main(args):
    
    is_verbose = args.verbose
    
    raw_data = read_data(log_fname)
    
    day_entries_map = parse_data(raw_data)
    
    today_ymd = get_today_ymd()
    
    report = generate_report(day_entries_map, today_ymd, is_verbose)
    
    print(report)
            


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Work Timer Analysis')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    
    main(args)