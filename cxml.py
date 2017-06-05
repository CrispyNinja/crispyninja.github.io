import sys
import hashlib
import glob
import re
import readline
import os
from os import walk
from xml.dom import minidom

import xml.etree.cElementTree as ET

def removeXMLVersion(path):
    try:
        f = open(str(path), "r")
        lines = f.readlines()

        f = open(str(path), "w")
        f.seek(0)
        for line in lines:
            if line != lines[0]:
                f.write(line)
        f.truncate()
        f.close()
    except FileNotFoundError:
        sys.exit("Error: file '{}' is not found".format(path))

def createInfoXML(path, p_id, name, version, miniOS, pack_dependencies, description, screen_desc, screen_img, first_changelog, link_title, link_url, iconclass):
    print("\nCreating Info XML file...")

    package = ET.Element("package")

    ET.SubElement(package, "id").text = str(p_id)
    ET.SubElement(package, "name").text = str(name)
    ET.SubElement(package, "version").text = str(version)

    comp = ET.SubElement(package, "compatibility")
    firmware = ET.SubElement(comp, "firmware")
    ET.SubElement(firmware, "miniOS").text = str(miniOS)

    dependencies = ET.SubElement(package, "dependencies")
    ET.SubElement(dependencies, "package").text = str(pack_dependencies)

    desclist = ET.SubElement(package, "descriptionlist")
    ET.SubElement(desclist, "description").text = str(description)

    screenshots = ET.SubElement(package, "screenshots")
    shot1 = ET.SubElement(screenshots, "screenshot")
    ET.SubElement(shot1, "description").text = str(screen_desc)
    ET.SubElement(shot1, "image").text = str(screen_img)

    changelog = ET.SubElement(package, "changelog")
    ET.SubElement(changelog, "change").text = str(first_changelog)

    links = ET.SubElement(package, "links")
    link1 = ET.SubElement(links, "link")
    ET.SubElement(link1, "name").text = str(link_title)
    ET.SubElement(link1, "url").text = str(link_url)
    ET.SubElement(link1, "iconclass").text = str(iconclass)

    tree = ET.ElementTree(package)
    tree.write(str(path) + "/info.xml")

    xmlstr = minidom.parseString(ET.tostring(package)).toprettyxml(indent="   ")
    with open(str(path) + "/info.xml", "w") as f:
        f.write(xmlstr)
        f.close()

    removeXMLVersion(tr(path) + "/info.xml")
    print("Done!")

def createChangelogXML(path, version, change):
    print("Creating Changelog XML file...")

    log = ET.Element("changelog")
    changes = ET.SubElement(log, "changes")
    ET.SubElement(changes, "version").text = str(version)
    ET.SubElement(changes, "change").text = str(change)

    tree = ET.ElementTree(log)
    tree.write(str(path) + "/changelog.xml")

    xmlstr = minidom.parseString(ET.tostring(log)).toprettyxml(indent="   ")
    with open(str(path) + "/changelog.xml", "w") as f:
        f.write(xmlstr)
        f.close()

    removeXMLVersion(tr(path) + "/changelog.xml")
    print("Done!")
