from rest_framework.throttling import UserRateThrottle


class ThreeCallsPerMinute(UserRateThrottle):
    '''
    Custom Throttle, 
    make sure add scope name in setting DEFAULT_THROTTLE_RATES
    '''
    scope = 'three'
