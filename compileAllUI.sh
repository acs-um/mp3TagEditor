#!/usr/bin/env bash
pyrcc5 UI/images.qrc -o Source/images_rc.py #convertir recursos

pyuic5 UI/mainWindows.ui -o Source/mainWindows.py --from-imports #ui a .py




