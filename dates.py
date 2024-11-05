import pandas as pd

weekday = {
    0.0: 'Monday',
    1.0: 'Tuesday',
    2.0: 'Wednesday',
    3.0: 'Thursday',
    4.0: 'Friday',
    5.0: 'Saturday',
    6.0: 'Sunday'
}

month = {
     1.0: 'January',
     2.0: 'February',
     3.0: 'March',
     4.0: 'Aprrl',
     5.0: 'May',
     6.0: 'June',
     7.0: 'July',
     8.0: 'August',
     9.0: 'September',
    10.0: 'October',
    11.0: 'November',
    12.0: 'December'
}

hour = {
     0.0: "00:00",
     1.0: "01:00",
     2.0: "02:00",
     3.0: "03:00",
     4.0: "04:00",
     5.0: "05:00",
     6.0: "06:00",
     7.0: "07:00",
     8.0: "08:00",
     9.0: "09:00",
    10.0: "10:00",
    11.0: "11:00",
    12.0: "12:00",
    13.0: "13:00",
    14.0: "14:00",
    15.0: "15:00",
    16.0: "16:00",
    17.0: "17:00",
    18.0: "18:00",
    19.0: "19:00",
    20.0: "20:00",
    21.0: "21:00",
    22.0: "22:00",
    23.0: "23:00"
}

year = {
    2019.0: '2019',
    2020.0: '2020',
    2021.0: '2021',
    2022.0: '2022',
    2023.0: '2023',
    2024.0: '2024',
    2025.0: '2025',
    2026.0: '2026'
}

def split_date_time_stamp(data, timestamp):
    # # convert timestamp into date/time object
    # # then make Year, Month and Day and Hour columns
    data[timestamp] = pd.to_datetime(data[timestamp])
    data[timestamp] = data[timestamp].dt.round(freq='15min')
    data['Weekday'] = data[timestamp].dt.day_name()
    data['Year'] = data[timestamp].dt.year
    data['Day of Year'] = data[timestamp].dt.day_of_year
    data['Week'] = data[timestamp].dt.isocalendar().week
    data['Month'] = data[timestamp].dt.month
    data['Hour'] = data[timestamp].dt.hour
    # data['Time'] = data[timestamp].dt.time