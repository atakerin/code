import datetime

dt = datetime.datetime.now()
dag = dt.date()
tid = dt.time()


print(f'Dagens datum: {dag}')
print(f'Klockan är: {str(tid)[:8]}')