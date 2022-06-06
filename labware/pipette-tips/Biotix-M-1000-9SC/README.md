# M-1000-9SC Labware Definitions

This directory contains a labware definition file for M-1000-9SC tip rack for use with the OT-2 robot:

- biotix_96_tiprack_300ul.json

**Do not execute a protocol using these labware definitions without running the labware position check.**
This check will allow you to customize the pipette offsets manually for your protocol using the OT-2's pipette jog controls.
If you run this check, you don't need to worry about the left/right pipette issue because you'll be able to correct the offsets as part of the check.

**NOTE:** This definition was generated and lightly tested with the right pipette. Regardless of the which pipette slot you use, you should run a labware position check. However, if you use the left pipette slot with this definition, you will absolutely need to adjust the offsets (via the labware position check option).

**DISCLAIMER**: I (@amlalejini) did not have technical specifications for the pipette racks in sufficient detail to create the labware files.
I generated initial labware files by measuring the tip racks (with lots of estimating for tricky measurements), and I used trial-and-error to tweak the labware files until they worked.
As such, these labware files are not perfect. Folks should absolutely feel free to improve them.


## Definition testing

Light tested using the opentrons test script (output from the custom labware creator):

- biotix_96_tiprack_1000ul_left.json (with left pipette)

Stress tested

TODO