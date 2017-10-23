from items import *

room_studio = {
	"name": "Studio",
	"rap": "this ting go skraa, pap pap kak kak kak, skiddy skit pap pap, an a pop pop truu boom",
	"room_difficulty": 14,
	"description": "The studio is small, and smells of marijuana. The coat rack is empty, man's not hot.",
	"rapper": "Roadman Shaq",
	"rapperbeat": False,
	"exits": {"east": "Warehouse", "south": "Street Corner", "north": "Concert", "east": "Recording Booth"},
	"items": [],
	"award": item_hat

}

room_warehouse = {
	"name": "Warehouse",
	"rap": "Kung fu kenny now, my resume is real enough for two millenniums",
	"room_difficulty": 14,
	"description": "It's a dimly lit warehouse, the air is thick with smoke, and floors littered with burnt out joints.",
	"rapper": "Kendrick Lamar",
	"exits": {"west": "Studio", "north": "Grove Street"},
	"rapperbeat": False,
	"items": [],
	"award": item_dreadlocks
}

room_streetcorner = {
	"name": "Street Corner",
	"rap": "Who dat boy, who him is",
	"room_difficulty": 3,
	"description": "There is a crowd of gang members",
	"rapper": "Tyler, the Creator",
	"exits": {"north": "Studio"},
	"rapperbeat": False,
	"items": [],
	"award": item_mic
}

room_concert = {
	"name": "Rap Concert",
	"rap": "a suma luma duma luma you assumin I'm a human, what I got to do to get it through to you I'm superhuman",
	"room_difficulty": 2,
	"description": "Eminem stands proudly on stage, as thousands of fans scream his name. Out of the crowd he spots you, and invites you to challenge him to a rap battle - live!",
	"rapper": "Eminem",
	"exits": {"south": "Studio"},
	"rapperbeat": False,
	"items": [],
	"award": item_tattoo
}

jail_entrance = {
	"name": "Jail Entrance",
	"description": "You have just been released from jail.",
	"exits": {"south":"Main Street"},
	"items":[],
	"rap": "",
	"n":0,
	"rapperbeat": False,
	"rapper":"",


}

main_street = {
	"name": "Main Street",
	"description": "You are on the Main Street.",
	"exits": {"north":"Jail Entrance", "south":"Grove Street"},
	"items":[],
	"rap": "I'm bout to make this mic short circuit, this beat is whack and fits you perfect",
	"room_difficulty":16,
	"rapperbeat": False,
	"rapper":"Novice Rapper",
	"award": item_glasses
}

grove_street = {
	"name": "Grove Street",
	"description": "You are in your old cul-de-sac. Your old home.",
	"exits": {"north":"Main Street", "south": "Warehouse"},
	"items":[],
	"rap":"",
	"room_difficulty":14,
	"rapperbeat": False,
	"rapper":"Ice Cube",
	"award": item_mic

}

room_recordingbooth = {
	"name": "Recording Booth",
	"description": "You are in a retro recording booth, and a dimly lit character stands in the corner of the room, joint in hand.",
	"exits": {"west": "Studio"},
	"items":[],
	"rap":"",
	"room_difficulty": 14,
	"rapperbeat": False,
	"rapper": "Snoop Dogg",
	"award": item_joint
}


rooms = {
    "Studio": room_studio,
    "Warehouse": room_warehouse,
    "Street Corner": room_streetcorner,
    "Concert": room_concert,
    "Grove Street": grove_street,
    "Main Street": main_street,
    "Jail Entrance":jail_entrance,
    "Recording Booth": room_recordingbooth
}
