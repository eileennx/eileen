# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_star_names(data):
    for star in data:
        print(star)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_star_spectral_types(data):
    for star, info in data.items():
        print(f"Star: {star} | Spectral Type: {info['Spectral Type']}")
        
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def faint_stars(data):
    print("Stars with Magnitude > 0.1:")
    for star, info in data.items():
        if info["Magnitude"] > 0.1:
            print(f"- {star} ({info['Magnitude']})")

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Arcturus"] = {
    "RA": "14h 15m 39.7s",
    "Dec": "+19° 10′ 56″",
    "Magnitude": -0.05,
    "Spectral Type": "K1.5IIIp"
}


# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def find_best_target(data):
    best_star = None
    min_diff = float('inf')

    for star, info in data.items():
        clean_dec = info["Dec"].replace('−', '-').split('°')[0]
        dec_val = float(clean_dec)
        diff = abs(dec_val - 20)

        if diff < min_diff:
            min_diff = diff
            best_star = star

    return best_star

# 6) What is your favorite constellation?
# The Big Dipper
