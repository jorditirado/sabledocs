import json
import pprint
from proto_json_parser import parse_proto_json
from jinja2 import Environment, FileSystemLoader, select_autoescape

packages = parse_proto_json('description.json')

#pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(packages)

jinja_env = Environment(
    loader=FileSystemLoader(searchpath="./"),
    autoescape=select_autoescape()
)

template = jinja_env.get_template('templates/docs.html.jinja')

print(template.render(packages=packages))
