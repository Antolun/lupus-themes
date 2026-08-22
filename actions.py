#!/usr/bin/python3
from luppo.actionsapi import luppotools
from luppo.actionsapi import shelltools
import os

WorkDir = "."

def build():
    pass

def install():
    src_dir = os.environ.get("LUPUS_THEMES_SRC_DIR", os.getcwd())

    wallpapers_dir = os.path.join(src_dir, "wallpapers", "lupus-default")
    plymouth_dir = os.path.join(src_dir, "plymouth", "lupus-default")
    laf_dir = os.path.join(src_dir, "look-and-feel", "lupus-default")
    icons_dir = os.path.join(src_dir, "icons", "lupus-default")
    cscheme_path = os.path.join(src_dir, "color-schemes", "lupus-default.colors")
    
    if not os.path.isfile(cscheme_path):
        cscheme_path = "color-schemes/lupus-default.colors"
    if os.path.isfile(cscheme_path):
        luppotools.insinto("/usr/share/color-schemes", cscheme_path)
    
    if not os.path.isdir(wallpapers_dir):
        wallpapers_dir = "wallpapers/lupus-default"
    if os.path.isdir(wallpapers_dir):
        luppotools.insinto("/usr/share/wallpapers", wallpapers_dir)
        
    if not os.path.isdir(plymouth_dir):
        plymouth_dir = "plymouth/lupus-default"
    if os.path.isdir(plymouth_dir):
        luppotools.insinto("/usr/share/plymouth/themes", plymouth_dir)

    if not os.path.isdir(laf_dir):
        laf_dir = "look-and-feel/lupus-default"
    if os.path.isdir(laf_dir):
        luppotools.insinto("/usr/share/plasma/look-and-feel", laf_dir)

    if not os.path.isdir(icons_dir):
        icons_dir = "icons/lupus-default"
    if os.path.isdir(icons_dir):
        luppotools.insinto("/usr/share/icons", icons_dir)

    readme_path = os.path.join(src_dir, "README.md")
    if not os.path.isfile(readme_path):
        readme_path = "README.md"
    if os.path.isfile(readme_path):
        luppotools.dodoc(readme_path)

    license_path = os.path.join(src_dir, "LICENSE")
    if not os.path.isfile(license_path):
        license_path = "LICENSE"
    if os.path.isfile(license_path):
        luppotools.dodoc(license_path)
