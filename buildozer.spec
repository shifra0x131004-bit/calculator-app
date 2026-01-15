[app]
title = CalculatorX
package.name = calculatorx
package.domain = org.calculator

source.dir = .
source.include_exts = py

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

icon.filename =

[buildozer]
log_level = 2

[android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.archs = arm64-v8a,armeabi-v7a
