import time
import requests
import urllib2

class HTTPBridge:

  _api_version = '/v1'
  """string: http bridge API version.
"""

  def __init__(self,  controller_ip=None, port='7070'):
    """Function to make a post/get request

    Args:
        controller_ip: IP of your control4 controller.
        port: the port of the bridge api


    Returns:
        Returns HTTPBridge object.

    """
    self.controller_ip = controller_ip
    self.port = port

  def _make_request(self, url, params=None, method='GET', ):
    """Function to make a post/get request

    Args:
        url: The url to request.
        params: the http params for the request
        method: default GET. Could be POST

    Returns:
        Returns JSON or text response.

    """

    if params:
      params = urllib.urlencode(params, True).replace('+', '%20')
    if method=='GET':
      if params:
        url = url + '?'+params
    f = urllib2.urlopen(url,params)
    if (method == 'GET'):
      r = requests.get(url)
    if (r.json()):
        response = r.json()
    else:
        response = r.text
    return response

  def _build_url(self,url):
    """Function to build the request URL .

    Args:
        url: The url to attach to the api version and IP.

    Returns:
        Full request URL.

    """

    url = "http://" + self.controller_ip + ":" + self.port + self._api_version + url
    print url
    return url

  def room_control(self, room_id, command, params=None):
    """Function to handle ROOM CONTROL .
    Direct room remote commands.  

    Key presses listed under Programming, Room Name, Commands, Commands drop-down.

    Example:
        api.room_control(123, "SET_VOLUME_LEVEL", {"LEVEL":25})
        api.room_control(123, "MUTE_ON")

    Args:
        room_id: The url to attach to the api version and IP.
        command: Command from control4
        params: Dict of params for the command. ex: {"LEVEL":25}

    Returns:
        Response from bridge API.


    """
    command = command.upper()
    url =  "/room/" + str(room_id) + "/" + command + "/"
    if params:
      param_url = ', '.join("%s/%r" % (key,val) for (key,val) in params.iteritems())

      url = url + param_url
    url = self._build_url(url)
    return self._make_request(url)

  def event_trigger(self, event_name):
    """Function to handle event triggers .
    Define a event trigger in control4 and then execute it here. 

    Fire driver events to execute Control4 based programming. 

    Example:
        api.event_trigger("TRIGGER1")

    Args:
        event_name: The event name that you want to trigger as defined by the bridge

    Returns:
        Response from bridge API.
    """    

    url = "/event/" + str(event_name)
    url = self._build_url(url)
    return self._make_request(url)

  def room_variable(self, room_id, variable_number=None):
    """Function to get room variables .
    Return room variables. (source ID, volume, etc.) 

    Variables of interest
      1001: Source Device ID
      1005: Mediainfo
      1007: Active Device Binding
      1011: Volume Level
      1031: Mediainfo
      1033: Camera Info

    Example:
        api.room_variable(123) #returns all variables for room
        api.room_variable(123,"1011") #returns Volume level

    Args:
        room_id: the room idea to query
        variable_number: (optional) the variable number

    Returns:
        Response from bridge API.

    """   

    if variable_number:
        url =  "/roomvar/" + str(room_id) + "/" + variable_number
    else:
        url =  "/roomvar/" + str(room_id)

    url = self._build_url(url)
    return self._make_request(url)

  def device_variable(self, device_id, variable_number):
    """Function to return device variable.

    Example:
        api.room_variable(123, 1001) #returns variables 1001

    Args:
        device_id: the room idea to query
        variable_number: the variable number

    Returns:
        Response from bridge API.
    """  
    url =  "/devicevar/" + str(device_id) + "/" + variable_number
    url = self._build_url(url)
    return self._make_request(url)

  def security_panel(self, proxy_id):
    """Return security panel status variables. 

    (Armed state, display text, trouble text, etc.).

    Example:
        api.security_panel(123)

    Args:
        proxy_id: proxy id of the alarm panel

    Returns:
        Response from bridge API.
    """  
    url =  "/securitypanel/" + str(proxy_id)
    url = self._build_url(url)
    return self._make_request(url)

  def relay(self, device_id):
    """Return relay state.

    Example:
        api.relay(123)

    Args:
        device_id: device id of relay

    Returns:
        Response from bridge API.
    """

    url =  "/relay/" + str(device_id)
    url = self._build_url(url)
    return self._make_request(url)

  def contact(self, device_id):
    """Return contact state.

    Example:
        api.contact(123)

    Args:
        device_id: device id of contact

    Returns:
        Response from bridge API.
    """

    url =  "/contact/" + str(device_id)
    url = self._build_url(url)
    return self._make_request(url)

  def thermostat(self, proxy_id):
    """Return thermostat status variables. 
    (Temperature, setpoints, scale, etc.)

    **Needs to be a V2 thermostat driver.**

    Example:
        api.thermostat(123)

    Args:
        proxy_id: proxy id of thermostat

    Returns:
        Response from bridge API.
    """
    url =  "/thermostatv2/" + str(proxy_id)
    url = self._build_url(url)
    return self._make_request(url)

  def house_off(self, event="TRIGGER2"):
    """Turn house to off state.

    Example:
        api.house_off()

    Args:
        event: (OPTIONAL) event which turns house off

    Returns:
        Response from bridge API.
    """
    return self.event_trigger(event)

  def home(self, event="TRIGGER1"):
    """Turn house to home state.

    Example:
        api.home()

    Args:
        event: (OPTIONAL) event which turns home on

    Returns:
        Response from bridge API.
    """
    return self.event_trigger(event)

  def set_room_volume(self, room_id, volume):
    """Set room volume.

    Example:
        api.set_room_volume(123, 25)

    Args:
        room_id: room id to set
        volume: 0-100 volume to set in the room

    Returns:
        Response from bridge API.
    """
    return self.room_control(room_id, "SET_VOLUME_LEVEL", {"LEVEL":volume})

  def mute_room(self, room_id):
    """Mute room.

    Example:
        api.mute_room(123)

    Args:
        room_id: room id to mute

    Returns:
        Response from bridge API.
    """
    return self.room_control(room_id, "MUTE_ON")

  def unmute_room(self, room_id):
    """Unmute room.

    Example:
        api.unmute_room(123)

    Args:
        room_id: room id to unmute

    Returns:
        Response from bridge API.
    """
    return self.room_control(room_id, "MUTE_OFF")

  def get_room_volume(self, room_id):
    """Get room volume.

    Example:
        api.get_room_volume(123)

    Args:
        room_id: room id to get volume

    Returns:
        Response from bridge API.
        VOLUME entity is the 0-100 in volume of room
    """    
    event_id = 1011 #volume 
    result = self.room_variable(room_id,"1011")
    result["VOLUME"] = result["VARIABLE_1011"]
    del result["VARIABLE_1011"]
    return result

  def get_room_mediainfo(self, room_id):
    """Get room media info.

    Example:
        api.get_room_mediainfo(123)

    Args:
        room_id: room id to get media room

    Returns:
        Response from bridge API.
        cover art is base64 encoding URL

    """        
    event_id = "1031" #media info
    result = self.room_variable(room_id,event_id)
    result["MEDIAINFO"] = result["VARIABLE_"+event_id]
    del result["VARIABLE_"+event_id]
    return result

