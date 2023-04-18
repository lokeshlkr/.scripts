#! /usr/bin/sh

# only for arch-based xfce distro

# install stranger nerd fonts first

sudo cp ~/working_folder/.scripts/fonts/StragerMonoNF/* /usr/share/fonts/
sudo cp ~/working_folder/.scripts/fonts/StragerSansNF/* /usr/share/fonts/

sudo pacman -Syyu
sudo pacman -S redshift sxhkd xfce4-genmon-plugin rofi alacritty paru
paru -S vscodium gnome-keyring

mkdir ~/.config
mkdir ~/.config/sxhkd
ln ~/working_folder/.scripts/configs/sxhkdrc ~/.config/sxhkd/sxhkdrc

mkdir ~/.config/alacritty
ln ~/working_folder/.scripts/configs/alacritty.yml ~/.config/alacritty/alacritty.yml

mkdir ~/.config/rofi
ln ~/working_folder/.scripts/configs/config.rasi ~/.config/rofi/config.rasi
ln ~/working_folder/.scripts/configs/rofi-theme.rasi ~/.config/rofi/rofi-theme.rasi

echo "" >> ~/.bashrc
echo "source ~/working_folder/.scripts/configs/bash_extras.sh" >> ~/.bashrc

sudo ln ~/working_folder/.scripts/shortcut-helper/shelp.py /usr/bin/s