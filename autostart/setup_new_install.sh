#! /usr/bin/sh

# only for arch-based xfce distro
# install stranger nerd fonts first

sudo pacman -Syy                 # update all repositories
sudo pacman -S archlinux-keyring # update arch-linux keyring
sudo pacman -Syu                 # update whole system
sudo pacman -S paru              # install paru (AUR helper)
paru -S redshift
paru -S sxhkd 
paru -S xfce4-genmon-plugin 
paru -S rofi 
paru -S alacritty 
paru -S vscodium 
paru -S gnome-keyring 
paru -S zenity 
paru -S xmodmap 
paru -S imagemagick 
paru -S ksuperkey
paru -S copyq 

echo "" >> ~/.bashrc
echo "source ~/working_folder/.scripts/configs/bash_extras.sh" >> ~/.bashrc
source ~/.bashrc

sudo cp ~/working_folder/.scripts/fonts/StrangerMono/* /usr/share/fonts/
sudo cp ~/working_folder/.scripts/fonts/StrangerSans/* /usr/share/fonts/
sudo cp ~/working_folder/.scripts/fonts/GoogleSans/* /usr/share/fonts/
sudo cp ~/working_folder/.scripts/fonts/JetBrainsMono/* /usr/share/fonts/
sudo cp ~/working_folder/.scripts/fonts/Inter/* /usr/share/fonts/

mkdir -p ~/.config/sxhkd
ln -s ~/working_folder/.scripts/configs/sxhkdrc ~/.config/sxhkd/sxhkdrc

mkdir -p ~/.config/alacritty
ln -s ~/working_folder/.scripts/configs/alacritty.yml ~/.config/alacritty/alacritty.yml

mkdir -p ~/.config/helix
ln -s ~/working_folder/.scripts/configs/helix.toml ~/.config/helix/config.toml

mkdir -p ~/.config/rofi
ln -s ~/working_folder/.scripts/configs/config.rasi ~/.config/rofi/config.rasi
ln -s ~/working_folder/.scripts/configs/rofi-theme.rasi ~/.config/rofi/rofi-theme.rasi

mkdir -p ~/.themes
mkdir -p ~/.icons
cp ~/working_folder/.scripts/xfce/.themes/* ~/.themes
cp ~/working_folder/.scripts/xfce/.icons/* ~/.icons

sudo ln -s ~/working_folder/.scripts/shortcut-helper/shelp.py /usr/bin/s 
