from opentrons import protocol_api 
from opentrons import types             # needed for location.move() method 
metadata = {
    "protocolName": "Microbial Colonies V1",
    "description": """This protocol is a test script for creating 
     patterened microbial communities on an agar plate. For now 
     the protocol will simply be testing the basic functions of the 
     API so I can start learning :)""",
    "author": "Tate Isaacs"

}

# Note:
# Use the labware postion check in the setup of the protocol run to check and set a z height offset for the labware, then run the protocol 

requirements = {"robotType": "OT-2", "apiLevel": "2.16"}

def run(protocol: protocol_api.ProtocolContext): 
    tips10ul = protocol.load_labware("opentrons_96_tiprack_10ul",1)                                 # This seems to work but I am not sure if the tips we use are truly opentrons branded..  
    tips300ul = protocol.load_labware("opentrons_96_tiprack_300ul",2)   
    snapcaps = protocol.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap",3)
    falcontubes = protocol.load_labware("opentrons_15_tuberack_falcon_15ml_conical",4)              # Custome labware definition for rectangular agar plate 
    plate = protocol.load_labware("nunc_1_well_dish",5)                                         
    

    # Loading Pipettes: 
    left_pipette = protocol.load_instrument("p10_single", "left", tip_racks=[tips10ul])             # Opentrons does not have the name of their gen1 pipettes anywhere on their website just FYI 
    right_pipette = protocol.load_instrument("p300_single", "right", tip_racks=[tips300ul])

    # defining the left corner of the plate to use as reference. This will be created using the well center position
    plate_center = plate["A1"].top()    # moves the pipette to the center of the top
    left_corner = plate_center.move(types.Point(-50,30,0)) # takes a postion x, y, z  plate dimensions are 121.4x 78y using an offset of ~2mm so moving -58x and 37y 
    top_Falcon_tube = falcontubes["A1"].top(z=-20)


    # TO DO Arrangment of the microbial communities in a simple array 

    for i in range(5):        # for some reason this goes to the same spot five times before picking up another tip... 
        offset = 0 
        point = left_corner.move(types.Point(offset,0,0))
        left_pipette.transfer(
            volume= 8,
            source= top_Falcon_tube,
            dest= point
        ) 
        offset += 10


    





