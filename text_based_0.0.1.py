import sys

PROMPT = "> "

# rooms are just dictionaries, with a description and a list of named actions, which point at other rooms
# the 'exit' value indicates a room which ends the game
# the 'name' is used to give each room a unique  in the map

# Additions
cloak = {
'name':'cloak',
'desc': 'You and three others meet to council in the basement of a building owned by an organization. This is day one, after this meeting you can choose to leave the brotherhood or stay.',
'actions': {'leave': 'sleep', 'stay': 'day_2'},
'exit':False
}
sleep = {
'name':'sleep',
'desc': 'You leave the meeting, sneak back upstairs and go to sleep never to return to the brotherhood.',
'actions': {},
'exit':True
}

sleep_2 = {
'name':'sleep_2',
'desc': 'You turn over in bed and fall asleep.',
'actions': {},
'exit':True
}

day_2 = {
'name':'day_2',
'desc': 'Your clock strikes midnight. The brotherhood is meeting for their second day.',
'actions': {'sleep': 'sleep_2', 'sneak to meeting': 'day_2_meeting'},
'exit':False
}

day_2_meeting = {
'name':'day_2_meeting',
'desc': 'You make it into the basement. The room is lit by a drop light covered with a cloth as not to arrouse suspicion. On the table is a map on Long Island. You and three others gather.',
'actions': {'hear plans': 'plans', 'zone out': 'zone_out'},
'exit':False
}

plans = {
'name':'plans',
'desc': 'Lion moves the light over the map of the Island. He puts a pin into Pilgrim State Psych centere, one in Katies of Smithtown, one in Kings Park Psych Centere, one on Sweethallow Rd, and one at the Amityville Horror house. Together, they form two opposing triangles. You mission is to investigate these sites and debunk two paranormal portals.',
'actions': {'laugh': 'laugh', 'take pilgrim': 'plans_2'},
'exit':False
}

plans_2 = {
'name':'plans_2',
'desc': 'The others took Katies Pub, The Amityville Horror House, and Kings Park. By default you will also take Sweethallow Rd. Lion speaks, Give me two weeks for my guy to report back with the papers, we can not let anyone know what we are up to. One week to process the request, and one for package delivery. That will leave us with one week and a half to plan.',
'actions': {'history': 'history', 'report': 'report'},
'exit':False
#'char_name': True
#'char_name_var': '0',
}

history = {
'name':'history',
'desc': 'You are a member of an secret organization on Long Island. You have temporary lodging at this Lake Ronkonkoma location. Hidden underneath this organization a group of four men meet to discuss the future fate of Long Island. During the day you converse with other group members while keeping secret the words said during the Midnight Meetings. The group leader, Lion, returns to this building from time to time when his services are required. During the day he organizes affairs.',
'actions': {'more history': 'history_2', 'report': 'report'},
'exit':False
}

history_2 = {
'name':'history_2',
'desc': 'A brotherhood gathers upstairs on the level of society seven days a week. Hallways are full of members and rooms are filled with bodies. People read, discuss, and gather. Life moves on. (Add More: Dev...) You can attend the Report meeting or go to sleep and skip it.',
'actions': {'report': 'report', 'sleep': 'sleep_2'},
'exit':False
}

report = {
'name':'report',
'desc': 'Welcome back gentleman, sorry it took so long to procure the necessary documents. After tonight we will only meet once more. From there, we will have new identities, new phone numbers, but it is imperative that we stay connected. We will pick a rendezvous next time. Lion handed out dossier in brown envelopes to each person. You are handed two, do not open them until you are clear of the building.',
'actions': {'last night': 'last_night', 'party': 'party'},
'exit':False
}

last_night = {
'name':'last_night',
'desc': 'You slowly creek the basement door open guided by the faint light of the drop light. As you peer around the staircase Lion is waiting underneath the glow. You help him arrange the parting rewards for your fellows. Moments later, the others join in. Lion speaks, Welcome back gentleman. Thank you for your persistance and stealth. Unfortunately lodging here is only for twenty eight days and tomorrow you will be on your way. Let us rendezvous at Southdown Coffee in Huntington on Friday nights to discuss our progress. Take your information and go with God. Before we depart tonight, I have a gift for each of you. Take this blessed cross and wear it about your necks, it will protect you.',
'actions': {'pack and depart': 'depart'},
'exit':False
}

depart = {
'name':'depart',
'desc': 'The next day you pack your dossiers into your bag and ensure you end is taken care of as you sign out. A car is waiting for you. As you approach the car, the other members of the Midnight Brotherhood are present. You each walk off into your respective modes of transportation. You are handed a new cell phone, a bit outdated, but your old one is no longer required.',
'actions': {'home': 'home', 'football': 'game'},
'exit':False
}

home = {
'name':'home',
'desc': 'You arrive at home, rush to a calender and mark Friday night on it. It is Sunday, you have one week.',
'actions': {'read pilgrim': 'pilgrim_plan', 'read sweethallow': 'sweethallow_plan'},
'exit':False
}

pilgrim_plan = {
'name':'pilgrim_plan',
'desc': 'You open the Pilgrim State Dossier and begin to read. The mental hospital had shutdown most of its facilities years ago. There are reports that range from missing blood to the dumping of bodies. There is still an active building there and the area is patrolled by the State Troopers 24/7. Enterance will be difficult. Rumon has it that local gangs use the abonden buildings as club houses and the homeless as a shelter.',
'actions': {'begin': 'pilgrim_2', 'sleep': 'sleep_2'},
'exit':False
}

pilgrim_2 = {
'name':'pilgrim_2',
'desc': 'You have no contacts',
'actions': {'read pilgrim': 'pilgrim_plan', 'read sweethallow': 'sweethallow_plan'},
'exit':False
}

sweethallow_plan = {
'name':'sweethallow_plan',
'desc': 'Dev Note-2',
'actions': {'read Pilgrim': 'pilgrim_plan', 'read sweethallow': 'sweethallow_plan', 'exit-loop': 'sleep',},
'exit':False
}


game = {
'name':'game',
'desc': 'You head out that night to catch the football game. You party hard and forget all about the Midnight Brotherhood. Years later, your dossier is thrown out in the trash.',
'actions': {},
'exit':True
}

party = {
'name':'party',
'desc': 'You get drunk and miss the final meeting of the Midnight Brotherhood, your dossiers are missing. You rush down into the basement at midnight and find nothing but janitorial equiptment.',
'actions': {},
'exit':True
}

laugh = {
'name':'laugh',
'desc': 'You roll onto the floor laughing. As you are doing so the drop light falls and punctures your eye, you grab frantically around and pull the side of the table onto your kneck.',
'actions': {},
'exit':True
}

zone_out = {
'name':'zone_out',
'desc': 'You fall alseep on the table and drool everwhere.',
'actions': {},
'exit':True
}


# Segement 2
bath = {
'name':'bath',
'desc': 'The last tour bus of the day leaves the city bringing with it the excitment of the day.',
#'actions': {'go up': 'tower', 'break the gate': 'main_stairs'},
'exit':False
}

gravel_walk = {
'name':'gravel_walk',
'desc': 'Trees arch over a grvel walkway at night illuinated by a single lantern post. You keep to the shadows.',
#'actions': {'go up': 'tower', 'break the gate': 'main_stairs'},
'exit':False
#pg 22
}

# Template Below
entrance_room = {
'name':'entrance',
'desc': 'You are in a dimly lit cave. To your left there is a winding staircase heading up into the darkness, to your right, a rusty iron gate',
'actions': {'go up': 'tower', 'break the gate': 'main_stairs'},
'exit':False
}

tower_dead_end = {
'name':'tower'  ,           
'desc' : 'You emerge from the stairway in the ruins of an old tower. There is nothing here but broken stones and matted vines',
'actions': {'go down': 'entrance'},
'exit':False
}

main_stairs = {
'name':'main_stairs',
'desc':'The gate gives way after a few hard kicks, and clangs loundly down a flight of steps into the darkness. You hear the sound of water from down below.',
'actions': { 'go down':'pitfall', 'light torch':'stairs_torch'},
'exit':False
}

stairs_torch= {
'name':'stairs_torch',          
'desc':'your torch sputters to life and reveals a large gap in the stairs about ten feet ahead of you. It might be possible to edge by it to the left side...',
'actions': { 'jump the gap':'pitfall', 'go_up':'entrance', 'edge around':'sneak_by'},
'exit':False
}

sneak_by = {
'name':'sneak_by',
'desc':'You carefully step past the gap. A few feet later you are handed a check for $85,000,000 and the keys to a Tesla. Congratulations!',
'actions':{},
'exit':True}

pitfall = {
'name':'pitfall',
'desc':'You fall into a large gap in the stairs that you would have seen if you had only lit a torch. You plummet to a mercifully quick death in the icy water far below.',
'actions':{},
'exit':True
}

# this is shorthand way of making all of the above dictionaries into a dictionary keyed by the 'name' entries
# in a real game you'd want to make sure these all actually existed and that there were no typos!
map = dict ( (item['name'],item) for item in (cloak, sleep, sleep_2, day_2, day_2_meeting, plans, zone_out, laugh, plans_2, history, history_2, report, party, last_night, depart, home, game, pilgrim_plan, sweethallow_plan, gravel_walk, entrance_room, tower_dead_end, main_stairs, stairs_torch, sneak_by, pitfall))


def game_loop(room, map):
    # room is a dictionary describing an individual room or action
    # map is a dictionary of rooms, keyed by name

    sys.stdout.writelines(room['desc'])

    if room['exit']: 
        sys.stdout.writelines('\nThanks for playing!')
        return

    next = None

    while not next:
        sys.stdout.writelines ("\nYou can...")
        for item in room['actions'].keys():
            sys.stdout.writelines("\n\t" + item)

        sys.stdout.writelines("\n>")
        user_input = sys.stdin.readline()
        user_input = user_input.strip().lower() # just take  lower case for simplicity
        if user_input in room['actions']:  
            next = room['actions'][user_input]
        else:
            sys.stdout.writelines("'%s' is not a supported option. Please try again\h" % user_input)
    game_loop(map[next], map)

game_loop (cloak, map)
