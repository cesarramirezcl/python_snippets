import socket

def is_port_open(request):
    """
    Check if a specific port on a given host is open.

    This function attempts to connect to a specified host and port using a TCP socket. 
    If the connection is successful, it indicates that the port is open. If the connection 
    fails, it indicates that the port is closed. In case of any exceptions during the 
    process, the exception message is captured and returned.

    Args:
        request: This argument is included for compatibility with the environment where 
                 this function might be used. However, it is not utilized within the function.

    Returns:
        dict: A dictionary containing the result of the port check:
            - 'open' (bool): True if the port is open, False if the port is closed.
            - 'error' (str, optional): If an exception occurs, this key contains the 
              exception message as a string.
    """
    host = "192.0.2.1"  # Documentation IP address
    port = 8081
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        if result == 0:
            response = {'open': True}
        else:
            response = {'open': False}
    except Exception as e:
        response = {'error': str(e)}
    finally:
        sock.close()
    return response
