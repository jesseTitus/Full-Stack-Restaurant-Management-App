from rest_framework.throttling import UserRateThrottle

#creates new throttle policy, used in settings.py to establish limit
class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten'