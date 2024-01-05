Logstash cofiguration for logpilot.

Please configure input and output sections in parser.conf before using it.



Example:

Input:

```bash
2016-11-17 21:11:31|DEBUG|__main__|test2_log.py|11|test2_log|__init__|MainProcess|MainThread|this is a test for logpilot|localhost|2b24bad1c5df6b4551768fe09ae877b893fc35505847e80f119c395bca27|256
```


Output:
```bash
{
    "@timestamp": "2016-11-17T21:11:31.000Z",
    "levelname": "DEBUG",
    "name": "__main__",
    "filename": "test2_log.py",
    "lineno": 11,
    "module": "test2_log",
    "funcName": "__init__",
    "processName": "MainProcess",
    "threadName": "MainThread",
    "messageinfo": "this is a test for logpilot",
    "hostname": "localhost",
    "uuid": "2b24bad1c5df6b4551768fe09ae877b893fc35505847e80f119c395bca27",
    "elapsed": 256
}
```
