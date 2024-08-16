import yaml
import os
import htmlmin

def wrap_td(text: str) -> str:
    return f"<td>{text}</td>"

def generate_one(id: str) -> str:
    if " " in id or "/" in id or "\\" in id:
        print("Error: Invalid ID (contains space or slash)")
        exit(1)
    file_name = f"lists/{id}.yml"
    html_td = "<tr>"
    with open(file_name, "r") as f:
        try:
            data = yaml.safe_load(f)
            list_title = data["title"]
            list_id = data["id"]
            if list_id != id:
                print(f"Error: ID mismatch ({list_id} != {id})")
                exit(1)
            list_description = data["description"]
            list_date = data["update-date"]
            list_owner = data["owner"]["name"]
            try:
                list_owner_url = data["owner"]["url"]
            except KeyError:
                list_owner_url = None
            list_url = "/lists/" + list_id + ".yml"
            html_td += wrap_td(f'<a href="{list_url}" download>{list_title}</a>')
            html_td += wrap_td(f'<a href="{list_url}" download class="text-tt">{list_id}</a>')
            html_td += wrap_td(list_description)
            if list_owner_url:
                html_td += wrap_td(f'<a href="{list_owner_url}" target="_blank">{list_owner}</a>')
            else:
                html_td += wrap_td(list_owner)
            html_td += wrap_td(list_date)
        except yaml.YAMLError as exc:
            print(exc)
            print("Error: Invalid YAML")
            exit(1)
    return html_td + "</tr>"

def generate_all() -> str:
    table_rows = ""
    # iterate all YML files in the directories "lists/", as ID
    for file in sorted(os.listdir("lists")):
        if file.endswith(".yml"):
            table_rows += generate_one(file[:-4])
    return table_rows

def main() -> None:
    with open("index_template.html", "r") as f:
        html = f.read()
        html = html.replace("<!-- # LISTS # -->", generate_all())
        html = htmlmin.minify(html, remove_empty_space=True)
    with open("index.html", "w") as f:
        f.write(html)

if __name__ == "__main__":
    main()
