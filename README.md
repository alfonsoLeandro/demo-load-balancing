# Demo Load balancing
Simulates a load balancing scenario with 3 instances of a server.
The load balancer is implemented with Nginx.

Each server instance gives out a different response for the same request.

A JMeter project is available to probe the load balancer. You can also access each instance separately.
(Some configuration values might be set to absolute paths, take this into account when running the JMeter project)

## Setup
Build each instance's image:
```
cd instancias
```
```
docker build -t server1 ./server1
```
```
docker build -t server2 ./server2
```
```
docker build -t server3 ./server3
```

## Execution
Run docker compose file
```
docker compose up -d
```

## Accessing
Access the load balancer at http://localhost:8089

Instances:
- server1: http://localhost:3001
- server2: http://localhost:3002
- server3: http://localhost:3003

## Load balancing
The load balancer is configured to use the weighted round-robin load balancing strategy. The weights are set to 1, 2, and 4 for server1, server2, and server3, respectively.

## JMeter
The JMeter project is available at `jmeter/HTTP Request.jmx`. It is configured to probe the load balancer at `http://localhost:8089`.
When ran, it will make 2000 requests with 4 threads (users) and a ramp-up period of 1 second.
When done, it will save the results to a xml file at `jmeter/jmeter_results.xml`.

## Data visualization
Inside the `data visualization` folder, there is a simple python project (requirements.txt included) that will create a pie chart from the responses saved to the jmeter results file.