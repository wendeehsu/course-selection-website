# Run backend
1. run the docker postgres-db
1. run this line in terminal
```
python run.py
```

# Login to db
1. run the docker postgres-db
1. run these commands
```
docker exec -it postgres-db bash
psql -U postgres
\c course_selection // connection to database
```