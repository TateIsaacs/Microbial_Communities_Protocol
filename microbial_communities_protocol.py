from opentrons import protocol_api 
from opentrons import types             # needed for location.move() method 
metadata = {
    "protocolName": "Microbial Colonies",
    "description": """This protocol is a test script for creating 
     patterened microbial communities on an agar plate. For now 
     the protocol will simply be testing the basic functions of the 
     API so I can start learning :)""",
    "author": "Tate Isaacs"

}

# Use the labware postion check after in the setup of the protocol run to check and set a z height offset for the labware, then run the protocol 

requirements = {"robotType": "OT-2", "apiLevel": "2.16"}

def run(protocol: protocol_api.ProtocolContext):
    # make sure to check all the labware pretty sure most of it is wrong!! 
    tips10ul = protocol.load_labware("opentrons_96_tiprack_10ul",1)  # not sure if we are using 10ul?? 
    tips300ul = protocol.load_labware("opentrons_96_tiprack_300ul",2)  # not sure if we are using 10ul?? 
    snapcaps = protocol.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap",3)
    falcontubes = protocol.load_labware("opentrons_15_tuberack_falcon_15ml_conical",4)
    plate = protocol.load_labware("nunc_1_well_dish",5)
    
    # Loading Pipettes: 
    left_pipette = protocol.load_instrument("p10_single", "left", tip_racks=[tips10ul]) # I do not belive that opentrons supports gen1 pipettes in their API anymore so you have to use gen 2 (I think)
    right_pipette = protocol.load_instrument("p300_single", "right", tip_racks=[tips300ul])

    # define the left corner of the plate to use as reference. This will be created using the well center position
    plate_center = plate["A1"].top()    # So I belive this moves the pipette to the center of the top, we will see 
    left_corner = plate_center.move(types.Point(-58,37,0)) # takes a postion x, y, z  plate dimensions are 121.4x 78y using an offset of ~2mm move 58x and 37y 


    # Here we will get a tip and move the pipette to the statring position on the plate 
    left_pipette.pick_up_tip()
    left_pipette.move_to(left_corner)    #.top() to move to the top of the plate 
    # Here we will pause for the user to check the z position 
    protocol.pause("Check z height of pipette")
    # Here we return the tip to it's original location 
    left_pipette.return_tip()

"""
  for i in range(2):
        column = snapcaps.column()[i]
        left_pipette.transfer(100, snapcaps["A1"], row[0], mix_after=(3, 50))
        left_pipette.transfer(100, row[:4], row[1], mix_after=(3, 50)) # from column 1 to 5 tranfer 100 to next column


  """
    





