# logster - python logging made easy

## installation

```
python -m pip install git+https://github.com/aljabadi/logster.git
```
## usage
```python
from logster import setup_logger

logger = setup_logger(name="rogue-app", level="DEBUG")

logger.debug("This is a debugging message")
logger.info("This is an information message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message, we're past just adding another #TODO")

```

![](static/demo.png)
