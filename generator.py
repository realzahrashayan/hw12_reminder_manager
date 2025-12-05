def id_generator(start = 1):
    first = start

    while True:
        yield first
        first+=1
 
id = id_generator(start=1)

def get_next_id():
    return next(id)