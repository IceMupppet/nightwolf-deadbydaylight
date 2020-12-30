import os
import shutil

mapping_list = {
    "themes/nightwolf/Perks/iconPerks_headOn.png": "../DeadByDaylight/Content/UI/Icons/Perks/Mali/iconPerks_headOn.png",
    "themes/nightwolf/Perks/iconPerks_quickAndQuiet.png": "../DeadByDaylight/Content/UI/Icons/Perks/iconPerks_quickAndQuiet.png",
    "themes/nightwolf/Perks/iconPerks_leftBehind.png": "../DeadByDaylight/Content/UI/Icons/Perks/L4D/iconPerks_leftBehind.png",
    "themes/nightwolf/Perks/iconPerks_unbreakable.png": "../DeadByDaylight/Content/UI/Icons/Perks/L4D/iconPerks_unbreakable.png",
    "themes/nightwolf/Perks/iconPerks_selfCare.png": "../DeadByDaylight/Content/UI/Icons/Perks/iconPerks_selfCare.png"
}

root_path = "E:/SteamLibrary/steamapps/common/Dead by Daylight/deadbydaylight-nightwolf"
destination = "E:/SteamLibrary/steamapps/common/Dead by Daylight/deadbydaylight-nightwolf"

for file in mapping_list:
    file_path = "{}/{}".format(root_path, file)
    dest_path = "{}/{}".format(root_path, mapping_list[file])
    shutil.copy(file_path, dest_path)