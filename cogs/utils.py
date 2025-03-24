def get_location_string(data):
    name = data['location']['name']
    region = data['location']['region']
    country = data['location']['country']

    location_string = f"{name}, "
    if region:
        location_string += f"{region}, "
    location_string += f"{country}"

    return location_string