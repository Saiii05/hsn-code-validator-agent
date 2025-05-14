import re
import pandas as pd

def load_hsn_data(file_path):
    df = pd.read_excel(file_path)
    return dict(zip(df["HSNCode"].astype(str).str.strip(), df["Description"]))

def is_valid_format(code):
    return bool(re.fullmatch(r'\d{2}|\d{4}|\d{6}|\d{8}', code))

def validate_hsn(code, hsn_data):
    code = code.strip()
    if not is_valid_format(code):
        return f"{code} is not a valid format. HSN codes must be 2, 4, 6, or 8-digit numbers."
    if code in hsn_data:
        response = f"{code} is a valid HSN code: {hsn_data[code]}"
        hierarchy = [code[:i] for i in [2, 4, 6] if i < len(code)]
        missing_parents = [p for p in hierarchy if p not in hsn_data]
        if missing_parents:
            response += f"\nWarning: Missing parent codes: {', '.join(missing_parents)}"
        return response
    return f"{code} is not found in the HSN master list."
