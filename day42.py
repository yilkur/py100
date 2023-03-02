print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()


def getPrintColor(type):
    DEFAULT = "\033[33m"

    colors = {
        "earth": "\033[32m",
        "air": "\033[37m",
        "fire": "\033[31m",
        "water": "\033[34m"
    }

    return colors[type] if type in colors else DEFAULT


mokedex = {
    "Beast Name": None,
    "Type": None,
    "Special Move": None,
    "HP": None,
    "MP": None
}

for key, value in mokedex.items():
    mokedex[key] = input(f"{key}: ").strip().lower()

print("MokéBeast")
print()
print(getPrintColor(mokedex["Type"]), end="")

for key, value in mokedex.items():
    print(f"{key:<15}: {value}")
