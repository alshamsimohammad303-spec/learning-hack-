import datetime
import pytz

# Function to display current time in different time zones
# دالة لعرض الوقت الحالي في مناطق زمنية مختلفة

def display_time():
    timezones = {
        'Egypt (Africa/Cairo)': 'Africa/Cairo',
        'Saudi Arabia (Asia/Riyadh)': 'Asia/Riyadh',
        'USA (America/New_York)': 'America/New_York',
        'London (Europe/London)': 'Europe/London',
        'Japan (Asia/Tokyo)': 'Asia/Tokyo',
        'Australia (Australia/Sydney)': 'Australia/Sydney'
    }
    
    while True:
        now = datetime.datetime.now()
        for city, tz in timezones.items():
            timezone = pytz.timezone(tz)
            current_time = datetime.datetime.now(timezone)
            print(f'{city}: {current_time.strftime("%Y-%m-%d %H:%M:%S")}')
        
        # Wait for 1 second
        # الانتظار لثانية واحدة
        time.sleep(1)

if __name__ == '__main__':
    display_time()