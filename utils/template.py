html_template = """<h1>{part_number}</h1><p>{short_description}</p><h2>Key Features</h2><p>{key_features}</p><h2>Details</h2><p>{long_description}</p><h2>Specifications</h2><ul><li><strong>HP Gains:</strong> {hp_gains} HP</li><li><strong>Torque Gains:</strong> {tq_gains} ft/lbs</li><li><strong>Replacement Filter:</strong> {filter}</li><li><strong>Black Hydroshield:</strong> {black_hydroshield}</li><li><strong>Red Hydroshield:</strong> {red_hydroshield}</li><li><strong>Prop 65 Information:</strong> {prop_65_compliance}</li></ul><h3>Shipping Information</h3><ul><li><strong>Weight:</strong> {weight_lbs} lbs</li><li><strong>Box Dimensions:</strong></li><li>Length: {box_length_inches} in</li><li>Width: {box_width_inches} in</li><li>Height: {box_height_inches} in</li><li><strong>UPC Code:</strong> {upc_code}</li></ul><h3>CARB Information</h3><ul><li><strong>Compliance Specification:</strong> {compliance_specification}</li><li><strong>CARB Model Year Coverage:</strong> {carb_model_years}</li><li><strong>Notes:</strong> {carb_fitment_notes}</li></ul><h2>Product Image</h2>{product_image}<h2>Additional Information</h2><ul><li>Category: {category}</li><li>Year: {year}</li><li>Make: {make}</li><li>Model: {model}</li><li>Engine: {engine}</li><li>Cylinder: {cylinder}</li><li>Fuel: {fuel}</li></ul><h2>Other Details</h2><ul><li>MAP: {map}</li></ul><h3>Warranty Information</h3><p>{warranty_info_or_document}</p>"""

shopify_field_names = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Type", "Tags", "Published", 
    "Option1 Name", "Option1 Value", "Option2 Name", "Option2 Value", "Option3 Name", "Option3 Value", 
    "Variant SKU", "Variant Grams", "Variant Inventory Tracker", "Variant Inventory Qty", 
    "Variant Inventory Policy", "Variant Fulfillment Service", "Variant Price", "Variant Compare At Price", 
    "Variant Requires Shipping", "Variant Taxable", "Variant Barcode", 
    "Image Src", "Image Position", "Image Alt Text", "Gift Card", 
    "SEO Title", "SEO Description", "Google Shopping / Google Product Category", 
    "Google Shopping / Gender", "Google Shopping / Age Group", "Google Shopping / MPN", 
    "Google Shopping / AdWords Grouping", "Google Shopping / AdWords Labels", "Google Shopping / Condition", 
    "Google Shopping / Custom Product", "Google Shopping / Custom Label 0", "Google Shopping / Custom Label 1", 
    "Google Shopping / Custom Label 2", "Google Shopping / Custom Label 3", "Google Shopping / Custom Label 4", 
    "Variant Image", "Variant Weight Unit", "Variant Tax Code", "Cost per item"
]
"""
PARA LLENAR EL TEMPLATE:
product_info = {
    "part_number": "12345",
    "short_description": "Performance Air Intake Kit",
    "key_features": "- Direct fit for the 1990-1993 Acura Integra L4-1.8L<br>"
                    "- Fits ABS equipped models<br>"
                    "- Provides power gains while maintaining A/F ratios with no additional tuning<br>"
                    "- T6-6061 Mandrel-bent aluminum intake tubing<br>"
                    "- Fully serviceable Injen SuperNano-Web dry air filter<br>"
                    "- Replacement air filter part number X-1014-BB<br>"
                    "- Optional hydroshield part number 1033BLK or 1033RED<br>"
                    "- Available with a polished or laser black powder coated finish<br>"
                    "- Aggressive engine tone under full throttle<br>"
                    "- Smooth mandrel-bent Intake piping eliminates restrictions and improves airflow<br>"
                    "- Made in Pomona California, USA<br>"
                    "- Injen Technology Limited Lifetime Warranty<br>"
                    "- CARB EO #: D-476",
    "long_description": "Add some easy horsepower to your Acura Integra with this Injen Technology IS Performance short ram air intake! Our engineers spent abundant amounts of time designing, testing, and perfecting the IS400P to produce some serious bolt-on power with some killer Horsepower increase. In addition to the impressive power increase, the Injen team has ensured that safe Air fuel (A/F) ratios are maintained throughout the powerband. The soul of this intake it is our mandrel-bent aluminum air intake tube that provides a smooth uninterrupted path for highly efficient airflow. Additionally, this kit also includes a fully serviceable Injen SuperNano-Web dry air filter, which provides increased filter surface area, allowing for greater airflow and unbeatable filtration. This Injen IS performance intake provides the power you can hear! It is truly an upgrade for intake noise and provides an aggressive throaty tone, especially when you put the hammer down. Want to add a personalized touch? Well, you are in luck, we offer this kit in a polished finish or a powder-coated laser black. Plus, just like any other Injen air intake systems, this intake kit includes the unbeatable Injen limited Lifetime Warranty!",
    "hp_gains": "N/A HP",
    "tq_gains": "N/A ft/lbs",
    "filter": "X-1014-BB",
    "black_hydroshield": "1033BLK",
    "red_hydroshield": "1033RED",
    "prop_65_compliance": "This product can expose you to chemicals including Chromium, Nickel, Carbon Black & Cobalt, which are known to the State of California to cause cancer, and (Antimony [Oxide], Arsenic, Beryllium. Chromium (hexavalent), Cobalt Cadmium, Lead, and Nickel, which is known to the State of California to cause birth defects or other reproductive harm.",
    "weight_lbs": "5 lbs",
    "box_length_inches": "26",
    "box_width_inches": "13",
    "box_height_inches": "9",
    "upc_code": "843115000530",
    "compliance_specification": "D-476",
    "carb_model_years": "1990-1993",
    "carb_fitment_notes": "",
    "warranty_info_or_document": "Injen Technology offers a Limited Lifetime Warranty to the original purchaser against defects in material and workmanship on all intake systems, air filters, and hydroshields. Injen Technology will replace, at no charge, any intake pipe, air filter, or hydroshield considered by Injen Technology to be defective. Any and all warranty coverage is limited to the repair or replacement of the defective part only, at Injen Technology's discretion. Proof of purchase is required. The warranty does not cover incidental or consequential damages, damages caused from improper installation, nor does it cover the cost of installation or removal of the defective part or its replacement. All warranty items must be sent freight prepaid with a valid RMA (Return Merchandise Authorization) number and copy of the original invoice.",
    "product_image": "product_image.jpg",
    "category": "Automotive",
    "year": "1990",
    "make": "Acura",
    "model": "Integra",
    "engine": "L4-1.8L",
    "cylinder": "4",
    "fuel": "Gasoline",
    "map": "$299.99",
    "available": "Yes",
    "manual": "Yes"
}

# Apply the variables to the template
filled_html = html_template.format(**product_info)

# Now, 'filled_html' contains the HTML code with the variables replaced.


"""