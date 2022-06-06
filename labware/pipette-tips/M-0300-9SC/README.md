# M-0300-9SC Labware Definitions

This directory contains two labware files for M-0300-9SC tip rack for use with our OT-2 robot:

- biotix_96_tiprack_300ul_left.json
- biotix_96_tiprack_300ul_right.json

**Do not execute a protocol using these labware definitions without running the labware position check.**
This check will allow you to customize the pipette offsets manually for your protocol using the OT-2's pipette jog controls.
If you run this check, you don't need to worry about the left/right pipette issue because you'll be able to correct the offsets as part of the check.

**DISCLAIMER**: I (@amlalejini) did not have technical specifications for the pipette racks in sufficient detail to create the labware files.
I generated initial labware files by measuring the tip racks (with lots of estimating for tricky measurements), and I used trial-and-error to tweak the labware files until they worked.
As such, these labware files are not perfect. Folks should absolutely feel free to improve them.

**NOTE**: In testing, I found that definitions that I created with the left pipette did not work as-is with the right pipette (and vice versa).
`_left.json` was created using the left pipette slot, and the `_right.json` was created using the right pipette slot.

## Definition testing

Light tested using the opentrons test script (output from the custom labware creator):

- biotix_96_tiprack_10ul_left.json (with left pipette)
- biotix_96_tiprack_10ul_right.json (with right pipette)

Stress tested

TODO