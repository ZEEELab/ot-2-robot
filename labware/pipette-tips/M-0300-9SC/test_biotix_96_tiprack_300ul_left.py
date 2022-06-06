import json
from opentrons import protocol_api, types


TEST_TIPRACK_SLOT = '5'

RATE = 0.25  # % of default speeds
SLOWER_RATE = 0.1

PIPETTE_MOUNT = 'left'
PIPETTE_NAME = 'p300_multi'


TIPRACK_DEF_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"biotix","brandId":["M-0300-9SC"]},"metadata":{"displayName":"Biotix 96 Tip Rack 300 µL","displayCategory":"tipRack","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.5,"yDimension":85.35,"zDimension":63.2},"wells":{"A1":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":14.8,"y":76.65,"z":3.66},"B1":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":14.8,"y":67.65,"z":3.66},"C1":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":14.8,"y":58.65,"z":3.66},"D1":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":14.8,"y":49.65,"z":3.66},"E1":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":14.8,"y":40.65,"z":3.66},"F1":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":14.8,"y":31.65,"z":3.66},"G1":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":14.8,"y":22.65,"z":3.66},"H1":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":14.8,"y":13.65,"z":3.66},"A2":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":23.78,"y":76.65,"z":3.66},"B2":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":23.78,"y":67.65,"z":3.66},"C2":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":23.78,"y":58.65,"z":3.66},"D2":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":23.78,"y":49.65,"z":3.66},"E2":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":23.78,"y":40.65,"z":3.66},"F2":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":23.78,"y":31.65,"z":3.66},"G2":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":23.78,"y":22.65,"z":3.66},"H2":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":23.78,"y":13.65,"z":3.66},"A3":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":32.76,"y":76.65,"z":3.66},"B3":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":32.76,"y":67.65,"z":3.66},"C3":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":32.76,"y":58.65,"z":3.66},"D3":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":32.76,"y":49.65,"z":3.66},"E3":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":32.76,"y":40.65,"z":3.66},"F3":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":32.76,"y":31.65,"z":3.66},"G3":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":32.76,"y":22.65,"z":3.66},"H3":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":32.76,"y":13.65,"z":3.66},"A4":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":41.74,"y":76.65,"z":3.66},"B4":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":41.74,"y":67.65,"z":3.66},"C4":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":41.74,"y":58.65,"z":3.66},"D4":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":41.74,"y":49.65,"z":3.66},"E4":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":41.74,"y":40.65,"z":3.66},"F4":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":41.74,"y":31.65,"z":3.66},"G4":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":41.74,"y":22.65,"z":3.66},"H4":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":41.74,"y":13.65,"z":3.66},"A5":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":50.72,"y":76.65,"z":3.66},"B5":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":50.72,"y":67.65,"z":3.66},"C5":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":50.72,"y":58.65,"z":3.66},"D5":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":50.72,"y":49.65,"z":3.66},"E5":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":50.72,"y":40.65,"z":3.66},"F5":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":50.72,"y":31.65,"z":3.66},"G5":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":50.72,"y":22.65,"z":3.66},"H5":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":50.72,"y":13.65,"z":3.66},"A6":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":59.7,"y":76.65,"z":3.66},"B6":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":59.7,"y":67.65,"z":3.66},"C6":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":59.7,"y":58.65,"z":3.66},"D6":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":59.7,"y":49.65,"z":3.66},"E6":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":59.7,"y":40.65,"z":3.66},"F6":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":59.7,"y":31.65,"z":3.66},"G6":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":59.7,"y":22.65,"z":3.66},"H6":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":59.7,"y":13.65,"z":3.66},"A7":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":68.68,"y":76.65,"z":3.66},"B7":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":68.68,"y":67.65,"z":3.66},"C7":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":68.68,"y":58.65,"z":3.66},"D7":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":68.68,"y":49.65,"z":3.66},"E7":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":68.68,"y":40.65,"z":3.66},"F7":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":68.68,"y":31.65,"z":3.66},"G7":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":68.68,"y":22.65,"z":3.66},"H7":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":68.68,"y":13.65,"z":3.66},"A8":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":77.66,"y":76.65,"z":3.66},"B8":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":77.66,"y":67.65,"z":3.66},"C8":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":77.66,"y":58.65,"z":3.66},"D8":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":77.66,"y":49.65,"z":3.66},"E8":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":77.66,"y":40.65,"z":3.66},"F8":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":77.66,"y":31.65,"z":3.66},"G8":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":77.66,"y":22.65,"z":3.66},"H8":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":77.66,"y":13.65,"z":3.66},"A9":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":86.64,"y":76.65,"z":3.66},"B9":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":86.64,"y":67.65,"z":3.66},"C9":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":86.64,"y":58.65,"z":3.66},"D9":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":86.64,"y":49.65,"z":3.66},"E9":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":86.64,"y":40.65,"z":3.66},"F9":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":86.64,"y":31.65,"z":3.66},"G9":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":86.64,"y":22.65,"z":3.66},"H9":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":86.64,"y":13.65,"z":3.66},"A10":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":95.62,"y":76.65,"z":3.66},"B10":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":95.62,"y":67.65,"z":3.66},"C10":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":95.62,"y":58.65,"z":3.66},"D10":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":95.62,"y":49.65,"z":3.66},"E10":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":95.62,"y":40.65,"z":3.66},"F10":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":95.62,"y":31.65,"z":3.66},"G10":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":95.62,"y":22.65,"z":3.66},"H10":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":95.62,"y":13.65,"z":3.66},"A11":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":104.6,"y":76.65,"z":3.66},"B11":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":104.6,"y":67.65,"z":3.66},"C11":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":104.6,"y":58.65,"z":3.66},"D11":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":104.6,"y":49.65,"z":3.66},"E11":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":104.6,"y":40.65,"z":3.66},"F11":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":104.6,"y":31.65,"z":3.66},"G11":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":104.6,"y":22.65,"z":3.66},"H11":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":104.6,"y":13.65,"z":3.66},"A12":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":113.58,"y":76.65,"z":3.66},"B12":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":113.58,"y":67.65,"z":3.66},"C12":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":113.58,"y":58.65,"z":3.66},"D12":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":113.58,"y":49.65,"z":3.66},"E12":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":113.58,"y":40.65,"z":3.66},"F12":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":113.58,"y":31.65,"z":3.66},"G12":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":113.58,"y":22.65,"z":3.66},"H12":{"depth":59.54,"totalLiquidVolume":300,"shape":"circular","diameter":5.35,"x":113.58,"y":13.65,"z":3.66}},"groups":[{"metadata":{},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":true,"tipLength":59.54,"isMagneticModuleCompatible":false,"loadName":"biotix_96_tiprack_300ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
TIPRACK_DEF = json.loads(TIPRACK_DEF_JSON)
TIPRACK_LABEL = TIPRACK_DEF.get('metadata', {}).get(
    'displayName', 'test labware')

metadata = {'apiLevel': '2.0'}


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware_from_definition(TIPRACK_DEF, TEST_TIPRACK_SLOT, TIPRACK_LABEL)
    pipette = protocol.load_instrument(
        PIPETTE_NAME, PIPETTE_MOUNT, tip_racks=[tiprack])

    num_cols = len(TIPRACK_DEF.get('ordering', [[]]))
    num_rows = len(TIPRACK_DEF.get('ordering', [[]])[0])


    def set_speeds(rate):
        protocol.max_speeds.update({
            'X': (600 * rate),
            'Y': (400 * rate),
            'Z': (125 * rate),
            'A': (125 * rate),
        })

        speed_max = max(protocol.max_speeds.values())

        for instr in protocol.loaded_instruments.values():
            instr.default_speed = speed_max

    set_speeds(RATE)
    firstwell = tiprack.well('A1')
    pipette.move_to(firstwell.top())
    protocol.pause("If the pipette is accurate click 'resume'")
    pipette.pick_up_tip()
    protocol.pause("If the pipette went into the center of the tip, click 'resume'")
    pipette.return_tip()
    protocol.pause("If the pipette successfully picked up the tip(s) but does not eject succesfully, pull the tip(s) off by hand and click 'resume'. Do not worry about tip ejection yet")

    last_col = (num_cols * num_rows) - num_rows
    if (PIPETTE_NAME == 'p20_multi_gen2' or PIPETTE_NAME == 'p300_multi_gen2'):
        well = tiprack.well(last_col)
        pipette.move_to(well.top())
        protocol.pause("If the position is accurate click 'resume'")
        pipette.pick_up_tip(well)
    else:
        last_well = (num_cols) * (num_rows)
        well = tiprack.well(last_well-1)
        pipette.move_to(well.top())
        protocol.pause("If the position is accurate click 'resume'")
        pipette.pick_up_tip(well)

    protocol.pause("If the pipette went to the center of the tip, click 'resume'")
    pipette.return_tip()
    protocol.comment("If the pipette successfully picked up the tip(s) but does not eject succesfully, pull the tip(s) off by hand and click 'resume'. Do not worry about tip ejection yet")

