## Sometimes traceback is long

When URL to retrieve doesn’t exist, or the host server is down.
In those cases, this script will now raise an uncaught ConnectionError exception and print a traceback:

```
python urlcaller.py http://thisurlprobablydoesntexist.com
```

#### Output

  <details>

```
        python urlcaller.py http://thisurlprobablydoesntexist.com\
    C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.9) or chardet (5.1.0)/charset_normalizer (2.0.4) doesn't match a supported version!
      warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
    Traceback (most recent call last):
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
        conn = connection.create_connection(
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\util\connection.py", line 72, in create_connection
        for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\socket.py", line 918, in getaddrinfo
        for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
    socket.gaierror: [Errno 11001] getaddrinfo failed

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
        httplib_response = self._make_request(
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
        conn.request(method, url, **httplib_request_kw)
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 239, in request
        super(HTTPConnection, self).request(method, url, body=body, headers=headers)
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1255, in request
        self._send_request(method, url, body, headers, encode_chunked)
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1301, in _send_request
        self.endheaders(body, encode_chunked=encode_chunked)
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1250, in endheaders
        self._send_output(message_body, encode_chunked=encode_chunked)
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1010, in _send_output
        self.send(msg)
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 950, in send
        self.connect()
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 205, in connect
        conn = self._new_conn()
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
        raise NewConnectionError(
    urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x0000023BFF630DF0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\adapters.py", line 440, in send
        resp = conn.urlopen(
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connectionpool.py", line 785, in urlopen
        retries = retries.increment(
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\util\retry.py", line 592, in increment
        raise MaxRetryError(_pool, url, error or ResponseError(cause))
    urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: /%5C (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000023BFF630DF0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "urlcaller.py", line 4, in <module>
        response = requests.get(sys.argv[1])
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\api.py", line 75, in get
        return request('get', url, params=params, **kwargs)
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\api.py", line 61, in request
        return session.request(method=method, url=url, **kwargs)
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\sessions.py", line 529, in request
        resp = self.send(prep, **send_kwargs)
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\sessions.py", line 645, in send
        r = adapter.send(request, **kwargs)
      File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\adapters.py", line 519, in send
        raise ConnectionError(e, request=request)
    requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: /%5C (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000023BFF630DF0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
```

  </details>

## Suppress error

- If no catch, traceback will print
- If catch the exception, the traceback can be suppress

```
python urlcaller_suppress.py http://thisurlprobablydoesntexist.com
```

#### Output

```
-1 Connection Error
```

## Logging traceback

- in most real systems, you don’t want to just silence the exception and resulting traceback, but you want to log the traceback.
- Logging tracebacks allows you to have a better understanding of what goes wrong in your programs.

```
python urlcaller_logger.py http://thisurlprobablydoesntexist.com
```

#### Output

<details>

```
 warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
Traceback (most recent call last):
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
   conn = connection.create_connection(
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\util\connection.py", line 72, in create_connection
   for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\socket.py", line 918, in getaddrinfo
   for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
   httplib_response = self._make_request(
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
   conn.request(method, url, **httplib_request_kw)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 239, in request    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1255, in request
   self._send_request(method, url, body, headers, encode_chunked)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1301, in _send_request
   self.endheaders(body, encode_chunked=encode_chunked)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1250, in endheaders
   self._send_output(message_body, encode_chunked=encode_chunked)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1010, in _send_output
   self.send(msg)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 950, in send
   self.connect()
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 205, in connect    conn = self._new_conn()
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
   raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x0000011B23A80DC0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\adapters.py", line 440, in send
   resp = conn.urlopen(
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connectionpool.py", line 785, in urlopen
   retries = retries.increment(
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\util\retry.py", line 592, in increment
   raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000011B23A80DC0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
 File "urlcaller_logger.py", line 9, in <module>
   response = requests.get(sys.argv[1])
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\api.py", line 75, in get
   return request('get', url, params=params, **kwargs)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\api.py", line 61, in request
   return session.request(method=method, url=url, **kwargs)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\sessions.py", line 529, in request
   resp = self.send(prep, **send_kwargs)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\sessions.py", line 645, in send
   r = adapter.send(request, **kwargs)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\adapters.py", line 519, in send
   raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000011B23A80DC0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
 File "urlcaller_logger.py", line 11, in <module>
   logger.exception()
TypeError: exception() missing 1 required positional argument: 'msg'                                               python urlcaller_logger.py http://thisurlprobablydoesntexist.comence-playground\notebooks\error_handling\suppress_error>
C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.9) or chardet (5.1.0)/charset_normalizer (2.0.4) doesn't match a supported version!
 warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
Connection Error
Traceback (most recent call last):
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 174, in _new_conn
   conn = connection.create_connection(
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\util\connection.py", line 72, in create_connection
   for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\socket.py", line 918, in getaddrinfo
   for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen
   httplib_response = self._make_request(
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connectionpool.py", line 398, in _make_request
   conn.request(method, url, **httplib_request_kw)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 239, in request
   super(HTTPConnection, self).request(method, url, body=body, headers=headers)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1255, in request
   self._send_request(method, url, body, headers, encode_chunked)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1301, in _send_request
   self.endheaders(body, encode_chunked=encode_chunked)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1250, in endheaders
   self._send_output(message_body, encode_chunked=encode_chunked)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 1010, in _send_output
   self.send(msg)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\http\client.py", line 950, in send
   self.connect()
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 205, in connect
   conn = self._new_conn()
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connection.py", line 186, in _new_conn
   raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x0000019F56CF1DC0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\adapters.py", line 440, in send
   resp = conn.urlopen(
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\connectionpool.py", line 785, in urlopen
   retries = retries.increment(
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\urllib3\util\retry.py", line 592, in increment
   raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000019F56CF1DC0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
 File "urlcaller_logger.py", line 9, in <module>
   response = requests.get(sys.argv[1])
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\api.py", line 75, in get
   return request('get', url, params=params, **kwargs)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\api.py", line 61, in request
   return session.request(method=method, url=url, **kwargs)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\sessions.py", line 529, in request
   resp = self.send(prep, **send_kwargs)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\sessions.py", line 645, in send
   r = adapter.send(request, **kwargs)
 File "C:\Users\codenamewei\.conda\envs\face-meeting\lib\site-packages\requests\adapters.py", line 519, in send
   raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='thisurlprobablydoesntexist.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000019F56CF1DC0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
-1 Connection Error
```

</details>

- Now when the script for a problematic URL is run, it will print the expected -1 and Connection Error, but it will also log the traceback
- By default, Python will send log messages to standard error (stderr). This looks like we haven’t suppressed the traceback output at all. However, if you call it again while redirecting the stderr, you can see that the logging system is working, and we can save our logs off for later:

```
python urlcaller_logger.py http://thisurlprobablydoesntexist.com 2> my-logs.log
```

or add this config and run

```
logging.basicConfig(filename = "debug.log",
            level = os.environ.get("LOGLEVEL", "INFO").upper(),
            format = '%(asctime)s %(levelname)s %(filename)s:%(lineno)s - %(funcName)s(): %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
```

```
python urlcaller_logger.py http://thisurlprobablydoesntexist.com
```
