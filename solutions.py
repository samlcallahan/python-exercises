def extract_time_components(timestring):
    components = {'hours':0,'minutes':0,'seconds':0}
    components['hours'] = int(timestring[:2])
    components['minutes'] = int(timestring[3:5])
    components['seconds'] = int(timestring[-2:])
    return components