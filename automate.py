import sys
import hashlib
import glob
import re
import readline
import os
from os import walk

import cxml

dir_path = os.path.dirname(os.path.abspath(__file__))

print("\nTIP: just press enter if the 'def (default)' suits your needs!\n")

def getUseBool(use):
    if use == "y":
        return True
    elif use == "n":
        return False

def writeToPackages(p_file, package, version, section, maintainer, depends, arch, debloc, desc, name, depic):
    p_file.write("\nPackage: " + str(package))
    p_file.write("\nVersion: " + str(version))
    p_file.write("\nSection: " + str(section))
    p_file.write("\nMaintainer: " + str(maintainer))
    p_file.write("\nDepends: " + str(depends))
    p_file.write("\nArchitecture: " + str(arch))
    p_file.write("\nFilename: " + str(debloc))
    p_file.write("\nSize: " + str(os.path.getsize(str(debloc))))
    p_file.write("\nMD5sum: " + hashlib.md5(open(str(debloc), 'rb').read()).hexdigest())
    p_file.write("\nDescription: " + str(desc))
    p_file.write("\nName: " + str(name))
    p_file.write("\nAuthor: " + str(maintainer))
    if str(depic) != "":
        p_file.write("\nDepiction: " + str(depic))

name = ""
pack_file = input("\nEnter packages file location (def: 'Packages'): ")
if pack_file == "":
    pack_file = "Packages"
pack_path = ""

if pack_file == "Packages":
    pack_path = os.path.abspath(pack_file)
    try:
        open(pack_path, "r")
    except:
        sys.exit("Error: file '{}' is not found".format(pack_path))

    print("Found Packages file in: " + str(pack_path))
else:
    sys.exit("Didn't find Packages file. \nExiting...")

print("\nPreparing to Package file...")
packages_obj = open(pack_path, "a")

print("Starting Packaging session...")
package_i = input("\nPlease enter the package id: ")

version_i = input("Please enter the version: ")

section_i = input("Please enter the section (def: Tweaks): ")
if section_i == "":
    section_i = "Tweaks"

maintainer_i = input("Please enter the maintainer (Name <mail>): ")

depends_i = input("Please enter the dependencies (def: mobilesubstrate): ")
if depends_i == "":
    depends_i = "mobilesubstrate"

arch_i = input("Please enter the Architecture (def: iphoneos-arm): ")
if arch_i == "":
    arch_i = "iphoneos-arm"

debloc_i = input("Please enter the .deb file location (ex: 'debs/my.file.deb'): ")
if debloc_i == "":
    sys.exit("Error: .deb location cannot be empty!")
try:
    open(debloc_i, "r")
except FileNotFoundError:
    sys.exit("Error: file '{}' is not found".format(debloc_i))

desc_i = input("Please enter the description: ")

name_i = input("Please enter the name: ")

depiction_i = input("Please enter the depiction url: ")

min_os = input("Please enter the minimum iOS required (def: 10.0): ")
if min_os == "":
    min_os = "10.0"

path_depics = input("Please enter the path to your depictions folder: ")

changelog = input("Please enter a change log for this version ({}): ".format(version_i))

use_screen = input("Do you have screenshots of this tweak you want to use? (Y/n): ")
image_title = ""
image_path = ""
if use_screen == "" or use_screen.lower() == "y":
    use_screen = "y"
    image_title = input("Please enter the title of your image: ")
    image_path = input("Please enter the path of your image (ex: 'folder/to/screenshots/image.png'): ")
else:
    use_screen = "n"

use_link = input("Do you want to have links for your info.xml? (Y/n): ")
link_title = ""
link_url = ""
link_class = ""
if use_link == "" or use_link.lower() == "y":
    use_link = "y"

    link_title = input("Please enter the title of your link (ex: '/r/jailbreak_'): ")
    link_url = input("Please enter the URL of your title: ")
    link_class = input("Please enter the icon class for your link (def: 'fa fa-reddit'): ")
    if link_class == "":
        link_class = "fa fa-reddit"
else:
    use_link = "n"

print("\nWriting...")
writeToPackages(packages_obj, package_i, version_i, section_i, maintainer_i, depends_i, arch_i, debloc_i, desc_i, name_i, depiction_i)
print("Done!")

print("\nPreparing to create depiction for tweak: {}".format(package_i))


cxml.createInfoXML(path_depics, package_i, name_i, version_i, min_os, depends_i, desc_i, getUseBool(use_screen), image_title, image_path, changelog, getUseBool(use_link), link_title, link_url, link_class)

cxml.createChangelogXML(path_depics, package_i, version_i, changelog)
