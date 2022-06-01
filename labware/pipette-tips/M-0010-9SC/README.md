# M-0010-9SC Labware Definitions

This directory contains two labware files for M-0010-9SC tip rack for use with our OT-2 robot:

- biotix_96_tiprack_10ul_left.json
- biotix_96_tiprack_10ul_right.json

**DISCLAIMER**: I (@amlalejini) did not have technical specifications for the pipette racks in sufficient detail to create the labware files.
I generated initial labware files by measuring the tip racks (with lots of estimating for tricky measurements), and I used trial-and-error to tweak the labware files until they worked.
As such, these labware files are not perfect. Folks should feel free to improve them.

**NOTE**: In testing, I found that definitions that I created with the left pipette did not work as-is with the right pipette (and vice versa).
`_left.json` was created using the left pipette slot, and the `_right.json` was created using the right pipette slot.

When using either of these labware definitions, **I strongly recommend running the labware position check before starting your protocol on the robot.**
This will let you customize the offsets manually for your protocol using the OT-2 pipette jog controls.

## Definition testing

Light tested using the opentrons test script (output from the custom labware creator):

- biotix_96_tiprack_10ul_left.json (with left pipette)
- biotix_96_tiprack_10ul_right.json (with right pipette)

Stress tested

TODO