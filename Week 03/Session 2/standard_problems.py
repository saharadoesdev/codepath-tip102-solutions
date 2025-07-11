def process_performance_requests(requests):
    order = []

    d = {}
    for r in requests:
        d[r[0]] = r[1]


    for i in range(len(d)):
        temp = max(d.keys())
        order.append(d[temp])
        d.pop(temp)
    
    return order




print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))