"""
Functions relating to transforming data returned by the APIs
"""


###############################################################################
# FUNCTIONS
###############################################################################
def find_moon_phase(value: float) -> str:
    """
    Converts the numerical value of the moon phase provided by the API to a
    descriptive phrase.
    """
    if value == 0.00:
        return 'New moon'
    elif 0.00 < value < 0.25:
        return 'Waxing crescent'
    elif value == 0.25:
        return 'First quarter'
    elif 0.25 < value < 0.5:
        return 'Waxing gibbous'
    elif value == 0.5:
        return 'Full moon'
    elif 0.5 < value < 0.75:
        return 'Waning gibbous'
    elif value == 0.75:
        return 'Last quarter'
    elif 0.75 < value <= 1.0:
        return 'Waning Crescent'
    else:
        return 'Moon phase out of scope'


def find_how_cloudy(cloud_cover: float) -> str:
    """
    Takes the percentage cloud cover and returns an assessment of stargazing
    feasibility using boolean values.
    """
    if 0.0 <= cloud_cover < 10.0:
        return 'There are very few clouds. Perfect for for stargazing!'
    elif 10.0 <= cloud_cover < 30.0:
        return 'There are some clouds, so only moderately good stargazing.'
    else:
        return 'It is too cloudy for good stargazing.'
