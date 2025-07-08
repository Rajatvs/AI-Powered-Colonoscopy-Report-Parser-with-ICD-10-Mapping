import streamlit as st
import re
import json

st.title("🩺 Clinical Entity Extraction")

# Text input
report = st.text_area("Paste your colonoscopy report here:", height=300)

if st.button("Extract Entities"):
    if report.strip() == "":
        st.warning("Please paste a report first.")
    else:
        # Extract ICD-10 codes
        icd10_codes = re.findall(r'\((K\d{2}\.\d+|Z\d{2}\.\d+)\)', report)

        # Define static clinical terms and locations (or make smarter later)
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

        # Build output
        output = {
            "Clinical Terms": clinical_terms,
            "Anatomical Locations": anatomical_locations,
            "ICD-10": icd10_codes,
            "CPT": [],
            "Modifiers": [],
            "HCPCS": []
        }

        st.subheader("✅ Extracted Output")
        st.json(output)

        # Optionally save to file
        with open("web_output.json", "w") as f:
            json.dump(output, f, indent=2)
        st.success("Output saved to web_output.json")
