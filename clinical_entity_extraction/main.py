import re
import json

# Step 1: Colonoscopy report
report = """
Patient Name: Alex Johnson
Date: 8/15/2025
Procedure: Colonoscopy
Endoscopist: Sarah Lee, MD

Indications:
Chronic constipation (K59.00)
Family history of colon cancer (Z80.0)

Findings:
Single 5 mm sessile polyp in the sigmoid colon. Removed completely with cold snare.
Otherwise normal colon.

Impression:
5 mm sigmoid polyp (K63.5)
Normal remainder of colon.

Plan:
Await pathology results.
Recommend repeat colonoscopy in 5 years.
"""

# Step 2: Extract ICD-10 codes
icd10_codes = re.findall(r'\((K\d{2}\.\d+|Z\d{2}\.\d+)\)', report)
print("ICD-10 Codes:", icd10_codes)

# Step 3.5: Map ICD-10 codes to their descriptions
icd10_mapping = {
    "K59.00": "Chronic constipation",
    "Z80.0": "Family history of colon cancer",
    "K63.5": "Polyp of colon"
}

# Create a list of mapped descriptions
mapped_descriptions = [icd10_mapping.get(code, "Unknown") for code in icd10_codes]


# Step 3: Clinical terms and anatomical locations
clinical_terms = [
    "chronic constipation",
    "family history of colon cancer",
    "sessile polyp",
    "colonoscopy"
]

anatomical_locations = [
    "sigmoid colon",
    "colon"
]

# Step 4: Output dictionary
output = {
    "Clinical Terms": clinical_terms,
    "Anatomical Locations": anatomical_locations,
    "ICD-10": icd10_codes,
    "ICD-10 Descriptions": mapped_descriptions,
    "CPT": [],
    "Modifiers": [],
    "HCPCS": []
}


# Debugging line: print output before saving
print("Final output to be saved:\n", output)

# Step 5: Save to JSON
with open("sample_output.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ Extraction complete! Output saved to sample_output.json")
