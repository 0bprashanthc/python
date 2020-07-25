##
Features:
1. POST array of urls
2. GET on job status
3. GET on job result

Usecases:
1. [url1,url2,url3] POST
   - jobid 
2. GET jobid
   - JSON blob
3. GET jobresult
   - JSON blob {url:[images]}

Store:
1. url:
   - id (10 bytes)
   - dns ( weburl )
   - status ( visited true ? false )
   - images 
2. user/client
   - id
   - session bearer tokenk ( jwt ) 
   - geographic location
   - timestamp of the API calls ( rate limiting systems )
3. jobs:
   - id
   - urls[]
   - status (completed?in-progress)
   
High Level Design:
   Client
    INTERNET
  LOAD BALANCERS

  APP SERVERS --------------> [ job queue ]
                                   workers cluster
      Distributed Cache
  Distributed Database systems
Data analysis

nosql:
- key value ( amazon s3, dyanamo db)
 {url: {[images]}}
- indexing
- load, data
- eventual consistency
sql: 
- (relational) consistency
- scaling horizontally
- sharding costly

Low Level Design:
  Scheduling Algorithms:
     1. Weighted Round Robin
     2. Server load/capacity
     3. geographic location
    
  App Server:
     - API Call 
        - job queue [job1(post/get), job2(post/get)]
           - worker node should have process checking for the API call
           - if POST: [url1,url2]
               Two-phase transaction:
                 - single transaction as completed only if all urls are scraped
                 - wait mode ( all urls status to be completed )
                 - all urls
               queries the DB for urls?
               if visited? jobid as completed
               if not visited? scraping recursively until the no further <anchor>/img link found on url
          - if GET: [jobid]
               - worker DB, {completed: x, in-progress: T-x, failed/err: }
          - if GET: [jobid/results]
               - worker node queries on jobid
               - urls:
                  images
               - JSON BLOB {url:[images]}
