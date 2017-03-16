


## API documentation for the Control4 HTTP Web API Bridge

This is a annotated mirror of the Driver documenation that is located [here](https://www.houselogix.com/shop/control4-http-web-api)

###OVERVIEW

This driver exposes a web server endpoint for interacting with Control4 systems. This enables Control4 integration into other control systems.

API references RoomID, DeviceID, and ProxyID. These can be found in Composer by hovering over a room or device with your mouse until the tooltip appears.


---------

###API - CURRENT VERSION 1

### http://controllerIP:7070/

All endpoint requests return JSON responses.


---------

###ROOM CONTROL - HTTP GET

### /v1/room/[roomID]/[cmd]
OR
### /v1/room/[roomID]/[cmd]/[param1]/[value1]/.../...



Direct room remote commands.  

Key presses listed under Programming, Room Name, Commands, Commands drop-down.

**Example:**

* http://controllerIP:7070/v1/room/123/VOL_UP
* http://controllerIP:7070/v1/room/123/SET_VOLUME_LEVEL/LEVEL/25


---------

##EVENT TRIGGER - HTTP GET
### /v1/event/[eventName]

---------

Fire driver events to execute Control4 based programming.

**Example:**

* http://controllerIP:7070/v1/event/TRIGGER1


---------

##ROOM VARIABLE - HTTP GET

### /v1/roomvar/[roomID]
OR
### /v1/roomvar/[roomID]/[varNumber]


Return room variables. (source ID, volume, etc.)

**Example:**

* http://controllerIP:7070/v1/roomvar/123
* http://controllerIP:7070/v1/roomvar/123/1001

Some variables of interest:

* VARIABLE_1001: Source Device ID
* VARIABLE_1005: Mediainfo
* VARIABLE_1007: Active Device Binding
* VARIABLE_1011: Volume Level
* VARIABLE_1031: Mediainfo
* VARIABLE_1033: Camera Info


---------

##DEVICE VARIABLE - HTTP GET
### /v1/devicevar/[deviceID]/[varNumber]



Return device variable.

**Example:**

* http://controllerIP:7070/v1/devicevar/123/1001


---------

##SECURITY PANEL - HTTP GET
### /v1/securitypanel/[proxyID]

http://192.168.200.193:7070/v1/securitypanel/691

---------

Return security panel status variables. (Armed state, display text, trouble text, etc.)

**Example:**

* http://1921.686.1.2:7070/v1/securitypanel/123


---------

##RELAY - HTTP GET
### /v1/relay/[deviceID]

---------

Return relay state.

**Example:**

* http://controllerIP:7070/v1/relay/123


---------

##CONTACT - HTTP GET
### /v1/contact/[deviceID]

---------

Return contact state.

**Example:**

* http://controllerIP:7070/v1/contact/123


---------

##THERMOSTAT V2 - HTTP GET
### /v1/thermostatv2/[proxyID]

---------

Return thermostat status variables. (Temperature, setpoints, scale, etc.)

Needs to be a V2 thermostat driver.

**Example:**

* http://controllerIP:7070/v1/thermostatv2/123


---------
