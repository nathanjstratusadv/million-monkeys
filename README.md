# million-monkeys
A million monkeys on typewriters writing the greatest novel of all time!

# Running

## Windows

To run a Celery worker on Windows for development or debugging, you can use the --pool=solo (or shorthand -P solo) option. 
This is necessary because Celery's default concurrency mechanism (prefork) is incompatible with Windows due to differences in how the operating systems handle process forking. 

`celery worker --pool=solo --loglevel=info`