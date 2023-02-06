### Use case

To kill a certain process after x amount of time if its not done

for example can use on redis connection to test if the connection works

```
r = redis.Redis("119.196.22.172", port = 6379, db=0)

r.ping() # return true if success , do not return and wait if other wise

```

### References

https://stackoverflow.com/questions/492519/timeout-on-a-function-call
