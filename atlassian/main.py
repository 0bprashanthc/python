MAX_REQUESTS = 5
RATE_LIMITER_FUNCTION = 1

#requests_store is a hashmap with {customer_id: aggregated total no. of requests}
#{customerId: {timestamp:$timestamp, requests:$requests}}
requests_store = dict()

def rateLimit(customerId):
    """
    checks:
        1. customerId is valid type 'uuid'
        2. db query/cache for the customerId existence
    ratelimiting:
        1. if there is an existing valid session ( validating bearer token )
        2. {id: []} number of reqs sent till time.now()
        3. query threshold from a data store for a given customer id 2014
    """
    if customerId in requests_store:
        #YYYY-MM-DD:HH:MM:SS
        req_timestamp = get_request_timestamp(requestId)
        current_timestamp = requests_store[customerId]['timestamp']
        if get_diff(current_timestamp, req_timestamp) > RATE_LIMITER_FUNCTION:
            requests_store[customerId]['timestamp'] = time.now()
            requests_store[customerId]['requests'] = 1
        else:
            requests_store[customerId]['requests'] += 1
            current_no_of_requests = requests_store[customerId]['requests']
            if current_no_of_requests > MAX_REQUESTS:
                return False
    else:
        requests_store[customerId]['timestamp'] = time.now()
        requests_store[customerId]['requests'] = 1
    return True


if __name__ == "__main__":
    aggregated("
