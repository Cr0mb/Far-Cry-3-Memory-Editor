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


## How to Find Pointers in Cheat Engine for Far Cry 3

### Step 1: Finding the Health Pointer

1. **Search for Health Value**:
   - Since health regenerates and might be fractional (e.g., 99.85), we'll search using a **float** type.
   - In Cheat Engine, select **"Unknown Initial Value"** and hit **First Scan**.
   - This will return many addresses because Cheat Engine doesn’t know the exact value yet.

2. **Change Health**:
   - In the game, change your health (e.g., by taking fall damage or getting hit).
   - Afterward, return to Cheat Engine and select **"Changed Value"** and click **Next Scan**.
   - As health regenerates, select **"Increased Value"** and continue scanning.
   - Once health is full, take damage again and select **"Decreased Value"**.
   - Repeat this process until you find the correct address for health.

### Step 2: Finding Other Values (e.g., Money, Ammo)

1. **Search for Integer Values**:
   - For values like **money** or **ammo**, these are likely whole numbers, so use a **4-byte** or **2-byte** search.
   - For example, if you have $1000 in-game, search for **1000**.
   
2. **Change and Scan**:
   - Spend or gain money, then enter the new value (e.g., spend $500, leaving $500).
   - Scan for the new value and repeat the process until you narrow down the correct address.

### Step 3: Dealing with Dynamic Memory Addresses

- Memory addresses in games are dynamic and will change every time you restart the game. To address this, we need to **generate pointer maps**.

### Step 4: Using Pointer Maps

1. **Create Pointer Map**:
   - Right-click on a found address in Cheat Engine and select **"Pointer Map"**.
   - This saves the pointer path from the current address, helping you track how the value is stored.

2. **Scan for Pointers**:
   - Restart the game and rescan for the value you’re looking for.
   - Create a **Pointer Map** for this new scan.

3. **Repeat the Process**:
   - Repeat the process 3-4 times, creating new pointer maps each time.

### Step 5: Pointer Scan

1. **Start Pointer Scan**:
   - After creating a few pointer maps, right-click on one of the found addresses and select **"Pointer Scan for this address"**.
   - Set **Pointer Scan Depth** to a reasonable value (e.g., **7**) and begin the scan.

2. **Find Valid Pointer**:
   - Once the scan finishes, look for valid pointer paths that lead to the health value.
   - Restart the game and observe which pointers still lead to the health value.
   - Re-attach Cheat Engine to the game to prevent pointers from showing as "??".

### Step 6: Verifying the Pointer

- **Verify the Pointer**:
   - Modify the value at the pointer's location and check if it updates in the game.
   - If it updates correctly, you’ve found the right pointer.

> **Note**: Some values, like magazine ammo, might not update immediately after modification. In such cases, perform an in-game action (e.g., shooting the gun) to see the updated value.

### Step 7: Freezing Values

1. **Freeze a Value**:
   - To freeze a value (e.g., health), simply click the checkbox in the **Memory Viewer**.
   - If the checkbox is red with an "X", the value is frozen.
