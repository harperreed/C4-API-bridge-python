import time
import requests
import urllib2

class HTTPBridge:

  api_version = '/v1'

  def __init__(self,  controller_ip=None, port='7070'):
    self.controller_ip = controller_ip
    self.port = port

  def make_request(self, url, params=None, method='GET', ):
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

  def build_url(self,url):
    url = "http://" + self.controller_ip + ":" + self.port + self.api_version + url
    print url
    return url

  def room_control(self, room_id, command, params=None):
    command = command.upper()
    url =  "/room/" + str(room_id) + "/" + command + "/"
    if params:
      param_url = ', '.join("%s/%r" % (key,val) for (key,val) in params.iteritems())

      url = url + param_url
    url = self.build_url(url)
    return self.make_request(url)

  def event_trigger(self, event_name):
    url = "/event/" + str(event_name)
    url = self.build_url(url)
    return self.make_request(url)

  def room_variable(self, room_id, variable_number=None):
    if variable_number:
        url =  "/roomvar/" + str(room_id) + "/" + variable_number
    else:
        url =  "/roomvar/" + str(room_id)

    url = self.build_url(url)
    return self.make_request(url)

  def device_variable(self, device_id, variable_number):
    url =  "/devicevar/" + str(device_id) + "/" + variable_number
    url = self.build_url(url)
    return self.make_request(url)

  def security_panel(self, proxy_id):
    url =  "/securitypanel/" + str(proxy_id)
    url = self.build_url(url)
    return self.make_request(url)

  def relay(self, device_id):
    url =  "/relay/" + str(device_id)
    url = self.build_url(url)
    return self.make_request(url)

  def contact(self, device_id):
    url =  "/contact/" + str(device_id)
    url = self.build_url(url)
    return self.make_request(url)

  def thermostat(self, proxy_id):
    url =  "/thermostatv2/" + str(proxy_id)
    url = self.build_url(url)
    return self.make_request(url)

  def house_off(self):
    #Define TRIGGER1 to be your "house off" event
    event = "TRIGGER2"
    print self.event_trigger(event)

  def home(self):
    #Define TRIGGER1 to be your "home" event
    event = "TRIGGER1"
    return self.event_trigger(event)

  def set_room_volume(self, room_id, volume):
    return self.room_control(42, "SET_VOLUME_LEVEL", {"LEVEL":volume})

  def get_room_volume(self, room_id):
    event_id = 1011
    result = self.room_variable(room_id,"1011")
    result["VOLUME"] = result["VARIABLE_1011"]
    del result["VARIABLE_1011"]
    return result

  def get_room_mediainfo(self, room_id):
    event_id = "1031"
    result = self.room_variable(room_id,event_id)
    result["MEDIAINFO"] = result["VARIABLE_"+event_id]
    del result["VARIABLE_"+event_id]
    return result

