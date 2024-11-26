# Far-Cry-3-Memory-Editor
A Python-based memory editor for Far Cry 3, allowing users to modify in-game values such as health, money, ammo, and items. This script uses the pymem library to directly manipulate game memory addresses, providing functionality for both setting new values and freezing them for continuous effect. 

This script was created solely for education.


Features include:

- Real-time modification of health, ammo, syringes, and other inventory items.
- Option to freeze values for continuous effect.
- User-friendly menu interface with item-specific adjustments.
- Built-in safeguards for handling invalid inputs and memory reading errors.

## Prerequisites

- **Python 3.x**: Make sure you have Python 3 installed on your system.
- **pymem library**: This script uses `pymem` for memory manipulation.

## Pointer Offset Info
```
    health_pointer_base = module.lpBaseOfDll + 0x028624D0
    health_offsets = [0x4, 0x10, 0x44, 0x2C, 0x10]

    "money": (module.lpBaseOfDll + 0x02861838, [0x0, 0xE4, 0x24, 0xC48]),
    "syringes": (module.lpBaseOfDll + 0x02829C3C, [0xA4, 0x148, 0x8, 0x2C, 0xC, 0x138, 0x0, 0x60]),
    "ammo": (module.lpBaseOfDll + 0x028B67B0, [0x0, 0xC, 0x88, 0x10, 0x48, 0xCC]),
    "pistol_magazine": (module.lpBaseOfDll + 0x0284F620, [0x4, 0xE8, 0x20, 0xF0, 0x0, 0x10]),
    "smg_magazine": (module.lpBaseOfDll + 0x0284F620, [0x4, 0xE8, 0x20, 0xF0, 0x10, 0x10]),
    "shotgun_magazine": (module.lpBaseOfDll + 0x02829490, [0x4, 0x38, 0x4, 0x4C, 0x0, 0x14, 0x10]),
    "rifle_magazine": (module.lpBaseOfDll + 0x02829490, [0x4, 0x38, 0x4, 0x4C, 0x0, 0xC, 0x10]),
    "sniper_magazine": (module.lpBaseOfDll + 0x02829490, [0x4, 0x38, 0x4, 0x4C, 0x0, 0x8, 0x10]),
    "lmg_magazine": (module.lpBaseOfDll + 0x0284F620, [0x4, 0xE8, 0x20, 0xF0, 0x4, 0x10]),
    "rpg_magazine": (module.lpBaseOfDll + 0x0284F620, [0x4, 0xE8, 0x20, 0xF0, 0x18, 0x10]),
    "arrows": (module.lpBaseOfDll + 0x0284F620, [0x4, 0xE8, 0x20, 0xF0, 0x30, 0x10]),
    "flares": (module.lpBaseOfDll + 0x02829490, [0x4, 0x38, 0x4, 0x4C, 0x0, 0x24, 0x10]),
```


