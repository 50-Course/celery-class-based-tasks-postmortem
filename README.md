Post-mortem: Leaking state between class based tasks

Ticket No: `#8972`

This repository aims to perform post-mortem of the production bug in @celery organization.

Reference: https://github.com/celery/celery/issues/8972

Bug description:

> I have a list defined in my **init** method of my task. As the task runs things are appended to the list. I'm noticing that the class is only instantiated once. The list attached to self seems to persist between jobs. This seems very unintuitive and seems like it could lead to concurrency issues with a thread based worker.

Installation

To install the dependencies, run as follows in a virtual environment:

```sh
$ pip install -r requirements.txt
```

Usage

To run the test case, execute the following command:

```sh
$ python test.py
```

Bug tracker

Please report error regarding this issue to official `celery` repository. Or continue the discussion at: celery/celery#8972
