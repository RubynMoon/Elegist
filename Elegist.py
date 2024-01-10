import random
import tkinter as tk

# Define lists of words for each part of the 

articles= [ "a", "the", "an", "your", "our", ""]

nouns = [
    "moon", "heart", "sun", "ocean", "tree", "flower", "song", "bird", "river",
    "cloud", "star", "rain", "wind", "sea", "stone", "path", "dream", "night",
    "day", "sky", "leaf", "wave", "fire", "shadow", "mirror", "journey",
    "echo", "whisper", "silence", "world", "time", "hope", "fate", "tear",
    "sorrow", "laughter", "wonder", "destiny", "dawn", "dusk", "light",
    "shadow", "embrace", "serenity", "solitude", "magic", "eternity",
    "reflection", "soul", "garden", "feather", "breeze", "joy", "passion",
    "harmony", "mystery", "serenade", "infinity", "horizon", "alchemy",
    "serendipity", "rapture", "melody", "essence", "cascade", "whirlwind",
    "cascade", "tranquility", "insomnia", "whimsy", "lullaby", "ethereal",
    "sonnet", "velvet", "nostalgia", "fable", "labyrinth", "luminous",
    "cascade", "gossamer", "charisma", "ephemeral", "illuminate", "azure",
    "petrichor", "oblivion", "ephemeral", "luminescent"
]

adjectives = [
    "gentle", "sparkling", "mysterious", "whispering", "ancient", "enchanting",
    "radiant", "vivid", "tranquil", "captivating", "bewitching", "sublime",
    "majestic", "ethereal", "ephemeral", "serene", "luminous", "surreal",
    "harmonious", "melancholic", "effervescent", "elusive", "transient",
    "rhapsodic", "majestic", "resplendent", "sensual", "sorcerous", "soothing",
    "cosmic", "diaphanous", "ineffable", "lustrous", "empyrean", "celestial",
    "infinite", "ethereal", "effulgent", "enigmatic", "transcendent",
    "oblivious", "celestial", "resonant", "tranquil", "imperceptible",
    "iridescent", "lustrous", "luminescent", "nebulous", "serendipitous",
    "vivid", "effervescent", "ephemeral", "ethereal", "scintillating",
    "enigmatic", "serene", "luminous", "resplendent", "effulgent", "tranquil",
    "nebulous", "ineffable", "celestial", "lustrous", "ephemeral", "ethereal",
    "effervescent", "scintillating", "resplendent", "enigmatic", "luminous",
    "ethereal", "serene", "tranquil", "ephemeral", "resplendent", "effulgent",
    "nebulous", "celestial", "scintillating", "lustrous", "enigmatic",
    "ephemeral", "ethereal"
]

verbs = [
    "dances", "sings", "dreams", "whispers", "cries", "enchants",
    "illuminates", "resonates", "awakens", "embraces", "yearns", "descends",
    "ascends", "waltzes", "invokes", "stirs", "echoes", "radiates", "savors",
    "penetrates", "harmonizes", "sweeps", "lingers", "beckons", "melts",
    "reveals", "conceals", "entwines", "weaves", "spirals", "ignites",
    "enthralls", "devours", "captivates", "echoes", "savors", "permeates",
    "shrouds", "entices", "intrigues", "intoxicates", "glimmers",
    "intertwines", "quivers", "whirls", "dazzles", "entangles", "vanishes",
    "consumes", "disentangles", "beholds", "bewitches", "resounds",
    "resonates", "envelops", "transcends", "illumines", "enraptures",
    "envelops", "whirls", "resounds", "illuminates", "immerses", "captivates",
    "beckons", "entices", "resonates", "shimmers", "stirs", "entwines",
    "unfurls", "intertwines", "enraptures", "resonates", "invokes", "whirls",
    "imbibes", "shimmers", "bewitches", "resounds", "enraptures", "whirls",
    "envelops", "resonates", "immerses", "entwines", "beckons", "resounds",
    "illuminates", "beckons"
]

adverbs = [
    "softly", "silently", "tenderly", "gracefully", "lonely", "gently",
    "whisperingly", "ethereally", "dreamily", "passionately", "delicately",
    "soulfully", "mystically", "serenely", "enchantingly", "effortlessly",
    "melodically", "harmoniously", "subtly", "luminously", "transcendentally",
    "captivatingly", "rhapsodically", "gracefully", "tenderly", "intimately",
    "bewitchingly", "soothingly", "entrancingly", "sensually", "dreamily",
    "whisperingly", "radiantly", "transcendentally", "mesmerizingly",
    "lustrously", "effervescently", "silently", "celestially", "tenderly",
    "enigmatically", "serenely", "luminously", "resplendently", "whisperingly",
    "harmoniously", "ethereally", "tranquilly", "dreamily", "effortlessly",
    "gracefully", "soulfully", "rhapsodically", "mystically", "passionately",
    "luminously", "silently", "tenderly", "gracefully", "lonely", "gently",
    "whisperingly", "ethereally", "dreamily", "passionately", "delicately",
    "soulfully", "mystically", "serenely"
]

# Function to generate a random line of the poem
def generate_line():
  line = f"{random.choice(articles)} {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)} {random.choice(adverbs)}"
  return line


# Function to generate a random poem
def generate_poem(num_lines):
  poem = [generate_line() for _ in range(num_lines)]
  return "\n".join(poem)


# Function to update the poem text
def update_poem():
    poem = generate_poem(5)
    poem_text.set(poem)

# Create a simple Tkinter window
root = tk.Tk()
root.title("Elegist")

# Configure the background color of the window
root.configure(bg='#d087f5')  

# Create a StringVar to hold the poem text
poem_text = tk.StringVar()

# Create and configure widgets with custom colors
poem_label = tk.Label(root, textvariable=poem_text, font=("Arial", 12), wraplength=600, justify="center", bg='#d89ff5', fg='#f0f0f0') 

# Background and foreground color
generate_button = tk.Button(root, text="Another One", command=update_poem, bg='#ea9bfa', fg='white')  

# Place widgets in the window
poem_label.pack(pady=10)
generate_button.pack(pady=10)

# Initial poem generation
update_poem()

# Start the Tkinter event loop
root.mainloop()

