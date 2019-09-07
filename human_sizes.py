def approx_size(size, a_kilobyte_is_1024_bytes=True):
    if size < 0: 
        raise ValueError('number must be non-negative')
    
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    
    for suffix in SUFFIXES[multiple]:
        size