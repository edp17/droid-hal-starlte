# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device starlte
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy S9

%define installable_zip 1

%define enable_kernel_update 1

%define android_config \
#define MALI_QUIRKS 1\
%{nil}

%define additional_ha_groups \
system\
%{nil}

#decomission sys-fs-pstore.service
%define makefstab_skip_entries /sys/fs/pstore

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

