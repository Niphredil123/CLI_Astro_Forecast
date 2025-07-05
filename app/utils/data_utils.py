"""
Functions relating to transforming data returned by the APIs
"""
###############################################################################
# FUNCTIONS
###############################################################################
def find_moon_phase(value: float) -> str:
    """
    Converts the numerical value of the moon phase to a descriptive phrase
    using a list of tuples. Each tuple contains a boolean lambda check and a
    moon phase label.
    """
    conditions = [
        (lambda v: v == 0.00, 'New moon'),
        (lambda v: 0.00 < v < 0.25, 'Waxing crescent'),
        (lambda v: v == 0.25, 'First quarter'),
        (lambda v: 0.25 < v < 0.5, 'Waxing gibbous'),
        (lambda v: v == 0.5, 'Full moon'),
        (lambda v: 0.5 < v < 0.75, 'Waning gibbous'),
        (lambda v: v == 0.75, 'Last quarter'),
        (lambda v: 0.75 < v <= 1.0, 'Waning Crescent'),
    ]

    for check, label in conditions:
        if check(value):
            return label

    return 'Moon phase not found'


def find_how_cloudy(cloud_cover: float) -> str:
    """
    Takes the percentage cloud cover and returns an assessment of stargazing
    feasibility using boolean values.
    """
    if 0.0 <= cloud_cover < 10.0:
        return 'There are very few clouds. Perfect for for stargazing!'
    if 10.0 <= cloud_cover < 30.0:
        return 'There are some clouds, so only moderately good stargazing.'
    return 'It is too cloudy for good stargazing.'
