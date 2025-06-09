def evaluate_material(material_name, temp_limit, radiation_limit):
    materials = {
        "C-C Composite": {"temp_limit": 3000, "radiation": "high"},
        "MLI Aluminum/Mylar": {"temp_limit": 500, "radiation": "medium"},
    }
    mat = materials.get(material_name)
    if not mat:
        return "Material not found"

    return (
            temp_limit <= mat["temp_limit"]
            and radiation_limit in ["low", mat["radiation"]]
    )
