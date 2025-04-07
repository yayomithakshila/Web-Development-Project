import os
import re

# --- Settings ---
directory = "./pages"  # Folder where the files are
misspelling = "Breakfest"
correct_spelling = "Breakfast"
special_offer_html = "\n<!-- Special Offers -->\n<div class='special-offers'>Weekend Discount - 20% Off</div>\n"
phone_number = "+1-234-567-8900"
contact_keywords = ["contact", "get-in-touch"]  # Keywords to find contact page files

# --- Fix spelling mistakes ---
def fix_spelling(directory, wrong, correct):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            with open(path, 'r+', encoding='utf-8') as file:
                content = file.read()
                new_content = content.replace(wrong, correct)
                if new_content != content:
                    print(f"Fixed spelling in {filename}")
                    file.seek(0)
                    file.write(new_content)
                    file.truncate()

# --- Add special offers section ---
def add_special_offers(directory):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path) and filename.endswith((".html", ".htm")):
            with open(path, 'r+', encoding='utf-8') as file:
                content = file.read()
                if "special-offers" not in content:
                    new_content = content.replace("</body>", special_offer_html + "</body>")
                    print(f"Added special offers section in {filename}")
                    file.seek(0)
                    file.write(new_content)
                    file.truncate()

# --- Add phone number to contact page ---
def add_phone_number(directory, phone, keywords):
    for filename in os.listdir(directory):
        if any(keyword in filename.lower() for keyword in keywords):
            path = os.path.join(directory, filename)
            if os.path.isfile(path):
                with open(path, 'r+', encoding='utf-8') as file:
                    content = file.read()
                    if phone not in content:
                        # Add phone number at the end of the body
                        updated_content = re.sub(r"(</body>)", f"<p>Phone: {phone}</p>\n\\1", content, flags=re.IGNORECASE)
                        print(f"Added phone number to {filename}")
                        file.seek(0)
                        file.write(updated_content)
                        file.truncate()

