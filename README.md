# ChunChunMaru

ChunChunMaru (ちゅんちゅん丸/啾啾丸) is a Minecraft resource pack project.

WIP.

## Why?

Since a few years ago, Mojang has been updating resource packs more and more frequently, and the authors of the packs need to redraw or rename the textures when updating. This is a totally boring and useless task that takes a lot of time. I don't want to waste that time on these things. So I created this project to keep the contents of my favorite resource packs up to date.

## Principle

This project creates some generic methods for dynamically creating resource packages from vanilla resource packages. When Mojang updates a resource package, the only thing that needs to be done is to fix some naming issues and then re-run this program to rebuild the entire package. This project is based on a programmer's mindset, not an artist's mindset, because I am a programmer. This project prefers to describe each texture modification in code rather than a bunch of Photoshop files. So obviously, this project may not be understood by most resource pack creators.

## Style

This resource pack generator is for my tastes. I am a redstone player, not a builder or PVP player. Therefore, the focus of this project is to show redstone status and facilitate building redstone machines.

This resource pack has:

### Ore Blocks

* Ore
  - Add significant border for coal ore, copper ore, diamond ore, emerald ore, gold ore, iron ore, lapis ore, redstone ore (including their deepslate variants).
* Nether ore
  - Add significant border for gilded blackstone, nether gold ore, nether quartz ore.
  - Add VERY significant, animated shiny border for ancient debris.
* Raw ore blocks
  - Add significant border for raw copper block, raw gold block, raw iron block (they may appear in vein).
* Mineral blocks
  - Add border for coal block (other mineral blocks already have border).
* Amethyst
  - Add border for amethyst block.
  - Add warning border for budding amethyst (to tell player do not break it).

### Tree Blocks

* Add decay level and persistent status display for all leaves except nether tree leaves because they are not real leaves (they can not decay).
* Add border for specific leaves, log, stripped log, wood, stripped wood, planks. Following table describe which one were added.

|Type|Log (±Stripped) / Wood (±Stripped)|Planks|Leaves|
|:---|:---|:---|:---|
|oak|√|√|√|
|spruce|√|√|×|
|birch|√|√|√|
|jungle|√|√|×|
|acacia|√|√|×|
|dark oak|√|√|×|
|mangrove|√|√|×|
|cherry|√|√|√|
|bamboo|√|√|N/A|
|crimson|√|√|√|
|warped|√|√|√|
|azalea|N/A|N/A|√|
|flowering azalea|N/A|N/A|√|

### Food Blocks

* Crops Blocks
  - Add border for melon, pumpkin, jack o latern.
  - Add border for hay block.
  - Add border for red mushroom block, brown mushroom block, mushroom stem.
* Bee Blocks
  - Add border for honeycomb block.

### Colorful Blocks

Add border for specific 16 color blocks which are described following.

|Color|Concrete|Concrete Powder|Terracotta|Glazed Terracotta|Wool|
|:---|:---|:---|:---|:---|:---|
|white|√|×|√|×|√|
|orange|√|×|√|×|×|
|mangenta|√|×|√|×|×|
|light blue|√|×|√|×|×|
|yellow|√|×|√|×|×|
|lime|√|×|√|×|×|
|pink|√|×|√|×|×|
|gray|√|×|√|×|×|
|light gray|√|×|√|×|×|
|cyan|√|×|√|×|×|
|purple|√|×|√|×|×|
|blue|√|×|√|×|×|
|brown|√|×|√|×|×|
|green|√|×|√|×|×|
|red|√|×|√|×|×|
|black|√|×|√|×|×|
|no color|N/A|N/A|√|N/A|N/A|

### Overworld Blocks

* Stone-like blocks
  - Add border for stone: stone, cobblestone, deepslate, cobbled deepslate, deepslate tiles, cracked deepslate tiles.
  - Add border for stone variants: diorite, andesite, granite, tuff, calcite.
  - Add significant for infested stone: infested stone, infested cobblestone, infested stone bricks, infested cracked stone bricks, infested mossy stone bricks, infested chiseled stone bricks, infested deepslate (to tell player do not dig them).
* Dirt-like blocks
  - Add border for dirt, grass block, mycelium, podzol, dirt path, clay.
  - Add significant border for coarse dirt.
* Mud-like blocks
  - Add border for mud, muddy mangrove roots, packed mud.
* Sand-like blocks
  - Add border for sand, sandstone (all variants), red sand, red sandstone (all variants), gravel.
  - Add significant border for suspicious sand, suspicious gravel.
* Obsidian0like blocks
  - Add border for obsidian, crying obsidian.
* Snow-like blocks
  - Add border for ice, packed ice, blue ice, frozed ice, snow, snow block.
  - Add sigificant snowflake pattern for powder snow.
* Cave update blocks:
  - Add border for moss, moss carpet, azalea, flowering azalea.
  - Add border for dripstone.
* Ocean blocks:
  - Add border for prismarine, prismarine bricks, dark prismarine.

### Nether Blocks

* Stone-like blocks

### End Blocks

* Add border for end stone, end stone bricks.

## Dependencies

* Python (Python 3.10 suggested)
* PIL package
* Minecraft font (may need to be downloaded from other sites)

## Usage

1. Get vanilla resource pack first. You can decompress the Minecraft JAR file into a empty folder to fetch it (you also can only decompress `assets` located in JAR to get the same effect because this program do not read anything in Java part).
1. Create an empty folder for generated resource pack. I suggest you create a folder in `.minecraft/resourcepacks` so that you can test it dynamically.
1. Open terminal in the folder where `chunchunmaru.py` located.
1. Execute `python3 chunchunmaru.py -i [input_path] -o [output_path] -m [mc_ver]`
    * `[input_path]` is replaced to your vanilla resource pack folder where you can find `assets` folder.
    * `[output_path]` is replaced to your generated resource pack folder. If you create a folder named `ChunChunMaru` in the folder we suggested in step 2, this argument should be `.minecraft/resourcepacks/ChunChunMaru`.
    * `[mc_ver]` is replaced to your expected resource pack version (not Minecraft version). For 1.19.4 instance, you should pass 13.
1. Everything are done. You can open game to check out the result or compress the result as a zip file if you want to move it into another place.

## Credit and License

This project combines the resource pack designs of 2 Minecraft players: Xe\_Kr's Redstone Display (Xe\_Kr红石显示) and hsds' HuYanDaBuWan (hsds护眼大补丸).

These 2 resource packs have their own licenses. So please note this project is **NOT** a **FREE** project. Redistributing the resource pack generated by this project is **ILLEGAL** and may be prosecuted by Xe\_Kr or hsds. I also will not publish any pre-built binary resource packs. This project do not take any warranty of any kind. In no event shall I be liable for any claim, damages or otherliability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

This program is for my personal use and uploading only for the purpose of sharing my ideas for implementation.
