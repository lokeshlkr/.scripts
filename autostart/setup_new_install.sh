#! /usr/bin/sh

# only for arch-based xfce distro

# install stranger nerd fonts first

sudo pacman -Syy
sudo pacman -S archlinux-keyring
sudo pacman -Syu
sudo pacman -S redshift sxhkd xfce4-genmon-plugin rofi alacritty paru 
paru -S vscodium gnome-keyring zenity xmodmap

echo "" >> ~/.bashrc
echo "source ~/working_folder/.scripts/configs/bash_extras.sh" >> ~/.bashrc
source ~/.bashrc

sudo cp ~/working_folder/.scripts/fonts/StrangerMonoNF/* /usr/share/fonts/
sudo cp ~/working_folder/.scripts/fonts/StrangerSansNF/* /usr/share/fonts/

mkdir -p ~/.config/sxhkd
ln ~/working_folder/.scripts/configs/sxhkdrc ~/.config/sxhkd/sxhkdrc

mkdir -p ~/.config/alacritty
ln ~/working_folder/.scripts/configs/alacritty.yml ~/.config/alacritty/alacritty.yml

mkdir -p ~/.config/rofi
ln ~/working_folder/.scripts/configs/config.rasi ~/.config/rofi/config.rasi
ln ~/working_folder/.scripts/configs/rofi-theme.rasi ~/.config/rofi/rofi-theme.rasi


sudo ln ~/working_folder/.scripts/shortcut-helper/shelp.py /usr/bin/s