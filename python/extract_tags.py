import json


# Load existing mockup.json
with open("sample_outputs/mockup.json","r") as f:
    data = json.load(f)



# Add caption and tags
data["caption"] =caption
data["tags"] =tags



# Save back to mockup.json
with open("sample_outputs/mockup.json","w") as f:
    json.dump(data,f,indent=4)

print("✅ mockup.json updated with caption and tags.")
