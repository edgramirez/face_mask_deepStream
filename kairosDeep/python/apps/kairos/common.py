import os
from os import walk


#----- Logging messages -----#
def log_error(msg, quit_program = True):
    print("-- PARAMETER ERROR --\n"*5)
    print(" %s \n" % msg)
    print("-- PARAMETER ERROR --\n"*5)
    if quit_program:
        quit()
    else:
        return False

#----- functions for files -----#
def file_exists(file_name):
    try:
        with open(file_name) as f:
            return file_name
    except OSError as e:
        return False


def open_file(file_name, option='a+'):
    if file_exists(file_name):
        return open(file_name, option)
    return False


def create_file(file_name, content = None):
    if file_exists(file_name):
        os.remove(file_name)
        if file_exists(file_name):
            raise Exception('unable to delete file: %s' % file_name)
    if content:
        with open(file_name, 'w+') as f:
            f.write(content)
    else:
        with open(file_name, 'w+') as f:
            f.close()

    return True


def read_images_in_dir(path_to_read):
    dir_name, subdir_name, file_names = next(walk(path_to_read))
    images = [item for item in file_names if '.jpeg' in item[-5:] or '.jpg' in item[-4:] or 'png' in item[-4:] ]
    return images, dir_name


#----- Json functions -----#
def get_supported_actions():
    return ('GET', 'POST', 'PUT', 'DELETE')


def send_json(data, action, url, header)
    try:
        if action == 'GET':
            r = requests.get(url, data=data, headers=header)
        elif action == 'POST':
            r = requests.post(url, data=data, headers=header)
        elif action == 'PUT':
            r = requests.put(url, data=data, headers=header)
        else:
            r = requests.delete(url, data=data, headers=header)
        return r
    except requests.exceptions.ConnectionError as e:
        time.sleep(sleep_time)
        if retry == retries - 1 and abort_if_exception:
            raise Exception("Unable to Connect to the server after {} retries\n. Original exception: {}".format(retry, str(e)))
    except requests.exceptions.HTTPError as e:
        time.sleep(sleep_time)
        if retry == retries - 1 and abort_if_exception:
            raise Exception("Invalid HTTP response in {} retries\n. Original exception: {}".format(retry, str(e)))
    except requests.exceptions.Timeout as e:
        time.sleep(sleep_time)
        if retry == retries - 1 and abort_if_exception:
            raise Exception("Timeout reach in {} retries\n. Original exception: {}".format(retry, str(e)))
    except requests.exceptions.TooManyRedirects as e:
        time.sleep(sleep_time)
        if retry == retries - 1 and abort_if_exception:
            raise Exception("Too many redirection in {} retries\n. Original exception: {}".format(retry, str(e)))


#----- date time functions -----#
def get_timestamp():
    return int(time.time() * 1000)


#----- network information functions -----#
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', bytes(ifname, 'utf-8')[:15]))
    return ':'.join('%02x' % b for b in info[18:24])


def get_ip_address(ifname):
    return [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]


def get_machine_macaddresses():
    list_of_interfaces = [item for item in os.listdir('/sys/class/net/') if item != 'lo']
    macaddress_list = []

    for iface_name in list_of_interfaces:
        ip = get_ip_address(iface_name)
        if ip:
            macaddress_list.append(getHwAddr(iface_name))
            return macaddress_list


#----- Poligons and Area validation -----#
def check_if_object_is_in_area2(object_coordinates, reference_line, m, b):
    '''
    - returns True if object is in Area2
    - returns False if object is in Area1

    Area1 is by default on top right side 
    '''
    if m is None:
        if object_coordinates[0] > reference_line[0][0]:
            return True
        return False
    elif m == 0:
        if object_coordinates[1] > reference_line[0][1]:
            return True
        return False
    else:
        y_overtheline = (m * object_coordinates[0]) + b

        if object_coordinates[1] > y_overtheline:
            return True
        else:
            return False


def is_point_insde_polygon(x, y, polygon_length, polygon):
    p1x,p1y = polygon[0]
    for i in range(polygon_length+1):
        p2x,p2y = polygon[i % polygon_length]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        # returns True if x,y are inside
                        return True
        p1x,p1y = p2x,p2y

    # returns False if x,y are not inside
    return False

