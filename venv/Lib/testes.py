# needs win32all, or ActiveState's ActivePython distribution
import win32serviceutil

def service_running(service, machine):
    return win32serviceutil.QueryServiceStatus(service, machine)[1] == 4

def service_info(action, machine, service):
    running = service_running(service, machine)
    servnam = f'service {service} on machine {machine}'
    action = action.lower(  )
    if action == 'stop':
        if not running:
            print(f"Can't stop, {servnam} not running") 
            return 0
        win32serviceutil.StopService(service, machine)
        running = service_running(service, machine)
        if running:
            print(f"Can't stop {servnam} (???)") 
            return 0
        print (f'{servnam} stopped successfully')
    elif action == 'start':
        if running:
            print(f"Can't start, {servnam} already running")
            return 0
        win32serviceutil.StartService(service, machine)
        running = service_running(service, machine)
        if not running:
            print(f"Can't start {servnam} (???)")
            return 0
        print (f"{servnam} started successfully")
    elif action == 'restart':
        if not running:
            print(f"Can't restart, {servnam} not running") 
            return 0
        win32serviceutil.RestartService(service, machine)
        running = service_running(service, machine)
        if not running:
            print(f"Can't restart {servnam} (???)")
            return 0
        print(f"{servnam} restarted successfully") 
    elif action == 'status':
        if running:
            print(f"{servnam} is running")
        else:
            print(f"{servnam} is not running") 
    else:
        print(f"Unknown action {action} requested on {servnam}") 

# if __name__ == '_ _main_ _':
#     # Just ome test code; change at will!
machine = 'NoteDoLucas'
service = 'busca competencia'
action = 'start'
service_info(action, machine, service)
#print('oi')