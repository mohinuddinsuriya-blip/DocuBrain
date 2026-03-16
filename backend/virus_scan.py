import pyclamd

def scan_file(file_path):

    cd = pyclamd.ClamdUnixSocket()

    result = cd.scan_file(file_path)

    if result:
        return False

    return True