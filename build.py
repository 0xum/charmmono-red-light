"""Package this local color theme as a VSIX using only Python's standard library."""
import json
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parent
package = json.loads((ROOT / "package.json").read_text())
for theme in package["contributes"]["themes"]:
    json.loads((ROOT / theme["path"]).read_text())

ns = "http://schemas.microsoft.com/developer/vsx-schema/2011"
ET.register_namespace("", ns)


def child(parent, tag, text=None, **attributes):
    element = ET.SubElement(parent, f"{{{ns}}}{tag}", attributes)
    element.text = text
    return element


manifest = ET.Element(f"{{{ns}}}PackageManifest", {"Version": "2.0.0"})
metadata = child(manifest, "Metadata")
child(metadata, "Identity", Language="en-US", Id=package["name"],
      Version=package["version"], Publisher=package["publisher"])
child(metadata, "DisplayName", package["displayName"])
child(metadata, "Description", package["description"])
child(metadata, "Categories", "Themes")
properties = child(metadata, "Properties")
child(properties, "Property", Id="Microsoft.VisualStudio.Code.Engine",
      Value=package["engines"]["vscode"])
child(properties, "Property", Id="Microsoft.VisualStudio.Code.ExtensionKind", Value="ui,workspace,web")
child(metadata, "License", "extension/LICENSE.txt")
installation = child(manifest, "Installation")
child(installation, "InstallationTarget", Id="Microsoft.VisualStudio.Code")
child(manifest, "Dependencies")
assets = child(manifest, "Assets")
for kind, filename in [
    ("Microsoft.VisualStudio.Code.Manifest", "package.json"),
    ("Microsoft.VisualStudio.Services.Content.Details", "README.md"),
    ("Microsoft.VisualStudio.Services.Content.License", "LICENSE.txt"),
]:
    child(assets, "Asset", Type=kind, Path=f"extension/{filename}", Addressable="true")

content_types = b'''<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="json" ContentType="application/json"/>
  <Default Extension="md" ContentType="text/markdown"/>
  <Default Extension="txt" ContentType="text/plain"/>
  <Default Extension="vsixmanifest" ContentType="text/xml"/>
</Types>'''

destination = ROOT / "dist" / f'{package["name"]}-{package["version"]}.vsix'
destination.parent.mkdir(exist_ok=True)
files = ["package.json", "README.md", "LICENSE.txt"]
files += [theme["path"] for theme in package["contributes"]["themes"]]
with ZipFile(destination, "w", compression=ZIP_DEFLATED) as archive:
    archive.writestr("[Content_Types].xml", content_types)
    archive.writestr("extension.vsixmanifest", ET.tostring(manifest, encoding="utf-8", xml_declaration=True))
    for filename in files:
        archive.write(ROOT / filename, "extension/" + filename.removeprefix("./"))
print(destination)
