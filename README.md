# logpilot
logpilot is a project to extend python standard logging to offer customizing ability.

### Install
```bash
pip install logpilot
```

### Log format  

we only support format like this:  
```bash
#--------------------------------------------------
# Log Format
#--------------------------------------------------
# %(asctime)s.%(msecs)03d      yyyy-mm-dd HH:MM:SS 2016-01-01 00:00:00.000
# %(filename)s      
# %(pathname)s      Full path 
# %(funcName)s      
# %(levelname)s     
# %(lineno)d        
# %(module)s        
# %(message)s       
# %(name)s          
# %(processName)s   
# %(threadName)s    
# %(hostname)s      FQDN
# %(uuid)s          custom uuid 
# %(elapsed)s       (ms)
%(asctime)s.%(msecs)03d|%(levelname)s|%(name)s|%(filename)s|%(lineno)d|%(module)s|%(funcName)s|%(processName)s|%(threadName)s|%(message)s|%(hostname)s|%(uuid)s|%(elapsed)s
```

### How to use  
```python
from logpilot.log import Log

log = Log.get_logger(__name__)


class Example(object):

    def __init__(self):
      log.info(msg="this is a test for logpilot", uuid="2b24bad1c5df6b4551768fe09ae877b893fc35505847e80f119c395bca27", elapsed=256)
```

### example log
```bash
2016-11-17 14:35:59|DEBUG|__main__|test2_log.py|11|test2_log|__init__|MainProcess|MainThread|this is a test for logpilot|localhost|2b24bad1c5df6b4551768fe09ae877b893fc35505847e80f119c395bca27|256
```

### How to set global uuid

```python
from logpilot.log import Log
log = Log.get_logger(__name__, uuid='hsdfhkd')
log.info(msg="this is a test logpilot", elapsed=8888)
log.info(msg='hahah', uuid='5678')
log.debug(msg="android world", elapsed=234)
# notice that uuid also can be override
log.error(msg="ios world", uuid='jaj', elapsed=99)
```


### How to change log level
  
default DEBUG

```python  
import logging
from logpilot.log import Log

log = Log.get_logger('test2222')
log.logger.setLevel(logging.INFO)


class Test(object):

    def __init__(self):
        log.info(msg="this is a test logpilot", hahah='hooooo.', age=10000, fake_key='not valid')
        
if __name__ == '__main__':
    from logpilot.log import Log
    a = Test()
    log.debug(msg="this is a test logpilot", hahah='hooooo.', uuid="1234567890")
```  

### TODO:
-[ ] custom format