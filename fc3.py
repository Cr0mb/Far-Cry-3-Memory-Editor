import os
import pymem
import pymem.process
import time
import threading

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_value(pointer_base, offsets):
    try:
        pointer = pm.read_int(pointer_base)
        for offset in offsets:
            pointer = pm.read_int(pointer + offset)
        return pointer
    except pymem.exception.MemoryReadError as e:
        print(f"Error reading memory: {e}")
        return None

def get_health_value():
    health_pointer_base = module.lpBaseOfDll + 0x028624D0
    health_offsets = [0x4, 0x10, 0x44, 0x2C, 0x10]
    pointer = get_value(health_pointer_base, health_offsets[:-1])
    if pointer is not None:
        pointer += health_offsets[-1]
        return pm.read_float(pointer)
    return None

def set_value(pointer_base, offsets, new_value, is_float=False):
    try:
        pointer = pm.read_int(pointer_base)
        for offset in offsets[:-1]:
            pointer = pm.read_int(pointer + offset)
        final_pointer = pointer + offsets[-1]
        
        if is_float:
            pm.write_float(final_pointer, new_value)
        else:
            pm.write_int(final_pointer, new_value)
    except pymem.exception.MemoryReadError as e:
        print(f"Error setting memory: {e}")

def get_value_for_item(pointer_base, offsets):
    return get_value(pointer_base, offsets)

def set_value_for_item(item, new_value):
    pointer_base, offsets = items[item]
    is_float = item == "health"
    set_value(pointer_base, offsets, new_value, is_float)

def print_item_values():
    item_values = {item: get_value_for_item(pointer_base, offsets) for item, (pointer_base, offsets) in items.items()}
    item_values['health'] = get_health_value()
    return item_values

def print_menu():
    clear_screen()
    item_values = print_item_values()
    print("="*15)
    print("Made By Cr0mb.")
    print("="*15, "\n")
    print("\nMenu:")
    menu_items = list(items.keys())
    for idx, (item, value) in enumerate(item_values.items(), start=1):
        if item == "health":
            frozen_flag = " [Frozen]" if frozen_values.get(item, False) else ""
            print(f"{idx}. Set Health {value}{frozen_flag}" if value is not None else f"{idx}. Set Health (Failed to read)")
        else:
            frozen_flag = " [Frozen]" if frozen_values.get(item, False) else ""
            print(f"{idx}. Set {item.capitalize()} {value}{frozen_flag}" if value is not None else f"{idx}. Set {item.capitalize()} (Failed to read)")
    print(f"{len(menu_items) + 2}. Exit")


def confirm_freeze(item, current_value):
    freeze = input(f"Do you want to freeze the value of {item} at {current_value}? (y/n): ").strip().lower()
    return freeze == 'y'

def confirm_unfreeze(item):
    unfreeze = input(f"Do you want to unfreeze the value of {item}? (y/n): ").strip().lower()
    return unfreeze == 'y'

def freeze_value(item, value):
    while frozen_values.get(item, False):
        try:
            pointer_base, offsets = items[item]
            is_float = item == "health"
            set_value(pointer_base, offsets, value, is_float)
            time.sleep(0.1)
        except Exception as e:
            print(f"Error in freezing {item}: {e}")
            break

def freeze_health(value):
    while frozen_values.get("health", False):
        try:
            set_value(module.lpBaseOfDll + 0x028624D0, [0x4, 0x10, 0x44, 0x2C, 0x10], value, is_float=True)
            time.sleep(0.1)
        except Exception as e:
            print(f"Error in freezing health: {e}")
            break

if __name__ == "__main__":
    pm = pymem.Pymem('farcry3_d3d11.exe')
    
    module = pymem.process.module_from_name(pm.process_handle, 'FC3_d3d11.dll')

    items = {
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
    }

    frozen_values = {}

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '14':
            print("Exiting...")
            break
        
        if choice == '13':
            item = "health"
            current_value = get_health_value()
            if current_value is not None:
                if item in frozen_values and frozen_values[item]:
                    unfreeze = confirm_unfreeze(item)
                    if unfreeze:
                        frozen_values[item] = False
                        print(f"{item.capitalize()} unfrozen.")
                if item not in frozen_values or not frozen_values[item]:
                    new_value = input(f"Enter new {item} value: ")
                    try:
                        new_value = float(new_value)
                        set_value(module.lpBaseOfDll + 0x028624D0, [0x4, 0x10, 0x44, 0x2C, 0x10], new_value, is_float=True)
                        if confirm_freeze(item, new_value):
                            frozen_values[item] = True
                            print(f"{item.capitalize()} frozen.")
                            freeze_thread = threading.Thread(target=freeze_health, args=(new_value,))
                            freeze_thread.daemon = True
                            freeze_thread.start()
                    except ValueError:
                        print(f"Invalid value for {item}. Please enter a valid number.")
                clear_screen()

        elif choice in [str(i) for i in range(1, 13)]:
            item = list(items.keys())[int(choice) - 1]
            current_value = get_value_for_item(items[item][0], items[item][1])
            
            if item in frozen_values and frozen_values[item]:
                unfreeze = confirm_unfreeze(item)
                if unfreeze:
                    frozen_values[item] = False
                    print(f"{item.capitalize()} unfrozen.")

            if item not in frozen_values or not frozen_values[item]:
                new_value = input(f"Enter new {item} value: ")
                try:
                    new_value = float(new_value) if item == "health" else int(new_value)
                    set_value_for_item(item, new_value)
                    if confirm_freeze(item, new_value):
                        frozen_values[item] = True
                        print(f"{item.capitalize()} frozen.")
                        freeze_thread = threading.Thread(target=freeze_value, args=(item, new_value))
                        freeze_thread.daemon = True
                        freeze_thread.start()
                except ValueError:
                    print(f"Invalid value for {item}. Please enter a valid number.")
            clear_screen()
        else:
            print("Invalid choice, please try again.")
