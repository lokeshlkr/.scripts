#! /usr/bin/sh

# only for arch-based xfce distro

# install stranger nerd fonts first

sudo cp ~/working_folder/.scripts/fonts/StragerMonoNF/* /usr/share/fonts/
sudo cp ~/working_folder/.scripts/fonts/StragerSansNF/* /usr/share/fonts/

sudo pacman -Syyu
sudo pacman -S redshift sxhkd xfce4-genmon-plugin rofi alacritty paru
paru -S vscodium

mkdir ~/.config
mkdir ~/.config/sxhkd
ln ~/working_folder/.scripts/configs/sxhkdrc ~/.config/sxhkd/sxhkdrc

mkdir ~/.config/alacritty
ln ~/working_folder/.scripts/configs/alacritty.yml ~/.config/alacritty/alacritty.yml

sudo ln ~/working_folder/.scripts/shortcut-helper/shelp.py /usr/bin/s