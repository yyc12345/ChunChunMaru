import modifier, common
import typing

def _iterate_copper_type() -> typing.Iterator[str]:
    for waxed in ('', 'waxed_'):
        for oxidezed_level in ('', 'exposed_', 'weathered_', 'oxidized_'):
            yield waxed + oxidezed_level + 'copper'

def proc_ore(ctx: common.McContext) -> None:
    # overworld
    modifier.common_ore(ctx, 'coal_ore', '#2e2e2e')
    modifier.common_ore(ctx, 'copper_ore', '#a65947')
    modifier.common_ore(ctx, 'diamond_ore', '#1ed0d6')
    modifier.common_ore(ctx, 'emerald_ore', '#17c544')
    modifier.common_ore(ctx, 'gold_ore', '#fcee4b')
    modifier.common_ore(ctx, 'iron_ore', '#d8af93')
    modifier.common_ore(ctx, 'lapis_ore', '#446fdc')
    modifier.common_ore(ctx, 'redstone_ore', '#ff0000')
    # nether
    modifier.border_block(ctx, 'gilded_blackstone', '#a5650e')
    modifier.border_block(ctx, 'nether_gold_ore', '#fcee4b')
    modifier.border_block(ctx, 'nether_quartz_ore', '#d4caba')
    # nether ancient debris need colorful border
    modifier.shiny_border_block(ctx, 'ancient_debris_side')
    modifier.shiny_border_block(ctx, 'ancient_debris_top')
    # raw ore block
    modifier.border_block(ctx, 'raw_copper_block', '#a65947')
    modifier.border_block(ctx, 'raw_gold_block', '#fcee4b')
    modifier.border_block(ctx, 'raw_iron_block', '#d8af93')
    # ore block
    # only coal block need border, other blocks is easy to distinguish
    modifier.border_block(ctx, 'coal_block', '#292727')
    # amethyst (紫水晶)
    modifier.border_block(ctx, 'amethyst_block', '#5d3a9a')
    modifier.border_block(ctx, 'budding_amethyst', '#be8e59')

def proc_redstone(ctx: common.McContext) -> None:
    # door showcase
    # todo: add copper door when updating to 1.20.3
    door_types: tuple[str, ...] = (
        'oak', 'spruce', 'birch', 'jungle', 'acacia', 'dark_oak', 'mangrove', 'cherry',
        'bamboo', 
        'crimson', 'warped',
        'iron',
    )
    for door_type in door_types:
        modifier.door(ctx, door_type + '_door')

def proc_tree(ctx: common.McContext) -> None:
    # ===== tree blocks =====
    # add border for log (原木), stripped_log (去皮原木), wood (木头), stripped_wood (去皮木头), planks (木板)
    # because wood use the same texture with log, so these proc can be merged.
    # color_tuple = tuple(log_color, log_top_color, stripped_log_color, stripped_log_top_color, planks_color)
    modifier.tree(ctx, 'oak', ('#4c3d26', None, '#846a3a', None, '#67502c'), modifier.TreeType.Overworld)
    modifier.tree(ctx, 'spruce', ('#2e1c0a', None, '#544525', None, '#553a1f'), modifier.TreeType.Overworld)
    modifier.tree(ctx, 'birch', ('#aea6a4', None, '#9d8754', None, '#907e58'), modifier.TreeType.Overworld)
    modifier.tree(ctx, 'jungle', ('#403612', None, '#977c45', None, '#68462f'), modifier.TreeType.Overworld)
    modifier.tree(ctx, 'acacia', ('#5b554d', None, '#8f4c2a', None, '#7b4024'), modifier.TreeType.Overworld)
    modifier.tree(ctx, 'dark_oak', ('#584428', '#53381a', '#32281a', None, '#291a0c'), modifier.TreeType.Overworld)
    modifier.tree(ctx, 'mangrove', ('#3c2f23', '#3c2f23', '#632122', None, '#5d1c1e'), modifier.TreeType.Overworld)
    modifier.tree(ctx, 'cherry', ('#1b0f16', None, '#c07974', None, '#cd8580'), modifier.TreeType.Overworld)
    modifier.tree(ctx, 'bamboo', ('#5a6627', '#505c23', '#615526', '#615526', '#615526'), modifier.TreeType.Bamboo)
    modifier.tree(ctx, 'crimson', ('#7b0000', '#442131', '#6a2640', None, '#3f1e2d'), modifier.TreeType.Nether)
    modifier.tree(ctx, 'warped', ('#16615b', '#442131', '#2e8578', None, '#113835'), modifier.TreeType.Nether)

    # ===== tree leaves =====
    # prepare leaves first
    modifier.prepare_tree_leaves(ctx)
    # process tree leaves on by one (there is no bamboo leaves)
    modifier.tree_leaves(ctx, 'oak', '#686468')
    modifier.tree_leaves(ctx, 'spruce', None)
    modifier.tree_leaves(ctx, 'birch', '#706d70')
    modifier.tree_leaves(ctx, 'jungle', None)
    modifier.tree_leaves(ctx, 'acacia', None)
    modifier.tree_leaves(ctx, 'dark_oak', None)
    modifier.tree_leaves(ctx, 'mangrove', None)
    modifier.tree_leaves(ctx, 'cherry', '#738726')

    # there is no bamboo leaves, so no need to process it

    # there is a extra leaves type: azalea leaves (杜鹃), flowering azalea leaves (盛开的杜鹃)
    modifier.tree_leaves(ctx, 'azalea', None)
    modifier.tree_leaves(ctx, 'flowering_azalea', None)

    # nether leaves (nether wart + shroomlight) do not have levels, so we just border it.
    modifier.border_block(ctx, 'nether_wart_block', '#3e0808')
    modifier.border_block(ctx, 'warped_wart_block', '#13585d')
    modifier.border_block(ctx, 'shroomlight', '#b62f09')

def proc_food(ctx: common.McContext) -> None:
    # pumpkin, jack o latern, watermelon
    modifier.border_block(ctx, 'melon_side', '#3e711d')
    # hay
    modifier.border_block(ctx, 'hay_block_side', '#78631c')
    modifier.border_block(ctx, 'hay_block_top', '#78631c')
    # mushroom
    modifier.border_block(ctx, 'brown_mushroom_block', '#725745')
    modifier.border_block(ctx, 'red_mushroom_block', '#a41b1a')
    modifier.border_block(ctx, 'mushroom_stem', '#ada797')

    # bee related
    # honeycomb (蜜脾块)
    modifier.border_block(ctx, 'honeycomb_block', '#b86309')

def proc_colorful(ctx: common.McContext) -> None:
    ## color_tuple = (
    #   white, orange, magenta, light_blue, 
    #   yellow, lime, pink, gray, 
    #   light_gray, cyan, purple, blue, 
    #   brown, green, red, black
    # )

    # all concrete varients
    modifier.colorful_block(ctx, 'concrete', (
        '#dadedf', '#e46f00', '#b544ac', '#3093cc',
        '#f5c02b', '#68af21', '#da729a', '#424549', 
        '#828278', '#1c7f8f', '#6d28a3', '#383a99', 
        '#6d492b', '#4f612a', '#992f2f', '#121621'
    ))

    # concrete powder do not have border

    # all terracotta varients and no color terracotta
    modifier.border_block(ctx, 'terracotta', '#87533b')
    modifier.colorful_block(ctx, 'terracotta', (
        '#ba9d90', '#8c471f', '#875062', '#655f79',
        '#a1721d', '#57632a', '#8c4344', '#2c201b', 
        '#735951', '#474c4c', '#623a47', '#372c45', 
        '#38241a', '#3d4320', '#80372b', '#190f0b'
    ))

    # glazed terracottta do not have border

    # only white wool for wool
    modifier.colorful_block(ctx, 'wool', (
        '#bec4c5', None, None, None,
        None, None, None, None,
        None, None, None, None,
        None, None, None, None
    ))

def proc_overworld(ctx: common.McContext) -> None:
    # ===== overworld block =====
    # stone and its variants
    # stone, cobblestone
    modifier.border_block(ctx, 'stone', '#5d5c5c')
    modifier.border_block(ctx, 'cobblestone', '#4e4d4d')
    # deepslate, cobbled deepslate, deepslate tiles, cracked deepslate tiles
    modifier.border_block(ctx, 'deepslate', '#202028')
    modifier.border_block(ctx, 'deepslate_top', '#202028')
    modifier.border_block(ctx, 'cobbled_deepslate', '#2b2b30')
    modifier.border_block(ctx, 'deepslate_tiles', '#1e1c1c')
    modifier.border_block(ctx, 'cracked_deepslate_tiles', '#242424')
    # overworld stone variants
    # diorite (闪长岩，白色的), andesite (安山岩，灰色的), granite (花岗岩，棕色的)
    # tuff (凝灰岩，新加的灰色的), calcite (方解石，新加的白色的)
    modifier.border_block(ctx, 'diorite', '#757373')
    modifier.border_block(ctx, 'andesite', '#514f4f')
    modifier.border_block(ctx, 'granite', '#5f4034')
    modifier.border_block(ctx, 'tuff', '#4d5046')
    modifier.border_block(ctx, 'calcite', '#b3b3b3')
    # infested stone
    modifier.infested_stone(ctx, 'stone', '#7f4e4e', False)
    modifier.infested_stone(ctx, 'cobblestone', '#7f4e4e', False)
    modifier.infested_stone(ctx, 'stone_bricks', '#7f4e4e', False)
    modifier.infested_stone(ctx, 'cracked_stone_bricks', '#7f4e4e', False)
    modifier.infested_stone(ctx, 'mossy_stone_bricks', '#7f4e4e', False)
    modifier.infested_stone(ctx, 'chiseled_stone_bricks', '#7f4e4e', False)
    modifier.infested_stone(ctx, 'deepslate', '#7f4e4e', True)

    # dirt and its variants
    # dirt
    modifier.border_block(ctx, 'dirt', '#664730')
    # grass block
    modifier.border_block(ctx, 'grass_block_top', '#828282')
    modifier.grass_border_block(ctx, 'grass_block_side', 2, 1, '#75b54b', '#664730', False)
    modifier.grass_border_block(ctx, 'grass_block_side_overlay', 2, 1, '#828282', None, False)
    # dirt variants: coarse dirt (砂土), mycelium (菌丝体), podzol (灰化土), dirt path (土径)
    # these dirt variants is not included because they are not importent: rooted dirt (缠根泥土), farm land (耕地)
    modifier.border_block(ctx, 'coarse_dirt', '#676767')
    modifier.border_block(ctx, 'mycelium_top', '#83757b')
    modifier.grass_border_block(ctx, 'mycelium_side', 4, 3, '#83757b', '#664730', False)
    modifier.border_block(ctx, 'podzol_top', '#7a5428')
    modifier.grass_border_block(ctx, 'podzol_side', 3, 3, '#7a5428', '#664730', False)
    modifier.border_block(ctx, 'dirt_path_top', '#775f33')
    modifier.grass_border_block(ctx, 'dirt_path_side', 2, 1, '#775f33', '#664730', True)
    # grass block, myselium block with snow
    modifier.grass_border_block(ctx, 'grass_block_snow', 4, 4, '#b5e1e1', '#664730', False)
    # clay
    modifier.border_block(ctx, 'clay', '#8a919d')

    # mud and its variants
    # mud
    modifier.border_block(ctx, 'mud', '#252129')
    # muddy mangrove
    modifier.border_block(ctx, 'muddy_mangrove_roots_top', '#3b3334')
    modifier.border_block(ctx, 'muddy_mangrove_roots_side', '#363239')
    # packed mud
    modifier.border_block(ctx, 'packed_mud', '#7f5d4c')

    # sand and its varients
    # sand, sandstone
    modifier.border_block(ctx, 'sand', '#cab57d')
    modifier.border_block(ctx, 'sandstone', '#9a8049')
    modifier.border_block(ctx, 'sandstone_top', '#9a8049')
    modifier.border_block(ctx, 'sandstone_bottom', '#9a8049')
    # red sand, red sandstone
    modifier.border_block(ctx, 'red_sand', '#61300a')
    modifier.border_block(ctx, 'red_sandstone', '#61300a')
    modifier.border_block(ctx, 'red_sandstone_top', '#61300a')
    modifier.border_block(ctx, 'red_sandstone_bottom', '#61300a')
    # gravel
    modifier.border_block(ctx, 'gravel', '#5d5555')
    # sus sand and sus gravel
    # support sus gravel since 1.20 (15)
    for i in range(4):
        modifier.border_block(ctx, f'suspicious_sand_{i}', '#ebe17f')
    if ctx.get_mc_ver() >= 15:
        for i in range(4):
            modifier.border_block(ctx, f'suspicious_gravel_{i}', '#7d7575')

    # obsidian and its variants
    modifier.border_block(ctx, 'obsidian', '#3b2754')
    modifier.border_block(ctx, 'crying_obsidian', '#3b2754')

    # ice, packed ice, blue ice, snow
    # 3 types ice
    modifier.border_block(ctx, 'ice', '#7daafb')
    modifier.border_block(ctx, 'packed_ice', '#6794e8')
    modifier.border_block(ctx, 'blue_ice', '#4c8ffb')
    # the ice created by enchantment frozen walker (4 levels)
    for i in range(4):
        modifier.border_block(ctx, f'frosted_ice_{i}', '#7dabfa')
    # snow & snow block
    modifier.border_block(ctx, 'snow', '#b5e1e1')
    # powder snow (细雪)
    # it need to add specific pattern
    modifier.snowflake_overlay_block(ctx, 'powder_snow')

    # ocean block
    modifier.border_block(ctx, 'prismarine', '#386e5a')
    modifier.border_block(ctx, 'prismarine_bricks', '#344f48')
    modifier.border_block(ctx, 'dark_prismarine', '#162720')

    # cave update blocks
    # dripstone
    modifier.border_block(ctx, 'dripstone_block', '#694f4a')
    # moss (苔藓), moss carpet (use the same texture as block)
    modifier.border_block(ctx, 'moss_block', '#384926')
    # azalea (杜鹃花从), flowering azalea (盛开的杜鹃花从)
    modifier.border_block(ctx, 'azalea_top', '#50692c')
    modifier.grass_border_block(ctx, 'azalea_side', 7, 8, '#50692c', None, False)
    modifier.border_block(ctx, 'flowering_azalea_top', '#50692c')
    modifier.grass_border_block(ctx, 'flowering_azalea_side', 7, 8, '#50692c', None, False)
    
def proc_nether(ctx: common.McContext) -> None:
    modifier.border_block(ctx, 'glowstone', '#573418')
    modifier.border_block(ctx, 'magma', '#421616')
    modifier.border_block(ctx, 'soul_sand', '#3a2d25')
    modifier.border_block(ctx, 'soul_soil', '#3b2e25')
    modifier.border_block(ctx, 'blackstone', '#3c3947')
    modifier.border_block(ctx, 'blackstone_top', '#3c3947')

def proc_end(ctx: common.McContext) -> None:
    modifier.border_block(ctx, 'end_stone', '#aba579')
    modifier.border_block(ctx, 'end_stone_bricks', '#aba579')
    # todo...
