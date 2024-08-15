import yaml

def wrap_th(text: str) -> str:
    return f"<th>{text}</th>"

def generate_one(id: str) -> str:
    file_name = f"lists/{id}.yml"
    html_td = "<tr>"
    with open(file_name, "r") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
            return "Error: Invalid YAML"
    # TODO: add table cells
    return html_td + "</tr>"
