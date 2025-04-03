def spring_equinox():
    details = ['Spring', 'Equinox', 3.20, 2025]
    #list using strings, float, and integer
    season = details[0]
    event = details[1]
    day = details[2]
    year = details[3]
    print(f'Welcome to the {season} {event} on {day:.2f}.{year}!')
    print(f'Types: {type(season)}, {type(event)}, {type(day)}, {type(year)}')
spring_equinox()
#Learn: lists can mix types (strings, float, int)