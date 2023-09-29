import pandas as pd
import pyfiglet
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tqdm import tqdm
from utils.template import html_template, shopify_field_names

def process_key_features(text):
    # Split the text into individual items
    items = text.split('\n')

    # Create an HTML list
    html_list = "<ul>"

    for item in items:
        # Remove leading "•" and strip any leading/trailing whitespace
        item = item.lstrip('•').strip()
        
        # Add the item as an HTML list item
        html_list += f"<li>{item}</li>"

    # Close the HTML list
    html_list += "</ul>"
    return html_list

def process_images(images_df, part_number, get_1st_url=False):
    if not get_1st_url:
        images_df = images_df[images_df['Part Number'] == part_number]

        # Create an HTML grid
        html = "<div class='image-grid'>"

        # Loop through the images and generate HTML for each
        for index, row in images_df.iterrows():
            html += f"<div class='image'><img src='{row['URL']}' alt='{row['Part Number']}'></div>"

        # Close the HTML grid
        html += "</div>"
        return html
    else:
        try:
            images_df = images_df[images_df['Part Number'] == part_number]
            return images_df.iloc[0]['URL']
        except:
            return ""
        
def clean_text(text):
    return text.replace('\n', '')


def to_shopify_csv(path_to_excel, path_to_images):

    print("Reading excel data...\n")

    raw_data = pd.read_excel(path_to_excel)
    images_df = pd.read_csv(path_to_images)

    print("Creating shopify csv...\n")

    shopify_df = pd.DataFrame(columns=shopify_field_names)
    for index, row in tqdm(raw_data.iterrows(), total=len(raw_data)):
        shopify_df.loc[index, "Handle"] = f"injen-{row['Part Number']}-{row['UPC Code']}"
        shopify_df.loc[index, "Title"] = f"Injen {row['Part Number']} - {clean_text(row['Product Title'])}"
        shopify_df.loc[index, "Body (HTML)"] = html_template.format(
            part_number=row["Part Number"],
            short_description=clean_text(row["Short Description"]),
            key_features=process_key_features(row["Key Features"]),
            long_description=clean_text(row["Long Description"]),
            hp_gains=row["HP Gains"],
            tq_gains=row["TQ Gains"],
            filter=row["Filter"],
            black_hydroshield=row["Black Hydroshield"],
            red_hydroshield=row["Red Hydroshield"],
            prop_65_compliance=row["Prop 65 Compliance"],
            weight_lbs=row["Weight\n(Lbs)"],
            box_length_inches=row["Box L (inches)"],
            box_width_inches=row["Box W (inches)"],
            box_height_inches=row["Box H (inches)"],
            upc_code=row["UPC Code"],
            compliance_specification="No EO#",
            carb_model_years=row["CARB Model Years"],
            carb_fitment_notes=row["CARB Fitment notes"],
            warranty_info_or_document=clean_text(row["Warranty Information or Document"]),
            product_image=process_images(images_df, row["Part Number"]),
            category=row["Category"],
            year=row["Year"],
            make=row["Make"],
            model=row["Model"],
            engine=row["Engine"],
            cylinder=row["Cylinder"],
            fuel=row["Fuel"],
            map=row["MAP"]
        )
        shopify_df.loc[index, "Vendor"] = "Injen Technology"
        shopify_df.loc[index, "Type"] = f"{row['Category']} Intake"
        shopify_df.loc[index, "Tags"] = f"{row['Part Number']} - {clean_text(row['Short Description'])}"
        shopify_df.loc[index, "Published"] = "TRUE"
        shopify_df.loc[index, "Option1 Name"] = "Title"
        shopify_df.loc[index, "Option1 Value"] = "Default Title"
        shopify_df.loc[index, "Variant SKU"] = row["Part Number"]
        shopify_df.loc[index, "Variant Grams"] = str(round(float(row["Weight\n(Lbs)"]) * 453.592, 2))
        shopify_df.loc[index, "Variant Inventory Qty"] = "0"
        shopify_df.loc[index, "Variant Inventory Policy"] = "continue"
        shopify_df.loc[index, "Variant Fulfillment Service"] = "manual"
        shopify_df.loc[index, "Variant Price"] = f"{row['MAP']}"
        shopify_df.loc[index, "Variant Requires Shipping"] = "TRUE"
        shopify_df.loc[index, "Variant Taxable"] = "TRUE"
        shopify_df.loc[index, "Variant Barcode"] = row["UPC Code"]
        shopify_df.loc[index, "Image Src"] = process_images(images_df, row["Part Number"], get_1st_url=True)
        shopify_df.loc[index, "Image Position"] = "1"
        shopify_df.loc[index, "Image Alt Text"] = row["Part Number"]
        shopify_df.loc[index, "Gift Card"] = "FALSE"
        shopify_df.loc[index, "SEO Title"] = f"{row['Part Number']} - {clean_text(row['Short Description'])}"
        shopify_df.loc[index, "SEO Description"] = clean_text(row["Long Description"])
        shopify_df.loc[index, "Variant Weight Unit"] = "lb"

    return shopify_df


if __name__ == "__main__":
    print(pyfiglet.figlet_format("Aftermarket Race Plug"))
    shopify_df = to_shopify_csv("data/Master Jobber_10_14_2020_JC.xlsx", "data/image-links.csv")
    os.makedirs("output", exist_ok=True)
    shopify_df.to_csv("output/shopify.csv", index=False, encoding='utf-8', na_rep='')