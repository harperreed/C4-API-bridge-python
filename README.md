# Control4 python API bridge

I recently started using control4. I needed a way to control my home via REST and wanted something that was easy. There is nothing easy. 

However, Houselogix makes a [http web api bridge for control4](https://www.houselogix.com/shop/control4-http-web-api). It is ok. Like most things control4, there is very little documentation and it seems half baked. You can certainly get a lot of things done with it. But it is hard to iterate through your rooms and do a specific task. 

For instance, you can not easily turn off the lights in a specific room. I am doing a lot of debugging and testing and will be updating this class with helper methods as I figure out various things. 

Right now, you can easily change the volume for a specific room, mute and unmute a room, and get room variables. If you know the various "commands" and "variables" inside of control4 - then you can probably get further. But since I am not a *dealer* and don't have access to all of the *insider info,* I am **SOL**.

I will be updating this as I make progress and will be posting more info that should help others do fun projects.

----

If you have questions please email me - [harper@nata2.org](mailto:harper@nata2.org) or hit me up on twitter [@harper](http://twitter.com/harper).





##Example usage 




	from HTTPBridge import HTTPBridge

	if __name__ == "__main__":

	    controller_ip = "192.168.1.x"
	    room = 42 # OFFICE
	    api = HTTPBridge(controller_ip=controller_ip)
	    print api.set_room_volume(room, 25)


More documentation will be forthcoming.



##Documentation

    Help on class HTTPBridge in module HTTPBridge:

    class HTTPBridge
     |  Methods defined here:
     |  
     |  __init__(self, controller_ip=None, port='7070')
     |      Function to make a post/get request
     |      
     |      Args:
     |          controller_ip: IP of your control4 controller.
     |          port: the port of the bridge api
     |      
     |      
     |      Returns:
     |          Returns HTTPBridge object.
     |  
     |  contact(self, device_id)
     |      Return contact state.
     |      
     |      Example:
     |          api.contact(123)
     |      
     |      Args:
     |          device_id: device id of contact
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  device_variable(self, device_id, variable_number)
     |      Function to return device variable.
     |      
     |      Example:
     |          api.room_variable(123, 1001) #returns variables 1001
     |      
     |      Args:
     |          device_id: the room idea to query
     |          variable_number: the variable number
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  event_trigger(self, event_name)
     |      Function to handle event triggers .
     |      Define a event trigger in control4 and then execute it here. 
     |      
     |      Fire driver events to execute Control4 based programming. 
     |      
     |      Example:
     |          api.event_trigger("TRIGGER1")
     |      
     |      Args:
     |          event_name: The event name that you want to trigger as defined by the bridge
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  get_room_mediainfo(self, room_id)
     |      Get room media info.
     |      
     |      Example:
     |          api.get_room_mediainfo(123)
     |      
     |      Args:
     |          room_id: room id to get media room
     |      
     |      Returns:
     |          Response from bridge API.
     |          cover art is base64 encoding URL
     |  
     |  get_room_volume(self, room_id)
     |      Get room volume.
     |      
     |      Example:
     |          api.get_room_volume(123)
     |      
     |      Args:
     |          room_id: room id to get volume
     |      
     |      Returns:
     |          Response from bridge API.
     |          VOLUME entity is the 0-100 in volume of room
     |  
     |  home(self, event='TRIGGER1')
     |      Turn house to home state.
     |      
     |      Example:
     |          api.home()
     |      
     |      Args:
     |          event: (OPTIONAL) event which turns home on
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  house_off(self, event='TRIGGER2')
     |      Turn house to off state.
     |      
     |      Example:
     |          api.house_off()
     |      
     |      Args:
     |          event: (OPTIONAL) event which turns house off
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  mute_room(self, room_id)
     |      Mute room.
     |      
     |      Example:
     |          api.mute_room(123)
     |      
     |      Args:
     |          room_id: room id to mute
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  relay(self, device_id)
     |      Return relay state.
     |      
     |      Example:
     |          api.relay(123)
     |      
     |      Args:
     |          device_id: device id of relay
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  room_control(self, room_id, command, params=None)
     |      Function to handle ROOM CONTROL .
     |      Direct room remote commands.  
     |      
     |      Key presses listed under Programming, Room Name, Commands, Commands drop-down.
     |      
     |      Example:
     |          api.room_control(123, "SET_VOLUME_LEVEL", {"LEVEL":25})
     |          api.room_control(123, "MUTE_ON")
     |      
     |      Args:
     |          room_id: The url to attach to the api version and IP.
     |          command: Command from control4
     |          params: Dict of params for the command. ex: {"LEVEL":25}
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  room_variable(self, room_id, variable_number=None)
     |      Function to get room variables .
     |      Return room variables. (source ID, volume, etc.) 
     |      
     |      Variables of interest
     |        1001: Source Device ID
     |        1005: Mediainfo
     |        1007: Active Device Binding
     |        1011: Volume Level
     |        1031: Mediainfo
     |        1033: Camera Info
     |      
     |      Example:
     |          api.room_variable(123) #returns all variables for room
     |          api.room_variable(123,"1011") #returns Volume level
     |      
     |      Args:
     |          room_id: the room idea to query
     |          variable_number: (optional) the variable number
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  security_panel(self, proxy_id)
     |      Return security panel status variables. 
     |      
     |      (Armed state, display text, trouble text, etc.).
     |      
     |      Example:
     |          api.security_panel(123)
     |      
     |      Args:
     |          proxy_id: proxy id of the alarm panel
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  set_room_volume(self, room_id, volume)
     |      Set room volume.
     |      
     |      Example:
     |          api.set_room_volume(123, 25)
     |      
     |      Args:
     |          room_id: room id to set
     |          volume: 0-100 volume to set in the room
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  thermostat(self, proxy_id)
     |      Return thermostat status variables. 
     |      (Temperature, setpoints, scale, etc.)
     |      
     |      **Needs to be a V2 thermostat driver.**
     |      
     |      Example:
     |          api.thermostat(123)
     |      
     |      Args:
     |          proxy_id: proxy id of thermostat
     |      
     |      Returns:
     |          Response from bridge API.
     |  
     |  unmute_room(self, room_id)
     |      Unmute room.
     |      
     |      Example:
     |          api.unmute_room(123)
     |      
     |      Args:
     |          room_id: room id to unmute
     |      
     |      Returns:
     |          Response from bridge API.
     |  


