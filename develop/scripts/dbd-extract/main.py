import os
import shutil

mapping_list = {
    "nightwolf/content/iconPerks_headOn.png": "../DeadByDaylight/Content/UI/Icons/Perks/Mali/iconPerks_headOn.png",
    "nightwolf/content/iconPerks_quickAndQuiet.png": "../DeadByDaylight/Content/UI/Icons/Perks/iconPerks_quickAndQuiet.png",
    "nightwolf/content/iconPerks_leftBehind.png": "../DeadByDaylight/Content/UI/Icons/Perks/L4D/iconPerks_leftBehind.png",
    "nightwolf/content/iconPerks_selfCare.png": "../DeadByDaylight/Content/UI/Icons/Perks/iconPerks_selfCare.png"
}

root_path = "E:/SteamLibrary/steamapps/common/Dead by Daylight/deadbydaylight-nightwolf"
destination = "E:/SteamLibrary/steamapps/common/Dead by Daylight/deadbydaylight-nightwolf"

for file in mapping_list:
    file_path = "{}/{}".format(root_path, file)
    dest_path = "{}/{}".format(root_path, mapping_list[file])
    shutil.copy(file_path, dest_path)