# Control4 API bridge python

I recently started using control4. I needed a way to control my home via REST and wanted something that was easy. There is nothing easy. 

However, Houselogix makes a [http web api bridge for control4](https://www.houselogix.com/shop/control4-http-web-api). It is ok. Like most things control4, there is very little documentation and it seems half baked. You can certainly get a lot of things done with it. But it is hard to iterate through your rooms and do a specific task. 

For instance, you can not easily turn off the lights in a specific room. I am doing a lot of debugging and testing and will be updating this class with helper methods as I figure out various things. 

Right now, you can easily change the volume for a specific room, mute and unmute a room, and get room variables. If you know the various "commands" and "variables" inside of control4 - then you can probably get further. But since I am not a *dealer* and don't have access to all of the *insider info* I am **SOL**.

I will be updating this as I make progress and will be posting more info that should help others do fun projects.

##Example usage 




	from HTTPBridge import HTTPBridge

	if __name__ == "__main__":

	    controller_ip = "192.168.1.x"
	    room = 42 # OFFICE
	    api = HTTPBridge(controller_ip=controller_ip)
	    print api.set_room_volume(room, 25)


More documentation will be forthcoming.


----

If you have questions please email me - [harper@nata2.org](mailto:harper@nata2.org) or hit me up on twitter [@harper](http://twitter.com/harper).

----
