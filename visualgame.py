import pygame
running = True
goal= False
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Image Based Adventure Game")
width = 1000
height = 600
screen = pygame.display.set_mode((width,height))
map_pos_y =-200
map_pos_x= -500
overall_y =1
last_thrown_position = None
og_map_y = -200
overlapped = True
extra_cover = None
last_position = (0,0)
last_overall_y = 1
inventory_pos = (2.77/4*width,3.1/4*height)
itemInhand = "Hand"
moving = False
punched = False

character_animation_on = False
punch_frame = 0
character_item_thrown_frame = 0
punched_direction = None
door_1_interact = False
door_2_interact = False
door_3_interact = False
door_4_interact = False
door_5_interact = False
sword_location = "inventory"
money_location = "inventory"
meat_location = "inventory"
key_location = "inventory"
key_img = pygame.image.load("images/characters/basic/north-west/Throw/Key/0095.png").convert_alpha()
sword_img = pygame.image.load("images/characters/basic/east/Throw/Sword/0095.png").convert_alpha()
money_img = pygame.image.load("images/characters/basic/south/Throw/Money/0095.png").convert_alpha()
meat_img = pygame.image.load("images/characters/basic/south/Throw/Meat/0095.png").convert_alpha()
direction = "east"
thrown_item = None
thrown_direction = None
semi_throwing = False
thrown_movement = None
thrown = False
character_thrown_frame = 0
throwing = False
thrown_position = None
movement = [0,0]
ptype = "basic"
moved_for = 0
current_room = "main"
past_room = "main"
door_interact = None
raw_main_room_img = pygame.image.load("images/enironment/Main-Room/Basic-View.png").convert_alpha()
raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Main-Room/Floor.png").convert_alpha()
room_change = None
collison, collision_with = None, None
door_1_interact_img=None 
door_2_interact_img=None 
door_3_interact_img=None 
door_4_interact_img=None 
door_5_interact_img=None  
money_interact_img=None  
money_interact1_img=None  
money_interact2_img=None  
money_interact3_img=None  
money_interact4_img=None  
meat_interact_img=None  
meat_interact1_img=None  
meat_interact2_img=None  
meat_interact3_img=None  
meat_interact4_img=None  
sword_interact_img=None
sword_interact1_img=None
sword_interact2_img=None
sword_interact3_img=None
sword_interact4_img=None  
key_interact_img=None 
key_interact1_img=None 
key_interact2_img=None 
key_interact3_img=None 
key_interact4_img=None 
door_1_interact_mask=None 
door_2_interact_mask=None 
door_3_interact_mask=None 
door_4_interact_mask=None 
door_5_interact_mask=None 
money_interact_mask=None 
meat_interact_mask=None 
sword_interact_mask=None 
key_interact_mask=None 
door_1_interact_rect=None 
door_2_interact_rect=None 
door_3_interact_rect=None 
door_4_interact_rect=None 
door_5_interact_rect = None
money_interact_rect = None
meat_interact_rect = None
sword_interact_rect = None
key_interact_rect = None
player_w,player_h = int(width*2/5), int(height*2/5)

inventory_selected = "1"
player_x,player_y = width/2,height/2
main_room_img = pygame.transform.scale(raw_main_room_img,(width*2,height*2))
main_room_floor = pygame.transform.scale(raw_main_room_floor_placeholder_img,(width*2,height*2))
floor_mask = pygame.mask.from_surface(main_room_floor)

last_player_size = None
player_hitbox_mask = None
current_player_size = (int(player_w), int(player_h))
player_real_hitbox_raw = pygame.image.load("images/characters/basic/The_real_hitbox.png").convert_alpha()
player_real_hitbox = pygame.transform.scale(player_real_hitbox_raw, current_player_size) 
player_real_hitbox_mask = pygame.mask.from_surface(player_real_hitbox)

player_real_hitbox_rect = player_real_hitbox.get_rect(center=(player_x,player_y))
inventory_selected_1 = pygame.transform.scale(pygame.image.load("images/other/Inventory_selected1.png").convert_alpha(),(width*0.3,height*0.3))
inventory_selected_2 = pygame.transform.scale(pygame.image.load("images/other/Inventory_selected2.png").convert_alpha(),(width*0.3,height*0.3))
inventory_selected_3 = pygame.transform.scale(pygame.image.load("images/other/Inventory_selected3.png").convert_alpha(),(width*0.3,height*0.3))
inventory_selected_4 = pygame.transform.scale(pygame.image.load("images/other/Inventory_selected4.png").convert_alpha(),(width*0.3,height*0.3))
inventory_selected_5 = pygame.transform.scale(pygame.image.load("images/other/Inventory_selected5.png").convert_alpha(),(width*0.3,height*0.3))

inventory_item_1 = pygame.transform.scale(pygame.image.load("images/other/Inventory_1_item.png").convert_alpha(),(width*0.3,height*0.3))
inventory_item_2 = pygame.transform.scale(pygame.image.load("images/other/Inventory_2_item.png").convert_alpha(),(width*0.3,height*0.3))
inventory_item_3 = pygame.transform.scale(pygame.image.load("images/other/Inventory_3_item.png").convert_alpha(),(width*0.3,height*0.3))
inventory_item_4 = pygame.transform.scale(pygame.image.load("images/other/Inventory_4_item.png").convert_alpha(),(width*0.3,height*0.3))
inventory_item_5 = pygame.transform.scale(pygame.image.load("images/other/Inventory_5_item.png").convert_alpha(),(width*0.3,height*0.3))
character_animation = {

    "loaded": False
    }
# function which loads all the core animations in the game, such as walking, throwing items, getting punched, standing still.
# function called with a variable named "ptype" which has not been fully finished yet, but later will provide customizability for characters.
def load_animations(ptype):
    directions = ["north","south","east","west","north-east","north-west","south-east","south-west"]
    items = ["Hand", "Money", "Sword", "Key", "Meat"]
    character_animation = {

    "loaded": True,
    "hitbox": pygame.image.load(f"images/characters/{ptype}/Hitbox.png").convert_alpha(),
    "east": {
    "walk": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []
    },
    "stand": {
        "Hand": None,
        "Sword": None,
        "Money": None,
        "Meat": None,
        "Key": None

    },
    "punched": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []

    },
    "throw": [],
    "throw_items": {
        "Key": [],
        "Sword": [],
        "Money": [],
        "Meat": []
    }
    },

    "west": {
    "walk": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []
    },
    "stand": {
        "Hand": None,
        "Sword": None,
        "Money": None,
        "Meat": None,
        "Key": None

    },
    "punched": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []

    },
    "throw": [],
    "throw_items": {
        "Key": [],
        "Sword": [],
        "Money": [],
        "Meat": []
    }
    },
    "north": {
    "walk": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []
    },
    "stand": {
        "Hand": None,
        "Sword": None,
        "Money": None,
        "Meat": None,
        "Key": None

    },
    "punched": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []

    },
    "throw": [],
    "throw_items": {
        "Key": [],
        "Sword": [],
        "Money": [],
        "Meat": []
    }
    },
    "south": {
    "walk": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []
    },
    "stand": {
        "Hand": None,
        "Sword": None,
        "Money": None,
        "Meat": None,
        "Key": None

    },
    "punched": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []

    },
    "throw": [],
    "throw_items": {
        "Key": [],
        "Sword": [],
        "Money": [],
        "Meat": []
    }
    },
    "south-east": {
    "walk": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []
    },
    "stand": {
        "Hand": None,
        "Sword": None,
        "Money": None,
        "Meat": None,
        "Key": None

    },
    "punched": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []

    },
    "throw": [],
    "throw_items": {
        "Key": [],
        "Sword": [],
        "Money": [],
        "Meat": []
    }
    },
    "south-west": {
    "walk": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []
    },
    "stand": {
        "Hand": None,
        "Sword": None,
        "Money": None,
        "Meat": None,
        "Key": None

    },
    "punched": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []

    },
    "throw": [],
    "throw_items": {
        "Key": [],
        "Sword": [],
        "Money": [],
        "Meat": []
    }
    },
    "north-west": {
    "walk": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []
    },
    "stand": {
        "Hand": None,
        "Sword": None,
        "Money": None,
        "Meat": None,
        "Key": None

    },
    "punched": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []

    },
    "throw": [],
    "throw_items": {
        "Key": [],
        "Sword": [],
        "Money": [],
        "Meat": []
    }
    },
    "north-east": {
    "walk": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []
    },
    "stand": {
        "Hand": None,
        "Sword": None,
        "Money": None,
        "Meat": None,
        "Key": None

    },
    "punched": {
        "Hand": [],
        "Sword": [],
        "Money": [],
        "Meat": [],
        "Key": []

    },
    "throw": [],
    "throw_items": {
        "Key": [],
        "Sword": [],
        "Money": [],
        "Meat": []
    }
    }}
    assets_loaded =0
    for item in items:
        print(f"Loading {item}...                 \033[F")
        for d in directions:
            print(f"Loading {d} walk...                \033[F")
            for x in range(30):
                y=x+5
                if y <10:
                    character_animation[d]["walk"][item].append(pygame.image.load(f"images/characters/{ptype}/{d}/Walk/{item}/000{y}.png").convert_alpha())
                    
                else:
                    character_animation[d]["walk"][item].append(pygame.image.load(f"images/characters/{ptype}/{d}/Walk/{item}/00{y}.png").convert_alpha())
                assets_loaded +=1
            character_animation[d]["stand"][item]=pygame.image.load(f"images/characters/{ptype}/{d}/Stand/{item}/Stand.png").convert_alpha()
            assets_loaded +=1
            punched_dir_vals = {
                "south-west": 80,
                "west": 115,
                "north": 150,
                "east": 185,
                "north-east": 220,
                "north-west": 255,
                "south": 290,
                "south-east": 325
            }
            
            print(f"Loading {d} punched...               \033[F")
            for x in range(31):
                if punched_dir_vals[d]+x < 100:
                    character_animation[d]["punched"][item].append(pygame.image.load(f"images/characters/{ptype}/{d}/Punched/{item}/00{punched_dir_vals[d]+x}.png").convert_alpha())
                    
                else:
                    character_animation[d]["punched"][item].append(pygame.image.load(f"images/characters/{ptype}/{d}/Punched/{item}/0{punched_dir_vals[d]+x}.png").convert_alpha())
                assets_loaded +=1
                    
            if len(character_animation[d]["walk"]) ==30 and len(character_animation[d]["throw"]) ==30 and len(character_animation[d]["punched"]) ==31 and character_animation[d]["stand"][item] is not None:
                print(f"Loaded {d} with item {item}.                 \033[F")
            print(f"Loading {d} throwable {item}                \033[F")
            for x in range(65,96):

                if item != "Hand":
                    assets_loaded +=1
                    character_animation[d]["throw_items"][item].append(pygame.image.load(f"images/characters/{ptype}/{d}/Throw/{item}/00{x}.png").convert_alpha())
        print(f"{item} item fully loaded.                      \033[F")
    
    for direction in directions:

        print(f"Loading {direction} throw...                         \033[F")
        for x in range(31):
            y = x + 45
            character_animation[direction]["throw"].append(pygame.image.load(f"images/characters/{ptype}/{direction}/Throw/00{y}.png").convert_alpha())
            assets_loaded +=1
            
    print(f"Loaded {assets_loaded} assets.                          ")
    
    return character_animation
# not yet used function or variable at its current state
def the_end(ending):
    pass
# loads room assets upon entering room. Can later be optimized to pre-load before starting the game to improve performance, or create an async function to not freeze the game during loading.
def change_location(room_change):
    if room_change == None:
        return None
    
    if room_change == "mainToCorOne":
        raw_main_room_img = pygame.image.load("images/enironment/Corridor1/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Corridor1/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Corridor1/Door_cover.png").convert_alpha()
    if room_change == "mainToCorTwo":
        raw_main_room_img = pygame.image.load("images/enironment/Corridor2/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Corridor2/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Corridor2/Door_cover.png").convert_alpha()
    if room_change == "mainToCorFour":
        raw_main_room_img = pygame.image.load("images/enironment/Corridor4/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Corridor4/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Corridor4/Door_cover.png").convert_alpha()
    if room_change == "mainToCorFive":
        raw_main_room_img = pygame.image.load("images/enironment/Corridor5/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Corridor5/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Corridor5/Door_cover.png").convert_alpha()

    if room_change == "CorOneToMain":
        raw_main_room_img = pygame.image.load("images/enironment/Main-Room/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Main-Room/Floor.png").convert_alpha()
        extra_cover_raw = None
    if room_change == "CorTwoToMain":
        raw_main_room_img = pygame.image.load("images/enironment/Main-Room/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Main-Room/Floor.png").convert_alpha()
        extra_cover_raw = None
    if room_change == "CorFourToMain":
        raw_main_room_img = pygame.image.load("images/enironment/Main-Room/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Main-Room/Floor.png").convert_alpha()
        extra_cover_raw = None
    if room_change == "CorFiveToMain":
        raw_main_room_img = pygame.image.load("images/enironment/Main-Room/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Main-Room/Floor.png").convert_alpha()
        extra_cover_raw = None

    if room_change == "CorOneToRoom1":
        raw_main_room_img = pygame.image.load("images/enironment/Room1/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Room1/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Room1/Door_cover.png").convert_alpha()
    if room_change == "CorTwoToRoom2":
        raw_main_room_img = pygame.image.load("images/enironment/Room2/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Room2/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Room2/Door_cover.png").convert_alpha()
    if room_change == "CorFourToRoom4":
        raw_main_room_img = pygame.image.load("images/enironment/Room4/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Room4/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Room4/Door_cover.png").convert_alpha()
    if room_change == "CorFiveToRoom5":
        raw_main_room_img = pygame.image.load("images/enironment/Room5/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Room5/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Room5/Door_cover.png").convert_alpha()

    if room_change == "Room1ToCorOne":
        raw_main_room_img = pygame.image.load("images/enironment/Corridor1/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Corridor1/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Corridor1/Door_cover.png").convert_alpha()
    if room_change == "Room2ToCorTwo":
        raw_main_room_img = pygame.image.load("images/enironment/Corridor2/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Corridor2/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Corridor2/Door_cover.png").convert_alpha()
    if room_change == "Room4ToCorFour":
        raw_main_room_img = pygame.image.load("images/enironment/Corridor4/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Corridor4/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Corridor4/Door_cover.png").convert_alpha()
    if room_change == "Room5ToCorFive":
        raw_main_room_img = pygame.image.load("images/enironment/Corridor5/Basic-View.png").convert_alpha()
        raw_main_room_floor_placeholder_img = pygame.image.load("images/enironment/Corridor5/Floor.png").convert_alpha()
        extra_cover_raw = pygame.image.load("images/enironment/Corridor5/Door_cover.png").convert_alpha()
    return raw_main_room_img, raw_main_room_floor_placeholder_img,extra_cover_raw
# function called for certain rooms only.
def update_images(raw_main_room_img, raw_main_room_floor_placeholder_img,extra_cover_raw):
    main_room_floor = pygame.transform.scale(raw_main_room_floor_placeholder_img,(width*2,height*2))
    if extra_cover_raw is not None:
        extra_cover =pygame.transform.scale(extra_cover_raw,(width*2,height*2))
    else:
        extra_cover = None
    return pygame.transform.scale(raw_main_room_img,(width*2,height*2)),main_room_floor, pygame.mask.from_surface(main_room_floor), extra_cover
# loads interact boxes for doors. and item interact hitboxes
def load_room_assets(current_room, meat_location, money_location, sword_location, key_location,thrown_item):
    door_1_interact_img, door_2_interact_img, door_3_interact_img, door_4_interact_img, door_5_interact_img, money_interact_img,money_interact1_img, money_interact2_img, money_interact3_img, money_interact4_img,meat_interact_img, meat_interact1_img, meat_interact2_img, meat_interact3_img, meat_interact4_img,sword_interact_img, sword_interact1_img, sword_interact2_img, sword_interact3_img, sword_interact4_img,key_interact_img, key_interact1_img, key_interact2_img, key_interact3_img, key_interact4_img, door_1_interact_mask, door_2_interact_mask, door_3_interact_mask, door_4_interact_mask, door_5_interact_mask,money_interact_mask, money_interact1_mask,money_interact2_mask,money_interact3_mask,money_interact4_mask,meat_interact_mask, meat_interact1_mask, meat_interact2_mask, meat_interact3_mask, meat_interact4_mask,sword_interact_mask, sword_interact1_mask, sword_interact2_mask, sword_interact3_mask, sword_interact4_mask,key_interact_mask,key_interact1_mask,key_interact2_mask,key_interact3_mask,key_interact4_mask = None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
    if current_room == "main":
        door_1_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Main-Room/Door1Hitbox.png").convert_alpha(),(width*2,height*2))
        door_1_interact_mask = pygame.mask.from_surface(door_1_interact_img)
        door_2_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Main-Room/Door2Hitbox.png").convert_alpha(),(width*2,height*2))
        door_2_interact_mask = pygame.mask.from_surface(door_2_interact_img)
        door_3_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Main-Room/Door3Hitbox.png").convert_alpha(),(width*2,height*2))
        door_3_interact_mask = pygame.mask.from_surface(door_3_interact_img)
        door_4_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Main-Room/Door4Hitbox.png").convert_alpha(),(width*2,height*2))
        door_4_interact_mask = pygame.mask.from_surface(door_4_interact_img)
        door_5_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Main-Room/Door5Hitbox.png").convert_alpha(),(width*2,height*2))
        door_5_interact_mask = pygame.mask.from_surface(door_5_interact_img)
    if current_room == "roomFive":
        door_1_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Room5/Door1Hitbox.png").convert_alpha(),(width*2,height*2))
        door_1_interact_mask = pygame.mask.from_surface(door_1_interact_img)
    if current_room == "roomFour":
        door_1_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Room4/Door1Hitbox.png").convert_alpha(),(width*2,height*2))
        door_1_interact_mask = pygame.mask.from_surface(door_1_interact_img)
    if current_room == "roomTwo":
        door_1_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Room2/Door1Hitbox.png").convert_alpha(),(width*2,height*2))
        door_1_interact_mask = pygame.mask.from_surface(door_1_interact_img)
    if current_room == "roomOne":
        door_1_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Room1/Door1Hitbox.png").convert_alpha(),(width*2,height*2))
        door_1_interact_mask = pygame.mask.from_surface(door_1_interact_img)
    if current_room == "corridorOne":
        door_1_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Corridor1/Door1Hitbox.png").convert_alpha(),(width*2,height*2))
        door_1_interact_mask = pygame.mask.from_surface(door_1_interact_img)
        door_2_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Corridor1/Door2Hitbox.png").convert_alpha(),(width*2,height*2))
        door_2_interact_mask = pygame.mask.from_surface(door_2_interact_img)
    if current_room == "corridorTwo": 
        door_1_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Corridor2/Door1Hitbox.png").convert_alpha(),(width*2,height*2))
        door_1_interact_mask = pygame.mask.from_surface(door_1_interact_img)
        door_2_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Corridor2/Door2Hitbox.png").convert_alpha(),(width*2,height*2))
        door_2_interact_mask = pygame.mask.from_surface(door_2_interact_img)
    if current_room == "corridorFour":
        door_1_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Corridor4/Door1Hitbox.png").convert_alpha(),(width*2,height*2))
        door_1_interact_mask = pygame.mask.from_surface(door_1_interact_img)
        door_2_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Corridor4/Door2Hitbox.png").convert_alpha(),(width*2,height*2))
        door_2_interact_mask = pygame.mask.from_surface(door_2_interact_img)
    if current_room == "corridorFive":
        door_1_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Corridor5/Door1Hitbox.png").convert_alpha(),(width*2,height*2))
        door_1_interact_mask = pygame.mask.from_surface(door_1_interact_img)
        door_2_interact_img  = pygame.transform.scale(pygame.image.load("images/enironment/Corridor5/Door2Hitbox.png").convert_alpha(),(width*2,height*2))
        door_2_interact_mask = pygame.mask.from_surface(door_2_interact_img)
    try:
        if money_location[0] == current_room or thrown_item == "Money":
            money_interact1_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox1.png").convert_alpha(),(width/2,height/2))
            money_interact1_mask = pygame.mask.from_surface(money_interact1_img)
            money_interact2_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox2.png").convert_alpha(),(width/2,height/2))
            money_interact2_mask = pygame.mask.from_surface(money_interact2_img)
            money_interact3_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox3.png").convert_alpha(),(width/2,height/2))
            money_interact3_mask = pygame.mask.from_surface(money_interact3_img)
            money_interact4_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox4.png").convert_alpha(),(width/2,height/2))
            money_interact4_mask = pygame.mask.from_surface(money_interact4_img)
            money_interact_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox.png").convert_alpha(),(width/2,height/2))
            money_interact_mask = pygame.mask.from_surface(money_interact_img)
    except:
        pass
    try:
        if sword_location[0] == current_room or thrown_item == "Sword":
            sword_interact1_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox1.png").convert_alpha(),(width/2,height/2))
            sword_interact1_mask = pygame.mask.from_surface(sword_interact1_img)
            sword_interact2_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox2.png").convert_alpha(),(width/2,height/2))
            sword_interact2_mask = pygame.mask.from_surface(sword_interact2_img)
            sword_interact3_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox3.png").convert_alpha(),(width/2,height/2))
            sword_interact3_mask = pygame.mask.from_surface(sword_interact3_img)
            sword_interact4_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox4.png").convert_alpha(),(width/2,height/2))
            sword_interact4_mask = pygame.mask.from_surface(sword_interact4_img)
            sword_interact_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox.png").convert_alpha(),(width/2,height/2))
            sword_interact_mask = pygame.mask.from_surface(sword_interact_img)
    except:
        pass
    try:
        if key_location[0] == current_room or thrown_item == "Key":
            key_interact1_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox1.png").convert_alpha(),(width/2,height/2))
            key_interact1_mask = pygame.mask.from_surface(key_interact1_img)
            key_interact2_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox2.png").convert_alpha(),(width/2,height/2))
            key_interact2_mask = pygame.mask.from_surface(key_interact2_img)
            key_interact3_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox3.png").convert_alpha(),(width/2,height/2))
            key_interact3_mask = pygame.mask.from_surface(key_interact3_img)
            key_interact4_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox4.png").convert_alpha(),(width/2,height/2))
            key_interact4_mask = pygame.mask.from_surface(key_interact4_img)
            key_interact_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox.png").convert_alpha(),(width/2,height/2))
            key_interact_mask = pygame.mask.from_surface(key_interact_img)
    except:
        pass
    try:
        if meat_location[0] == current_room or thrown_item == "Meat":
            meat_interact1_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox1.png").convert_alpha(),(width/2,height/2))
            meat_interact1_mask = pygame.mask.from_surface(meat_interact1_img)
            meat_interact2_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox2.png").convert_alpha(),(width/2,height/2))
            meat_interact2_mask = pygame.mask.from_surface(meat_interact2_img)
            meat_interact3_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox3.png").convert_alpha(),(width/2,height/2))
            meat_interact3_mask = pygame.mask.from_surface(meat_interact3_img)
            meat_interact4_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox4.png").convert_alpha(),(width/2,height/2))
            meat_interact4_mask = pygame.mask.from_surface(meat_interact4_img)
            meat_interact_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox.png").convert_alpha(),(width/2,height/2))
            meat_interact_mask = pygame.mask.from_surface(meat_interact_img)
    except:
        pass
    return door_1_interact_img, door_2_interact_img, door_3_interact_img, door_4_interact_img, door_5_interact_img, money_interact_img,money_interact1_img, money_interact2_img, money_interact3_img, money_interact4_img,meat_interact_img, meat_interact1_img, meat_interact2_img, meat_interact3_img, meat_interact4_img,sword_interact_img, sword_interact1_img, sword_interact2_img, sword_interact3_img, sword_interact4_img,key_interact_img, key_interact1_img, key_interact2_img, key_interact3_img, key_interact4_img, door_1_interact_mask, door_2_interact_mask, door_3_interact_mask, door_4_interact_mask, door_5_interact_mask,money_interact_mask, money_interact1_mask,money_interact2_mask,money_interact3_mask,money_interact4_mask,meat_interact_mask, meat_interact1_mask, meat_interact2_mask, meat_interact3_mask, meat_interact4_mask,sword_interact_mask, sword_interact1_mask, sword_interact2_mask, sword_interact3_mask, sword_interact4_mask,key_interact_mask,key_interact1_mask,key_interact2_mask,key_interact3_mask,key_interact4_mask
# detects collision between player, and door hitboxes, to check wether door can be opened or not. 
def interact_collison_detector(current_room, 
                               door_1_interact_rect, door_1_interact_mask, 
                               door_2_interact_rect, door_2_interact_mask, 
                               door_3_interact_rect, door_3_interact_mask, 
                               door_4_interact_rect, door_4_interact_mask, 
                               door_5_interact_rect, door_5_interact_mask, 
                               player_hitbox_rect, player_hitbox_mask,
                               hitbox_px_count):
    
        if door_1_interact_rect is not None and door_1_interact_mask is not None:
            offset = (player_hitbox_rect.x-door_1_interact_rect.x,player_hitbox_rect.y-door_1_interact_rect.y)
            overlap = door_1_interact_mask.overlap_area(player_hitbox_mask,offset)
            if overlap >= 0.5*hitbox_px_count:
                what = "unknown"
                if current_room == "main":
                    what= "DoorOneToCorOne"
                if current_room == "corridorOne" or current_room == "corridorTwo" or current_room == "corridorFour" or current_room == "corridorFive":
                    what= "DoorToMainRoom"
                if current_room == "roomOne" or current_room == "roomTwo" or current_room == "roomFour" or current_room == "roomFive":
                    what= "RoomToCorridor"
                return "door_1_interact",what    
        if door_2_interact_rect is not None and door_2_interact_mask is not None:
            offset = (player_hitbox_rect.x-door_2_interact_rect.x,player_hitbox_rect.y-door_2_interact_rect.y)
            overlap = door_2_interact_mask.overlap_area(player_hitbox_mask,offset)
            if overlap >= 0.5*hitbox_px_count:
                what = "unknown"
                if current_room == "main":
                    what= "DoorTwoToCorTwo"
                if current_room == "corridorOne" or current_room == "corridorTwo" or current_room == "corridorFour" or current_room == "corridorFive":
                    what= "DoorToRoom"
                return "door_2_interact",what    
        if door_3_interact_rect is not None and door_3_interact_mask is not None:
            offset = (player_hitbox_rect.x-door_3_interact_rect.x,player_hitbox_rect.y-door_3_interact_rect.y)
            overlap = door_3_interact_mask.overlap_area(player_hitbox_mask,offset)
            if overlap >= 0.5*hitbox_px_count:
                what = "unknown"
                if current_room == "main":
                    what= "DoorThreeToEscape"
                return "door_3_interact",what    
        if door_4_interact_rect is not None and door_4_interact_mask is not None:
            offset = (player_hitbox_rect.x-door_4_interact_rect.x,player_hitbox_rect.y-door_4_interact_rect.y)
            overlap = door_4_interact_mask.overlap_area(player_hitbox_mask,offset)
            if overlap >= 0.5*hitbox_px_count:
                what = "unknown"
                if current_room == "main":
                    what= "DoorFourToCorFour"
                return "door_4_interact",what  
              
        if door_5_interact_rect is not None and door_5_interact_mask is not None:
            offset = (player_hitbox_rect.x-door_5_interact_rect.x,player_hitbox_rect.y-door_5_interact_rect.y)
            overlap = door_5_interact_mask.overlap_area(player_hitbox_mask,offset)
            if overlap >= 0.5*hitbox_px_count:
                what = "unknown"
                if current_room == "main":
                    what= "DoorFiveToCorFive"
                return "door_5_interact",what    
        return None, None
# detects whether player hitbox is colliding with any of the item's hitboxes.
def item_collision_detector(money_interact_rect, money_interact_mask,
                            meat_interact_rect, meat_interact_mask,
                            sword_interact_rect, sword_interact_mask,
                            key_interact_rect, key_interact_mask,
                            player_hitbox_rect, player_hitbox_mask,
                            hitbox_px_count):
        if money_interact_rect is not None and money_interact_mask is not None:
            offset = (player_hitbox_rect.x-money_interact_rect.x,player_hitbox_rect.y-money_interact_rect.y)
            overlap = money_interact_mask.overlap_area(player_hitbox_mask,offset)
            if overlap >= 0.5*hitbox_px_count:
                what = "unknown"
                # returns money_interact if it can be picked up
                return "money_interact" 
        if meat_interact_rect is not None and meat_interact_mask is not None:
            offset = (player_hitbox_rect.x-meat_interact_rect.x,player_hitbox_rect.y-meat_interact_rect.y)
            overlap = meat_interact_mask.overlap_area(player_hitbox_mask,offset)
            if overlap >= 0.5*hitbox_px_count:
                what = "unknown"
                return "meat_interact"   
        if sword_interact_rect is not None and sword_interact_mask is not None:
            offset = (player_hitbox_rect.x-sword_interact_rect.x,player_hitbox_rect.y-sword_interact_rect.y)
            overlap = sword_interact_mask.overlap_area(player_hitbox_mask,offset)
            if overlap >= 0.5*hitbox_px_count:
                what = "unknown"
                return "sword_interact"  
        if key_interact_rect is not None and key_interact_mask is not None:
            offset = (player_hitbox_rect.x-key_interact_rect.x,player_hitbox_rect.y-key_interact_rect.y)
            overlap = key_interact_mask.overlap_area(player_hitbox_mask,offset)
            if overlap >= 0.5*hitbox_px_count:
                what = "unknown"
                return "key_interact"
        return None
# function loads item interact hitboxes, independently of the load_room_assets function
def load_item_assets(current_room, meat_location, money_location, sword_location, key_location,thrown_item):
    money_interact_img,money_interact1_img, money_interact2_img, money_interact3_img, money_interact4_img,meat_interact_img, meat_interact1_img, meat_interact2_img, meat_interact3_img, meat_interact4_img,sword_interact_img, sword_interact1_img, sword_interact2_img, sword_interact3_img, sword_interact4_img,key_interact_img, key_interact1_img, key_interact2_img, key_interact3_img, key_interact4_img = None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
    money_interact_mask,money_interact1_mask, money_interact2_mask, money_interact3_mask, money_interact4_mask,meat_interact_mask, meat_interact1_mask, meat_interact2_mask, meat_interact3_mask, meat_interact4_mask,sword_interact_mask, sword_interact1_mask, sword_interact2_mask, sword_interact3_mask, sword_interact4_mask,key_interact_mask, key_interact1_mask, key_interact2_mask, key_interact3_mask, key_interact4_mask = None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None

    if money_location != "inventory" or thrown_item == "Money":
        if  money_location[0] == current_room or thrown_item == "Money":
            money_interact1_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox1.png").convert_alpha(),(width/2,height/2))
            money_interact1_mask = pygame.mask.from_surface(money_interact1_img)
            money_interact2_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox2.png").convert_alpha(),(width/2,height/2))
            money_interact2_mask = pygame.mask.from_surface(money_interact2_img)
            money_interact3_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox3.png").convert_alpha(),(width/2,height/2))
            money_interact3_mask = pygame.mask.from_surface(money_interact3_img)
            money_interact4_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox4.png").convert_alpha(),(width/2,height/2))
            money_interact4_mask = pygame.mask.from_surface(money_interact4_img)
            money_interact_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox.png").convert_alpha(),(width/2,height/2))
            money_interact_mask = pygame.mask.from_surface(money_interact_img)
    else:
        pass
    if sword_location != "inventory" or thrown_item == "Sword":
        if  sword_location[0] == current_room or thrown_item == "Sword":
            sword_interact1_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox1.png").convert_alpha(),(width/2,height/2))
            sword_interact1_mask = pygame.mask.from_surface(sword_interact1_img)
            sword_interact2_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox2.png").convert_alpha(),(width/2,height/2))
            sword_interact2_mask = pygame.mask.from_surface(sword_interact2_img)
            sword_interact3_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox3.png").convert_alpha(),(width/2,height/2))
            sword_interact3_mask = pygame.mask.from_surface(sword_interact3_img)
            sword_interact4_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox4.png").convert_alpha(),(width/2,height/2))
            sword_interact4_mask = pygame.mask.from_surface(sword_interact4_img)
            sword_interact_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox.png").convert_alpha(),(width/2,height/2))
            sword_interact_mask = pygame.mask.from_surface(sword_interact_img)
    else:
        pass
    if key_location != "inventory" or thrown_item == "Key":
        if key_location[0] == current_room or thrown_item == "Key":
            key_interact1_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox1.png").convert_alpha(),(width/2,height/2))
            key_interact1_mask = pygame.mask.from_surface(key_interact1_img)
            key_interact2_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox2.png").convert_alpha(),(width/2,height/2))
            key_interact2_mask = pygame.mask.from_surface(key_interact2_img)
            key_interact3_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox3.png").convert_alpha(),(width/2,height/2))
            key_interact3_mask = pygame.mask.from_surface(key_interact3_img)
            key_interact4_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox4.png").convert_alpha(),(width/2,height/2))
            key_interact4_mask = pygame.mask.from_surface(key_interact4_img)
            key_interact_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox.png").convert_alpha(),(width/2,height/2))
            key_interact_mask = pygame.mask.from_surface(key_interact_img)
    else:
        pass
    if meat_location != "inventory" or thrown_item == "Meat":
        if  meat_location[0] == current_room or thrown_item == "Meat":
            meat_interact1_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox1.png").convert_alpha(),(width/2,height/2))
            meat_interact1_mask = pygame.mask.from_surface(meat_interact1_img)
            meat_interact2_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox2.png").convert_alpha(),(width/2,height/2))
            meat_interact2_mask = pygame.mask.from_surface(meat_interact2_img)
            meat_interact3_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox3.png").convert_alpha(),(width/2,height/2))
            meat_interact3_mask = pygame.mask.from_surface(meat_interact3_img)
            meat_interact4_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox4.png").convert_alpha(),(width/2,height/2))
            meat_interact4_mask = pygame.mask.from_surface(meat_interact4_img)
            meat_interact_img =pygame.transform.scale(pygame.image.load(f"images/characters/basic/Item_thrown_hitbox.png").convert_alpha(),(width/2,height/2))
            meat_interact_mask = pygame.mask.from_surface(meat_interact_img)
    else:
        pass
    return money_interact_img,money_interact1_img, money_interact2_img, money_interact3_img, money_interact4_img,meat_interact_img, meat_interact1_img, meat_interact2_img, meat_interact3_img, meat_interact4_img,sword_interact_img, sword_interact1_img, sword_interact2_img, sword_interact3_img, sword_interact4_img,key_interact_img, key_interact1_img, key_interact2_img, key_interact3_img, key_interact4_img,money_interact_mask, money_interact1_mask, money_interact2_mask, money_interact3_mask, money_interact4_mask,meat_interact_mask, meat_interact1_mask, meat_interact2_mask, meat_interact3_mask, meat_interact4_mask,sword_interact_mask, sword_interact1_mask, sword_interact2_mask, sword_interact3_mask, sword_interact4_mask,key_interact_mask, key_interact1_mask, key_interact2_mask, key_interact3_mask, key_interact4_mask 
# calls load_room_assets function, and returned values assigned to the below varibles.
door_1_interact_img, door_2_interact_img, door_3_interact_img, door_4_interact_img, door_5_interact_img, money_interact_img,money_interact1_img, money_interact2_img, money_interact3_img, money_interact4_img,meat_interact_img, meat_interact1_img, meat_interact2_img, meat_interact3_img, meat_interact4_img,sword_interact_img, sword_interact1_img, sword_interact2_img, sword_interact3_img, sword_interact4_img,key_interact_img, key_interact1_img, key_interact2_img, key_interact3_img, key_interact4_img, door_1_interact_mask, door_2_interact_mask, door_3_interact_mask, door_4_interact_mask, door_5_interact_mask,money_interact_mask, money_interact1_mask,money_interact2_mask,money_interact3_mask,money_interact4_mask,meat_interact_mask, meat_interact1_mask, meat_interact2_mask, meat_interact3_mask, meat_interact4_mask,sword_interact_mask, sword_interact1_mask, sword_interact2_mask, sword_interact3_mask, sword_interact4_mask,key_interact_mask,key_interact1_mask,key_interact2_mask,key_interact3_mask,key_interact4_mask=load_room_assets(current_room, meat_location, money_location, sword_location, key_location,thrown_item)
# the main game loop
while running:  

    if semi_throwing:
        semi_throwing = False
        throwing = True
    changing_room = False
    # checks if character is in new room compared to previous frame, if yes, it will load the new room
    if past_room != current_room:
        if past_room == "main": 
            if current_room == "corridorOne":
                room_change = "mainToCorOne"
            if current_room == "corridorTwo":
                room_change = "mainToCorTwo"
            if current_room == "corridorFour":
                room_change = "mainToCorFour"
            if current_room == "corridorFive":
                room_change = "mainToCorFive"
                

        if past_room == "corridorOne":
            if current_room == "main":
                room_change = "CorOneToMain"
            if current_room == "roomOne":
                room_change = "CorOneToRoom1"

        if past_room == "corridorTwo":
            if current_room == "main":
                room_change = "CorTwoToMain"
            if current_room == "roomTwo":
                room_change = "CorTwoToRoom2"

        if past_room == "corridorFour":
            if current_room == "main":
                room_change = "CorFourToMain"
            if current_room == "roomFour":
                room_change = "CorFourToRoom4"

        if past_room == "corridorFive":
            if current_room == "main":
                room_change = "CorFiveToMain"
            if current_room == "roomFive":
                room_change = "CorFiveToRoom5"


        if past_room == "roomOne":
            room_change = "Room1ToCorOne"

        if past_room == "roomTwo":
            room_change = "Room2ToCorTwo"

        if past_room == "roomFour":
            room_change = "Room4ToCorFour"

        if past_room == "roomFive":
            room_change = "Room5ToCorFive"
        # function calling and new value assigning :)
        raw_main_room_img,raw_main_room_floor_placeholder_img, extra_cover_raw = change_location(room_change)
        main_room_img, main_room_floor, floor_mask,extra_cover = update_images(raw_main_room_img,raw_main_room_floor_placeholder_img,extra_cover_raw)
        door_1_interact_img, door_2_interact_img, door_3_interact_img, door_4_interact_img, door_5_interact_img, money_interact_img,money_interact1_img, money_interact2_img, money_interact3_img, money_interact4_img,meat_interact_img, meat_interact1_img, meat_interact2_img, meat_interact3_img, meat_interact4_img,sword_interact_img, sword_interact1_img, sword_interact2_img, sword_interact3_img, sword_interact4_img,key_interact_img, key_interact1_img, key_interact2_img, key_interact3_img, key_interact4_img, door_1_interact_mask, door_2_interact_mask, door_3_interact_mask, door_4_interact_mask, door_5_interact_mask,money_interact_mask, money_interact1_mask,money_interact2_mask,money_interact3_mask,money_interact4_mask,meat_interact_mask, meat_interact1_mask, meat_interact2_mask, meat_interact3_mask, meat_interact4_mask,sword_interact_mask, sword_interact1_mask, sword_interact2_mask, sword_interact3_mask, sword_interact4_mask,key_interact_mask,key_interact1_mask,key_interact2_mask,key_interact3_mask,key_interact4_mask= load_room_assets(current_room, meat_location, money_location, sword_location, key_location,thrown_item)
    past_room = current_room
    # loads character animations if they are not loaded yet. this only runs once per game for now.
    if character_animation["loaded"] == False:
        character_animation = load_animations(ptype)
    if punched:
        punch_frame +=1
        character_animation_on = True
    if punch_frame == 31:
        punched = False  
        punch_frame = 0
        character_animation_on = False
    if moving and not character_animation_on:
        moved_for += 1
        if moved_for == 30:
            moved_for = 0
    else:
        moved_for = 0
    if throwing or thrown:
        if thrown_direction == "east":
            thrown_movement = [1,-1]
        if thrown_direction == "north-east":
            thrown_movement = [0,-1]
        if thrown_direction == "north":
            thrown_movement = [-1,-1]
        if thrown_direction == "north-west":
            thrown_movement = [-1,0]
        if thrown_direction == "west":
            thrown_movement = [-1,1]
        if thrown_direction == "south-west":
            thrown_movement = [0,1]
        if thrown_direction == "south":
            thrown_movement = [1,1]
        if thrown_direction == "south-east":
            thrown_movement = [1,0]
        character_item_thrown_frame +=1
        character_thrown_frame +=1 
    if character_thrown_frame == 20:
        thrown = True
        character_item_thrown_frame = 0
    if character_thrown_frame == 30:
        throwing = False
    if character_thrown_frame == 50:
        thrown = False
        throwing = False
        character_thrown_frame = 0
        character_item_thrown_frame = 0
        character_animation_on = False
        if thrown_item == "Key":
            key_location = [current_room, [-map_pos_x+thrown_position[0],-map_pos_y+thrown_position[1]], thrown_direction]
        if thrown_item == "Sword":
            sword_location = [current_room, [-map_pos_x+thrown_position[0],-map_pos_y+thrown_position[1]], thrown_direction]
        if thrown_item == "Meat":
            meat_location = [current_room, [-map_pos_x+thrown_position[0],-map_pos_y+thrown_position[1]], thrown_direction]
        if thrown_item == "Money":
            money_location = [current_room, [-map_pos_x+thrown_position[0],-map_pos_y+thrown_position[1]], thrown_direction]
        money_interact_img,money_interact1_img, money_interact2_img, money_interact3_img, money_interact4_img,meat_interact_img, meat_interact1_img, meat_interact2_img, meat_interact3_img, meat_interact4_img,sword_interact_img, sword_interact1_img, sword_interact2_img, sword_interact3_img, sword_interact4_img,key_interact_img, key_interact1_img, key_interact2_img, key_interact3_img, key_interact4_img,money_interact_mask, money_interact1_mask, money_interact2_mask, money_interact3_mask, money_interact4_mask,meat_interact_mask, meat_interact1_mask, meat_interact2_mask, meat_interact3_mask, meat_interact4_mask,sword_interact_mask, sword_interact1_mask, sword_interact2_mask, sword_interact3_mask, sword_interact4_mask,key_interact_mask, key_interact1_mask, key_interact2_mask, key_interact3_mask, key_interact4_mask  = load_item_assets(current_room=current_room,
                         meat_location=meat_location,
                         money_location=money_location,
                         sword_location=sword_location,
                         key_location=key_location,
                         thrown_item=thrown_item)
        
        thrown_interact_rect = None
        thrown_interact_mask = None
        thrown_interact_image = None
        
        thrown_interact1_rect = None
        thrown_interact1_mask = None
        thrown_interact1_image = None
        thrown_interact2_rect = None
        thrown_interact2_mask = None
        thrown_interact2_image = None
        thrown_interact3_rect = None
        thrown_interact3_mask = None
        thrown_interact3_image = None
        thrown_interact4_rect = None
        thrown_interact4_mask = None
        thrown_interact4_image = None
    
    width = screen.get_width()
    height = screen.get_height()
    player_y_position_multiplier = overall_y
    for event in pygame.event.get():
        #detecting events
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # selecting new items
                mouse_pos =pygame.mouse.get_pos() 
                if mouse_pos[0] > inventory_pos[0] + 5 and mouse_pos[0] <= inventory_pos[0] + 64 and mouse_pos[1] > inventory_pos[1] + 59 and mouse_pos[1] <= inventory_pos[1] + 121:
                    inventory_selected = "1"
                    itemInhand = "Hand"
                if mouse_pos[0] > inventory_pos[0] + 64 and mouse_pos[0] <= inventory_pos[0] + 120 and mouse_pos[1] > inventory_pos[1] + 59 and mouse_pos[1] <= inventory_pos[1] + 121:
                    if money_location == "inventory":
                        inventory_selected = "2"
                        itemInhand = "Money"
                if mouse_pos[0] > inventory_pos[0] + 120 and mouse_pos[0] <= inventory_pos[0] + 175 and mouse_pos[1] > inventory_pos[1] + 59 and mouse_pos[1] <= inventory_pos[1] + 121:
                    if meat_location == "inventory":
                        inventory_selected = "3"
                        itemInhand = "Meat"
                if mouse_pos[0] > inventory_pos[0] + 175 and mouse_pos[0] <= inventory_pos[0] + 232 and mouse_pos[1] > inventory_pos[1] + 59 and mouse_pos[1] <= inventory_pos[1] + 121:
                    if sword_location == "inventory":
                        inventory_selected = "4"
                        itemInhand = "Sword"
                if mouse_pos[0] > inventory_pos[0] + 232 and mouse_pos[0] <= inventory_pos[0] + 289 and mouse_pos[1] > inventory_pos[1] + 59 and mouse_pos[1] <= inventory_pos[1] + 121:
                    if key_location == "inventory":
                        inventory_selected = "5"
                        itemInhand = "Key"
                # punching character
                if player_real_hitbox_rect.collidepoint(mouse_pos):
                    local_x = mouse_pos[0] - player_real_hitbox_rect[0]
                    local_y = mouse_pos[1] - player_real_hitbox_rect[1]
                    #checks if hitbox was clicked
                    if player_real_hitbox_mask.get_at((local_x, local_y)):
                        punched = True
                        punched_direction = direction
                        character_animation_on = True
        if event.type == pygame.KEYDOWN and not punched and not character_animation_on:
            # going through doors
            if event.key == pygame.K_e:
                if collison is not None:
                    changing_room = True
                    # checking if which, if any, of the doors the character was in the hitbox in.
                    if collision_with == "DoorOneToCorOne":
                        current_room = "corridorOne"
                        player_x= 835.2015165544193                        
                        player_y= 300.0                        
                        map_pos_y= -498.0590934951555                        
                        map_pos_x= -553.3325634959601                        
                        overall_y= 1.1593415295852978                        
                        player_w= 463                        
                        player_h= 278
                    if collision_with == "DoorTwoToCorTwo":
                        current_room = "corridorTwo"
                        player_x= 703.6847258396973                         
                        player_y= 386.663051363206                        
                        map_pos_y= -543.6131994295507                         
                        map_pos_x= -553.0423157077254                         
                        overall_y= 1.2334193596034586                        
                        player_w= 493                        
                        player_h= 296 

                    if collision_with == "DoorThreeToEscape":
                        if itemInhand == "Key":
                            print("Escaped")
                        else: 
                            print("Locked door.")
                    if collision_with == "DoorFourToCorFour":
                        current_room = "corridorFour"
                        player_x= 123.17210410959154                        
                        player_y= 421.0577999078887                        
                        map_pos_y= -540.6179391792833                         
                        map_pos_x= -419.0459566926709                         
                        overall_y= 1.2507911839130785                        
                        player_w= 500                        
                        player_h= 300

                    if collision_with == "DoorFiveToCorFive":
                        current_room = "corridorFive"
                        player_x= 74.21684712091076                         
                        player_y= 399.44033563862286                        
                        map_pos_y= -540.6179391792833                         
                        map_pos_x= -419.0459566926709                         
                        overall_y= 1.2383579707193109                        
                        player_w= 495                        
                        player_h= 297

                    if collision_with == "DoorToMainRoom":
                        if current_room == "corridorOne":                                      
                            player_x= 248.80942039007914                         
                            player_y= 300.0                                      
                            map_pos_y= -186.66956910370155                        
                            map_pos_x= -418.65419073602783                        
                            overall_y= 0.9920398405582133                        
                            player_w= 396                        
                            player_h= 238
                        if current_room == "corridorTwo":
                            player_x= 704.3689606736817
                            player_y= 377.9797124854854
                            player_x= 455.129802721484577
                            player_y= 300.0
                            map_pos_y= -98.76909195266617
                            map_pos_x= -419.0879232599439
                            overall_y= 0.9231901003210928
                        if current_room == "corridorFour":
                            player_x= 703.4343008628653                        
                            player_y= 300.0                        
                            map_pos_y= -134.41516074634725                        
                            map_pos_x= -554.4712426524202                        
                            overall_y= 0.9589100003304616                        
                            player_w= 383                        
                            player_h= 230 
                        if current_room == "corridorFive":                            
                            player_x= 837.1051165668023                           
                            player_y= 300.0                                      
                            map_pos_y= -266.2819695751377                        
                            map_pos_x= -554.4712426524202                        
                            overall_y= 1.0407691980186191                        
                            player_w= 416                        
                            player_h= 249
                        current_room = "main"
                    if collision_with == "DoorToRoom":
                        if current_room == "corridorOne":
                            current_room = "roomOne"
                            player_x= 292.2171863259885
                            player_y= 408.0805764675304
                            map_pos_y= -540.5342817678109
                            map_pos_x= -419.27913531917886
                            overall_y= 1.243316356034071
                            player_w= 497
                            player_h= 298
                        if current_room == "corridorTwo":
                            current_room = "roomTwo"
                            player_x= 292.2171863259885
                            player_y= 408.0805764675304
                            map_pos_y= -540.5342817678109
                            map_pos_x= -419.27913531917886
                            overall_y= 1.243316356034071
                            player_w= 497
                            player_h= 298
                        if current_room == "corridorFour":
                            current_room = "roomFour"
                            player_x= 292.2171863259885
                            player_y= 408.0805764675304
                            map_pos_y= -540.5342817678109
                            map_pos_x= -419.27913531917886
                            overall_y= 1.243316356034071
                            player_w= 497
                            player_h= 298
                        if current_room == "corridorFive":
                            current_room = "roomFive"    
                            player_x= 292.2171863259885
                            player_y= 408.0805764675304
                            map_pos_y= -540.5342817678109
                            map_pos_x= -419.27913531917886
                            overall_y= 1.243316356034071
                            player_w= 497
                            player_h= 298
                    if collision_with == "RoomToCorridor":
                        if current_room == "roomFive":
                            current_room = "corridorFive" 
                            player_x= 720.7704741841684
                            player_y= 300.0
                            map_pos_y= -167.42177772722084
                            map_pos_x= -553.2542784303666
                            overall_y= 0.9666043248723577
                            player_w= 386
                            player_h= 231
                        if current_room == "roomFour":
                            current_room = "corridorFour"
                            player_x= 705.6083085159016
                            player_y= 300.0
                            map_pos_y= -155.00227784884493
                            map_pos_x= -550.1404363973642
                            overall_y= 0.9589100003292531
                            player_w= 383
                            player_h= 230
                        if current_room == "roomTwo":
                            current_room = "corridorTwo"
                            player_x= 393.630958134616
                            player_y= 300.0
                            map_pos_y= -71.54660291278176
                            map_pos_x= -416.34405277332985
                            overall_y= 0.8923595436508387
                            player_w= 356
                            player_h= 214
                        if current_room == "roomOne":
                            current_room = "corridorOne"
                            player_x= 236.11522122470845
                            player_y= 300.0
                            map_pos_y= -80.85764863444135
                            map_pos_x= -416.5831790585421
                            overall_y= 0.9121889553502356
                            player_w= 364
                            player_h= 218
            # attempts to pick up items
            if event.key == pygame.K_f:
                # checks which items character can pick up
                if item_collison == "key_interact":
                    key_location = "inventory"
                    itemInhand = "Key"
                    inventory_selected = "5"
                    key_interact_img = None
                    key_interact_rect = None
                    key_interact_mask = None
                if item_collison == "sword_interact":
                    itemInhand = "Sword"
                    sword_location = "inventory"
                    inventory_selected = "4"
                    sword_interact_img = None
                    sword_interact_rect = None
                    sword_interact_mask = None
                if item_collison == "meat_interact":
                    itemInhand = "Meat"
                    meat_location = "inventory"
                    inventory_selected = "3"
                    meat_interact_img = None
                    meat_interact_rect = None
                    meat_interact_mask = None
                if item_collison == "money_interact":
                    itemInhand = "Money"
                    money_location = "inventory"
                    inventory_selected = "2"
                    money_interact_img = None
                    money_interact_rect = None
                    money_interact_mask = None
            # throws/drops items
            if event.key == pygame.K_o:
                # cannot throw the hand
                if itemInhand != "Hand":
                    thrown_item = itemInhand
                    thrown_direction = direction
                    semi_throwing = True
                    character_animation_on = True
                    itemInhand = "Hand"
                    inventory_selected = "1"
                    thrown_position = [player_x-width/4,player_y-height/4]
                    money_interact_img,money_interact1_img, money_interact2_img, money_interact3_img, money_interact4_img,meat_interact_img, meat_interact1_img, meat_interact2_img, meat_interact3_img, meat_interact4_img,sword_interact_img, sword_interact1_img, sword_interact2_img, sword_interact3_img, sword_interact4_img,key_interact_img, key_interact1_img, key_interact2_img, key_interact3_img, key_interact4_img,money_interact_mask, money_interact1_mask, money_interact2_mask, money_interact3_mask, money_interact4_mask,meat_interact_mask, meat_interact1_mask, meat_interact2_mask, meat_interact3_mask, meat_interact4_mask,sword_interact_mask, sword_interact1_mask, sword_interact2_mask, sword_interact3_mask, sword_interact4_mask,key_interact_mask, key_interact1_mask, key_interact2_mask, key_interact3_mask, key_interact4_mask = load_item_assets(current_room, meat_location, money_location, sword_location, key_location,thrown_item)
    # movement
    keys = pygame.key.get_pressed()
    if not keys[pygame.K_a] and not keys[pygame.K_d] and not character_animation_on:
        movement[0] = 0
    if not keys[pygame.K_w] and not keys[pygame.K_s]and not character_animation_on:
        movement[1] = 0
    if keys[pygame.K_a] and not character_animation_on:
        movement[0] = 1
    if keys[pygame.K_d] and not character_animation_on:
        movement[0] = -1
    if keys[pygame.K_w] or punched:
        movement[1] = 1
    if keys[pygame.K_s] and not character_animation_on:
        movement[1] = -1

    if keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_w]:
        moving = True
    else:
        moving = False
    if punched:
        moving = False
    map_h = height*2*(abs(map_pos_y)+og_map_y+height)/height
    screen.fill((20,20,20))
    if movement == [1,0]:
        direction = "north-west"
    if movement == [-1,0]:
        direction = "south-east"
    if movement == [1,1]:
        direction = "north"
    if movement == [1,-1]:
        direction = "west"
    if movement == [-1,1]:
        direction = "east"
    if movement == [-1,-1]:
        direction = "south"
    if movement == [0,-1]:
        direction = "south-west"
    if movement == [0,1]:
        direction = "north-east"
    if punched:
        direction=punched_direction
    
    player_w,player_h = int((width*player_y_position_multiplier)/2.5), int((height*player_y_position_multiplier)/2.5)
    
    if moving or punched:
        before_last_pos= last_position
        before_last_overall_y = last_overall_y
        map_last_pos = (map_pos_x,map_pos_y)
        last_position = (player_x,player_y)
        last_overall_y = overall_y
        if movement[0] ==-1: 
            if map_pos_x+width*0.25>=-width*0.3 and player_x == width//2: #d
                map_pos_x += 3*movement[0]*((map_pos_y+map_h)/height)
            else:
                player_x += 3*-movement[0]*((map_pos_y+map_h)/height)
        if movement[0] ==1: #a
            if map_pos_x+width*1.5<=width*1.08 and player_x == width//2:
                map_pos_x += 3*movement[0]*((map_pos_y+map_h)/height)
            else:
                player_x += 3*-movement[0]*((map_pos_y+map_h)/height)
        if movement[1] ==-1: #s
            if map_pos_y-height*0.1>=-height and player_y == height//2:
                map_pos_y += 1.935*movement[1]*((map_pos_y+map_h)/height)
                overall_y *= 1.002
            else:
                player_y += -1.935*movement[1]*((map_pos_y+map_h)/height)
                overall_y *= 1.002
        if movement[1] ==1: #w
            if map_pos_y<=-0.12*height and player_y == height//2:
                map_pos_y += 1.935*movement[1]*((map_pos_y+map_h)/height)
                overall_y /= 1.002
            else:
                player_y += -1.935*movement[1]*((map_pos_y+map_h)/height)
                overall_y /= 1.002
    # throwing nd logic to check for wall collisions. in case of wall collision determines which way thrown item wil bounce of wall dependign on shape of wall, and the direction in which it was thrown
    if throwing:
        last_thrown_position = thrown_position.copy()
        if thrown_movement[0] ==-1: #d
            thrown_position[0] += thrown_movement[0]*7
        if thrown_movement[0] ==1: #a
            thrown_position[0] += thrown_movement[0]*7
        if thrown_movement[1] ==-1: #s
            thrown_position[1] += thrown_movement[1]*7
        if thrown_movement[1] ==1: #w
            thrown_position[1] += thrown_movement[1]*7
        thrown_interact_rect = None
        thrown_interact_mask = None
        thrown_interact_image = None
        item_collision_with_wall = False
        if  money_interact_img is not None or meat_interact_img is not None or sword_interact_img is not None or key_interact_img is not None:
            if thrown_item == "Money" and money_interact_img is not None:
                thrown_interact_rect = money_interact_img.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                thrown_interact_image = money_interact_img.copy()
                thrown_interact_mask = money_interact_mask.copy()
            if thrown_item == "Meat" and meat_interact_img is not None:
                thrown_interact_rect = meat_interact_img.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                thrown_interact_image = meat_interact_img.copy()
                thrown_interact_mask = meat_interact_mask.copy()
            if thrown_item == "Key" and key_interact_img is not None:
                thrown_interact_rect = key_interact_img.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                thrown_interact_image = key_interact_img.copy()
                thrown_interact_mask = key_interact_mask.copy()
            if thrown_item == "Sword" and sword_interact_img is not None:
                thrown_interact_image = sword_interact_img.copy()
                thrown_interact_rect = sword_interact_img.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                thrown_interact_mask = sword_interact_mask.copy()
            if thrown_interact_mask is not None:
                thrown_interact_pixel_count =thrown_interact_mask.count()
            if thrown_interact_rect != None:
                offset = (thrown_interact_rect.x-floor_rect.x,thrown_interact_rect.y-floor_rect.y)
                item_overlap = floor_mask.overlap_area(thrown_interact_mask,offset)
                if item_overlap <0.8*thrown_interact_pixel_count: #asda
                    item_collision_with_wall = True
                else:
                    item_collision_with_wall = False
                if item_collision_with_wall:
                    thrown_interact1_image = None
                    thrown_interact1_mask = None
                    thrown_interact1_rect = None
                    thrown_interact2_image = None
                    thrown_interact2_mask = None
                    thrown_interact2_rect = None
                    thrown_interact3_image = None
                    thrown_interact3_mask = None
                    thrown_interact3_rect = None
                    thrown_interact4_image = None
                    thrown_interact4_mask = None
                    thrown_interact4_rect = None
                    selected = False
                    if thrown_item == "Money":
                        selected = True
                        thrown_interact1_image = money_interact1_img.copy()
                        thrown_interact1_rect = thrown_interact1_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact1_mask = money_interact1_mask.copy()
                        thrown_interact2_image = money_interact2_img.copy()
                        thrown_interact2_rect = thrown_interact2_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact2_mask = money_interact2_mask.copy()
                        thrown_interact3_image = money_interact3_img.copy()
                        thrown_interact3_rect = thrown_interact3_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact3_mask = money_interact3_mask.copy()
                        thrown_interact4_image = money_interact4_img.copy()
                        thrown_interact4_rect = thrown_interact4_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact4_mask = money_interact4_mask.copy()
                    if thrown_item == "Sword":
                        selected = True
                        thrown_interact1_image = sword_interact1_img.copy()
                        thrown_interact1_rect = thrown_interact1_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact1_mask = sword_interact1_mask.copy()
                        thrown_interact2_image = sword_interact2_img.copy()
                        thrown_interact2_rect = thrown_interact2_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact2_mask = sword_interact2_mask.copy()
                        thrown_interact3_image = sword_interact3_img.copy()
                        thrown_interact3_rect = thrown_interact3_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact3_mask = sword_interact3_mask.copy()
                        thrown_interact4_image = sword_interact4_img.copy()
                        thrown_interact4_rect = thrown_interact4_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact4_mask = sword_interact4_mask.copy()
                    if thrown_item == "Key":
                        selected = True
                        thrown_interact1_image = key_interact1_img.copy()
                        thrown_interact1_rect = thrown_interact1_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact1_mask = key_interact1_mask.copy()
                        thrown_interact2_image = key_interact2_img.copy()
                        thrown_interact2_rect = thrown_interact2_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact2_mask = key_interact2_mask.copy()
                        thrown_interact3_image = key_interact3_img.copy()
                        thrown_interact3_rect = thrown_interact3_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact3_mask = key_interact3_mask.copy()
                        thrown_interact4_image = key_interact4_img.copy()
                        thrown_interact4_rect = thrown_interact4_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact4_mask = key_interact4_mask.copy()
                    if thrown_item == "Meat":
                        selected = True
                        thrown_interact1_image = meat_interact1_img.copy()
                        thrown_interact1_rect = thrown_interact1_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact1_mask = meat_interact1_mask.copy()
                        thrown_interact2_image = meat_interact2_img.copy()
                        thrown_interact2_rect = thrown_interact2_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact2_mask = meat_interact2_mask.copy()
                        thrown_interact3_image = meat_interact3_img.copy()
                        thrown_interact3_rect = thrown_interact3_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact3_mask = meat_interact3_mask.copy()
                        thrown_interact4_image = meat_interact4_img.copy()
                        thrown_interact4_rect = thrown_interact4_image.get_rect(topleft=(thrown_position[0],thrown_position[1]))
                        thrown_interact4_mask = meat_interact4_mask.copy()
                    if selected:
                        offset1 = (thrown_interact1_rect.x-floor_rect.x,thrown_interact1_rect.y-floor_rect.y)
                        offset2 = (thrown_interact2_rect.x-floor_rect.x,thrown_interact2_rect.y-floor_rect.y)
                        offset3 = (thrown_interact3_rect.x-floor_rect.x,thrown_interact3_rect.y-floor_rect.y)
                        offset4 = (thrown_interact4_rect.x-floor_rect.x,thrown_interact4_rect.y-floor_rect.y)
                        item1_overlap = floor_mask.overlap_area(thrown_interact1_mask,offset)
                        item2_overlap = floor_mask.overlap_area(thrown_interact2_mask,offset)
                        item3_overlap = floor_mask.overlap_area(thrown_interact3_mask,offset)
                        item4_overlap = floor_mask.overlap_area(thrown_interact4_mask,offset)
                        item1_collision = False
                        item2_collision = False
                        item3_collision = False
                        item4_collision = False
                        thrown_interact1_pixel_count =thrown_interact1_mask.count()
                        thrown_interact2_pixel_count =thrown_interact2_mask.count()
                        thrown_interact3_pixel_count =thrown_interact3_mask.count()
                        thrown_interact4_pixel_count =thrown_interact4_mask.count()
                        if item1_overlap <0.8*thrown_interact1_pixel_count:
                            item1_collision = True
                        else:
                            item1_collision = False
                        if item2_overlap <0.8*thrown_interact2_pixel_count:
                            item2_collision = True
                        else:
                            item2_collision = False
                        if item3_overlap <0.8*thrown_interact3_pixel_count:
                            item3_collision = True
                        else:
                            item3_collision = False
                        if item4_overlap <0.8*thrown_interact4_pixel_count:
                            item4_collision = True
                        else:
                            item4_collision = False
                        if item1_collision and not item2_collision and not item3_collision and not item4_collision:
                            if thrown_direction == "east":
                                thrown_direction = "west"

                            if thrown_direction == "north-east":
                                thrown_direction = "north-west"
                            if thrown_direction == "south-east":
                                thrown_direction = "south-west"

                            if thrown_direction == "north":
                                thrown_direction = "north-west"
                            if thrown_direction == "south":
                                thrown_direction = "south-west"

                            if thrown_direction == "south-west":
                                thrown_direction = "west"
                            if thrown_direction == "north-west":
                                thrown_direction = "west"
                        if item2_collision and not item1_collision and not item3_collision and not item4_collision:
                            if thrown_direction == "south":
                                thrown_direction = "north"

                            if thrown_direction == "south-east":
                                thrown_direction = "north-east"
                            if thrown_direction == "south-west":
                                thrown_direction = "north-west"

                            if thrown_direction == "east":
                                thrown_direction = "north-west"
                            if thrown_direction == "west":
                                thrown_direction = "north-west"

                            if thrown_direction == "north-west":
                                thrown_direction = "north"
                            if thrown_direction == "north-east":
                                thrown_direction = "north"
                            
                        if item3_collision and not item1_collision and not item2_collision and not item4_collision:
                            if thrown_direction == "west":
                                thrown_direction = "east"

                            if thrown_direction == "north-west":
                                thrown_direction = "north-east"
                            if thrown_direction == "south-west":
                                thrown_direction = "south-east"

                            if thrown_direction == "north":
                                thrown_direction = "north-east"
                            if thrown_direction == "south":
                                thrown_direction = "south-east"

                            if thrown_direction == "north-east":
                                thrown_direction = "east"
                            if thrown_direction == "south-east":
                                thrown_direction = "east"
                        if item4_collision and not item1_collision and not item2_collision and not item3_collision:
                            if thrown_direction == "north":
                                thrown_direction = "south"

                            if thrown_direction == "north-east":
                                thrown_direction = "south-east"
                            if thrown_direction == "north-west":
                                thrown_direction = "south-west"

                            if thrown_direction == "east":
                                thrown_direction = "south-east"
                            if thrown_direction == "west":
                                thrown_direction = "south-west"

                            if thrown_direction == "south-east":
                                thrown_direction = "south"
                            if thrown_direction == "south-west":
                                thrown_direction = "south"

                        if item1_collision and item2_collision:
                            if thrown_direction == "south-east":
                                thrown_direction = "north-west"
                                
                            if thrown_direction == "east":
                                thrown_direction = "north"
                            if thrown_direction == "south":
                                thrown_direction = "west"

                            if thrown_direction == "north-east":
                                thrown_direction = "north"
                            if thrown_direction == "south-west":
                                thrown_direction = "west"

                            if thrown_direction == "north":
                                thrown_direction = "north-west"
                            if thrown_direction == "west":
                                thrown_direction = "north-west"

                        if item2_collision and item3_collision:
                            if thrown_direction == "south-west":
                                thrown_direction = "north-east"
                                
                            if thrown_direction == "south":
                                thrown_direction = "east"
                            if thrown_direction == "west":
                                thrown_direction = "north"

                            if thrown_direction == "south-east":
                                thrown_direction = "east"
                            if thrown_direction == "north-west":
                                thrown_direction = "north"

                            if thrown_direction == "north":
                                thrown_direction = "north-east"
                            if thrown_direction == "east":
                                thrown_direction = "north-east"

                        if item3_collision and item4_collision:
                            if thrown_direction == "north-west":
                                thrown_direction = "south-east"
                                
                            if thrown_direction == "north":
                                thrown_direction = "east"
                            if thrown_direction == "west":
                                thrown_direction = "south"

                            if thrown_direction == "north-east":
                                thrown_direction = "east"
                            if thrown_direction == "south-west":
                                thrown_direction = "south"

                            if thrown_direction == "south":
                                thrown_direction = "south-east"
                            if thrown_direction == "east":
                                thrown_direction = "south-east"

                        if item4_collision and item1_collision:
                            if thrown_direction == "north-east":
                                thrown_direction = "south-west"
                                
                            if thrown_direction == "north":
                                thrown_direction = "west"
                            if thrown_direction == "east":
                                thrown_direction = "south"

                            if thrown_direction == "north-west":
                                thrown_direction = "west"
                            if thrown_direction == "south-east":
                                thrown_direction = "south"

                            if thrown_direction == "west":
                                thrown_direction = "south-west"
                            if thrown_direction == "south":
                                thrown_direction = "south-west"
                        thrown_position = last_thrown_position.copy()
                            


    # saves current player size
    current_player_size = (int(player_w), int(player_h))
    
    if current_player_size != last_player_size:

        player_hitbox = pygame.transform.scale(character_animation["hitbox"], current_player_size)
        player_real_hitbox = pygame.transform.scale(player_real_hitbox_raw, current_player_size) 
        player_real_hitbox_mask = pygame.mask.from_surface(player_real_hitbox)
        player_hitbox_mask = pygame.mask.from_surface(player_hitbox)
        last_player_size = current_player_size
    hitbox_px_count = player_hitbox_mask.count()
    player_img = pygame.transform.scale(character_animation[direction]["stand"][itemInhand],(player_w,   player_h))

    main_room_rect = main_room_img.get_rect(topleft=(map_pos_x,map_pos_y))
    if door_1_interact_img is not None:
        door_1_interact_rect = door_1_interact_img.get_rect(topleft=(map_pos_x,map_pos_y))
    if door_2_interact_img is not None:
        door_2_interact_rect = door_2_interact_img.get_rect(topleft=(map_pos_x,map_pos_y))
    if door_3_interact_img is not None:
        door_3_interact_rect = door_3_interact_img.get_rect(topleft=(map_pos_x,map_pos_y))
    if door_4_interact_img is not None:
        door_4_interact_rect = door_4_interact_img.get_rect(topleft=(map_pos_x,map_pos_y))
    if door_5_interact_img is not None:
        door_5_interact_rect = door_5_interact_img.get_rect(topleft=(map_pos_x,map_pos_y))
    if money_interact_img is not None and money_location != "inventory":
        money_interact_rect = money_interact_img.get_rect(topleft=(money_location[1][0]+map_pos_x, money_location[1][1]+map_pos_y))
    elif thrown_item == "Money" and money_interact_img is not None and thrown:
        money_interact_rect = money_interact_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        money_interact1_rect = money_interact1_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        money_interact2_rect = money_interact2_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        money_interact3_rect = money_interact3_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        money_interact4_rect = money_interact4_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
    if meat_interact_img is not None and meat_location != "inventory":
        meat_interact_rect = meat_interact_img.get_rect(topleft=(meat_location[1][0]+map_pos_x, meat_location[1][1]+map_pos_y))
    elif thrown_item == "Meat" and meat_interact_img is not None and thrown:
        meat_interact_rect = meat_interact_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        meat_interact1_rect = meat_interact1_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        meat_interact2_rect = meat_interact2_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        meat_interact3_rect = meat_interact3_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        meat_interact4_rect = meat_interact4_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
    if sword_interact_img is not None and sword_location != "inventory":
        sword_interact_rect = sword_interact_img.get_rect(topleft=(sword_location[1][0]+map_pos_x, sword_location[1][1]+map_pos_y)) 
    elif thrown_item == "Sword" and sword_interact_img is not None and thrown:
        sword_interact_rect = sword_interact_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        sword_interact1_rect = sword_interact1_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        sword_interact2_rect = sword_interact2_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        sword_interact3_rect = sword_interact3_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        sword_interact4_rect = sword_interact4_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
    if key_interact_img is not None and key_location != "inventory":
        key_interact_rect = key_interact_img.get_rect(topleft=(key_location[1][0]+map_pos_x, key_location[1][1]+map_pos_y))
    elif thrown_item == "Key" and key_interact_img is not None and thrown:
        key_interact_rect = key_interact_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        key_interact1_rect = key_interact1_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        key_interact2_rect = key_interact2_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        key_interact3_rect = key_interact3_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
        key_interact4_rect = key_interact4_img.get_rect(topleft=(thrown_position[0], thrown_position[1]))
    floor_rect = main_room_floor.get_rect(topleft=(map_pos_x,map_pos_y))
    player_rect = player_img.get_rect(center=(player_x,player_y))
    player_hitbox_rect = player_hitbox.get_rect(center=(player_x,player_y))
    player_real_hitbox_rect = player_real_hitbox.get_rect(center=(player_x,player_y))

    offset = (player_hitbox_rect.x-floor_rect.x,player_hitbox_rect.y-floor_rect.y)
    overlap = floor_mask.overlap_area(player_hitbox_mask,offset)
    if overlap >= 0.9*hitbox_px_count:
        overlapped = True
    else:
        overlapped = False
    if moving or punched:
        if overlapped == False:
            player_x,player_y = last_position
            map_pos_x,map_pos_y = map_last_pos
            overall_y = last_overall_y
        y_dis_to_y_axis = abs((player_y)-height/2)
        x_dis_to_x_axis = abs((player_x)-width/2)
        if y_dis_to_y_axis <3: 
            player_y = height/2
        if x_dis_to_x_axis <3:
            player_x = width/2
        player_img = pygame.transform.scale(character_animation[direction]["walk"][itemInhand][moved_for],(player_w,player_h))
    if punched:
        if overlapped == False:
            player_x,player_y = last_position
            map_pos_x,map_pos_y = map_last_pos
            overall_y = last_overall_y
        y_dis_to_y_axis = abs((player_y)-height/2)
        x_dis_to_x_axis = abs((player_x)-width/2)
        if y_dis_to_y_axis <3: 
            player_y = height/2
        if x_dis_to_x_axis <3:
            player_x = width/2
        player_img = pygame.transform.scale(character_animation[direction]["punched"][itemInhand][punch_frame],(player_w,player_h))
    
    collison, collision_with = interact_collison_detector(current_room, 
                               door_1_interact_rect, door_1_interact_mask, 
                               door_2_interact_rect, door_2_interact_mask, 
                               door_3_interact_rect, door_3_interact_mask, 
                               door_4_interact_rect, door_4_interact_mask, 
                               door_5_interact_rect, door_5_interact_mask,
                               player_hitbox_rect, player_hitbox_mask,
                               hitbox_px_count)
    item_collison = item_collision_detector(money_interact_rect, money_interact_mask,
                               meat_interact_rect, meat_interact_mask,
                               sword_interact_rect, sword_interact_mask,
                               key_interact_rect, key_interact_mask,
                               player_hitbox_rect, player_hitbox_mask,
                               hitbox_px_count)
    if throwing:
        player_img = pygame.transform.scale(character_animation[direction]["throw"][character_thrown_frame],(player_w,player_h))
    if thrown:
        if thrown_item == "Key":
            key_img = pygame.transform.scale(character_animation[direction]["throw_items"]["Key"][character_item_thrown_frame],(width/2,height/2))
        if thrown_item == "Sword":
            sword_img = pygame.transform.scale(character_animation[direction]["throw_items"]["Sword"][character_item_thrown_frame],(width/2,height/2))
        if thrown_item == "Meat":
            meat_img = pygame.transform.scale(character_animation[direction]["throw_items"]["Meat"][character_item_thrown_frame],(width/2,height/2))
        if thrown_item == "Money":
            money_img = pygame.transform.scale(character_animation[direction]["throw_items"]["Money"][character_item_thrown_frame],(width/2,height/2))
    if not changing_room:
        screen.blit(main_room_img, main_room_rect)
        #screen.blit(player_real_hitbox, player_real_hitbox_rect)
        #screen.blit(main_room_floor,floor_rect)
        if thrown:
            if thrown_item == "Key":
                screen.blit(key_img,( thrown_position[0],thrown_position[1]))
            if thrown_item == "Meat":
                screen.blit(meat_img,( thrown_position[0],thrown_position[1]))
            if thrown_item == "Money":
                screen.blit(money_img,( thrown_position[0],thrown_position[1]))
            if thrown_item == "Sword":
                screen.blit(sword_img,( thrown_position[0],thrown_position[1]))
        if  money_location[0] == current_room:
            screen.blit(money_img, (money_location[1][0]+map_pos_x, money_location[1][1]+map_pos_y))
        if meat_location[0] == current_room:
            screen.blit(meat_img, (meat_location[1][0]+map_pos_x, meat_location[1][1]+map_pos_y))
        if sword_location[0] == current_room:
            screen.blit(sword_img, (sword_location[1][0]+map_pos_x, sword_location[1][1]+map_pos_y))
        if key_location[0] == current_room:
            screen.blit(key_img, (key_location[1][0]+map_pos_x, key_location[1][1]+map_pos_y))
        screen.blit(player_img,(player_x-player_w/2,player_y-player_h/2)) 
        
        if extra_cover is not None:
            if current_room == "corridorOne" or current_room == "corridorTwo" or current_room == "corridorFour" or current_room == "corridorFive" or current_room == "roomFive" or current_room == "roomFive" or current_room == "roomTwo" or current_room == "roomOne":
                screen.blit(extra_cover, main_room_rect)
        if inventory_selected == "1":
            screen.blit(inventory_selected_1,inventory_pos)
        elif inventory_selected == "2":
            screen.blit(inventory_selected_2,inventory_pos)
        elif inventory_selected == "3":
            screen.blit(inventory_selected_3,inventory_pos)
        elif inventory_selected == "4":
            screen.blit(inventory_selected_4,inventory_pos)
        elif inventory_selected == "5":
            screen.blit(inventory_selected_5,inventory_pos)
        screen.blit(inventory_item_1,inventory_pos)
        
        
        if money_location == "inventory":
            screen.blit(inventory_item_2,inventory_pos)
        if meat_location == "inventory":
            screen.blit(inventory_item_3,inventory_pos)
        if sword_location == "inventory":
            screen.blit(inventory_item_4,inventory_pos)
        if key_location == "inventory":
            screen.blit(inventory_item_5,inventory_pos)
        pygame.display.flip()
    clock.tick(60)