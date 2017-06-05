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

def generateTweakDepics(depics_path, package):
    if not os.path.exists(depics_path + str(package)):
        os.makedirs(depics_path + str(package))

def createInfoXML(path, p_id, name, version, miniOS, pack_dependencies, description, use_screen, screen_desc, screen_img, first_changelog, use_link, link_title, link_url, iconclass):
    print("\nCreating Info XML file...")

    generateTweakDepics(path, p_id)

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
    if use_screen:
        if not os.path.exists(path + str(package) + "/screenshots"):
            os.makedirs(path + str(package) + "/screenshots")

        shot1 = ET.SubElement(screenshots, "screenshot")
        ET.SubElement(shot1, "description").text = str(screen_desc)
        ET.SubElement(shot1, "image").text = str(screen_img)
    else:
        screenshots.text = ""

    changelog = ET.SubElement(package, "changelog")
    ET.SubElement(changelog, "change").text = str(first_changelog)

    links = ET.SubElement(package, "links")
    if use_link:
        if not os.path.exists(path + p_id + "/screenshots"):
            os.makedirs(path + p_id + "/screenshots")

        link1 = ET.SubElement(links, "link")
        ET.SubElement(link1, "name").text = str(link_title)
        ET.SubElement(link1, "url").text = str(link_url)
        ET.SubElement(link1, "iconclass").text = str(iconclass)
    else:
        links.text = ""

    path_to_xml = str(path) + p_id + "/info.xml"

    tree = ET.ElementTree(package)
    tree.write(path_to_xml)

    xmlstr = minidom.parseString(ET.tostring(package)).toprettyxml(indent="   ")
    with open(path_to_xml, "w") as f:
        f.write(xmlstr)
        f.close()

    removeXMLVersion(path_to_xml)
    print("Done!")

def createChangelogXML(path, package_id, version, change):
    print("Creating Changelog XML file...")

    generateTweakDepics(path, package_id)

    path_to_xml = str(path) + package_id + "/changelog.xml"

    log = ET.Element("changelog")
    changes = ET.SubElement(log, "changes")
    ET.SubElement(changes, "version").text = str(version)
    ET.SubElement(changes, "change").text = str(change)

    tree = ET.ElementTree(log)
    tree.write(path_to_xml)

    xmlstr = minidom.parseString(ET.tostring(log)).toprettyxml(indent="   ")
    with open(path_to_xml, "w") as f:
        f.write(xmlstr)
        f.close()

    removeXMLVersion(path_to_xml)
    print("Done!")
