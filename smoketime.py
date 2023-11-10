from datetime import datetime, timedelta

YEAR = 2023
MONTH = 10
DAY = 31
WORKDAY_BEGIN_HOUR = 8
WORKDAY_BEGIN_MINUTES = 40
WORKDAY_END = 18
SMOKE_DURATION = 15
SMOKE_ABSTENTION = 20

if __name__ == '__main__':
    work_day_begin_time = datetime(YEAR,
                                   MONTH,
                                   DAY,
                                   WORKDAY_BEGIN_HOUR,
                                   minute=WORKDAY_BEGIN_MINUTES)
    work_day_end_time = datetime(YEAR,
                                 MONTH,
                                 DAY,
                                 WORKDAY_END,
                                 minute=0)
    smoke_times = [work_day_begin_time]                             
    total_duration = SMOKE_DURATION + SMOKE_ABSTENTION
    work_day_current_time = work_day_begin_time
    while work_day_begin_time < work_day_end_time:
        work_day_current_time += timedelta(minutes=total_duration)
        if work_day_current_time != work_day_end_time:
            smoke_times.append(work_day_current_time)
        work_day_begin_time = work_day_current_time
    all_minutes = SMOKE_DURATION * len(smoke_times) 
    print(f'Всего человек выходил курить {len(smoke_times)} раз(а)')
    print(f'Всего времени на курение {timedelta(minutes=all_minutes)} ч.')
    print()
    for idx, smoke_time in enumerate(smoke_times, start=1):
        print(f'{idx}. {datetime.strftime(smoke_time, "%H.%M")}')
