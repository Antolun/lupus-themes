#!/usr/bin/python3
from luppo.actionsapi import luppotools
from luppo.actionsapi import shelltools
import os

WorkDir = "."

def build():
    pass

def install():
    src_dir = os.environ.get("LUPUS_THEMES_SRC_DIR", os.getcwd())

    wallpapers_dir = os.path.join(src_dir, "wallpapers", "LupuS")

    if not os.path.isdir(wallpapers_dir):
        wallpapers_dir = "wallpapers/LupuS"
    if os.path.isdir(wallpapers_dir):
        luppotools.insinto("/usr/share/wallpapers", wallpapers_dir)

    wallpapers2_dir = os.path.join(src_dir, "wallpapers", "Blue")

    if not os.path.isdir(wallpapers2_dir):
        wallpapers2_dir = "wallpapers/Blue"
    if os.path.isdir(wallpapers2_dir):
        luppotools.insinto("/usr/share/wallpapers", wallpapers2_dir)

    wallpapers3_dir = os.path.join(src_dir, "wallpapers", "BlueBerry")

    if not os.path.isdir(wallpapers3_dir):
        wallpapers3_dir = "wallpapers/BlueBerry"
    if os.path.isdir(wallpapers3_dir):
        luppotools.insinto("/usr/share/wallpapers", wallpapers3_dir)

    wallpapers4_dir = os.path.join(src_dir, "wallpapers", "Cities")

    if not os.path.isdir(wallpapers4_dir):
        wallpapers4_dir = "wallpapers/Cities"
    if os.path.isdir(wallpapers4_dir):
        luppotools.insinto("/usr/share/wallpapers", wallpapers4_dir)

    wallpapers5_dir = os.path.join(src_dir, "wallpapers", "Wolf")

    if not os.path.isdir(wallpapers5_dir):
        wallpapers5_dir = "wallpapers/Wolf"
    if os.path.isdir(wallpapers5_dir):
        luppotools.insinto("/usr/share/wallpapers", wallpapers5_dir)
    
    plymouth_dir = os.path.join(src_dir, "plymouth", "LupuS")

    if not os.path.isdir(plymouth_dir):
        plymouth_dir = "plymouth/LupuS"
    if os.path.isdir(plymouth_dir):
        luppotools.insinto("/usr/share/plymouth/themes", plymouth_dir)

    plymouth2_dir = os.path.join(src_dir, "plymouth", "LupuS-Spinnner")

    if not os.path.isdir(plymouth2_dir):
        plymouth2_dir = "plymouth/LupuS-Spinner"
    if os.path.isdir(plymouth2_dir):
        luppotools.insinto("/usr/share/plymouth/themes", plymouth2_dir)

    plymouth3_dir = os.path.join(src_dir, "plymouth", "LupuS-Animated")

    if not os.path.isdir(plymouth3_dir):
        plymouth3_dir = "plymouth/LupuS-Animated"
    if os.path.isdir(plymouth3_dir):
        luppotools.insinto("/usr/share/plymouth/themes", plymouth3_dir)
    
    laf_dir = os.path.join(src_dir, "look-and-feel", "LupuS")

    if not os.path.isdir(laf_dir):
        laf_dir = "look-and-feel/LupuS"
    if os.path.isdir(laf_dir):
        luppotools.insinto("/usr/share/plasma/look-and-feel", laf_dir)

    icons_dir = os.path.join(src_dir, "icons", "LupuS")

    if not os.path.isdir(icons_dir):
        icons_dir = "icons/LupuS"
    if os.path.isdir(icons_dir):
        luppotools.insinto("/usr/share/icons", icons_dir)

    lupus_path = os.path.join(src_dir, "lupus.png")
    
    if not os.path.isfile(lupus_path):
        lupus_path = "lupus.png"
    if os.path.isfile(lupus_path):
        luppotools.insinto("/usr/share/icons", lupus_path)

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
