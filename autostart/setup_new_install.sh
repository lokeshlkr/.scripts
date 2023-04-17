#! /usr/bin/sh

sudo pacman -Syyu
sudo pacman -S redshift sxhkd xfce4-genmon-plugin rofi alacritty paru
paru -S vscodium
mkdir ~/.config
mkdir ~/.config/sxhkd
ln ~/working_folder/.scripts/configs/sxhkdrc ~/.config/sxhkd/sxhkdrc
sudo ln ~/working_folder/.scripts/shortcut-helper/shelp.py /usr/bin/s