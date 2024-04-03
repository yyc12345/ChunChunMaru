import drawer, modifier, common
import typing

def _iterate_copper_type() -> typing.Iterator[str]:
    for waxed in ('', 'waxed_'):
        for oxidezed_level in ('', 'exposed_', 'weathered_', 'oxidized_'):
            yield waxed + oxidezed_level + 'copper'

def proc_ore(ctx: common.McContext) -> None:
    # overworld
    modifier.overworld_ore(ctx, 'coal_ore', '#2e2e2e')
    modifier.overworld_ore(ctx, 'copper_ore', '#a65947')
    modifier.overworld_ore(ctx, 'diamond_ore', '#1ed0d6')
    modifier.overworld_ore(ctx, 'emerald_ore', '#17c544')
    modifier.overworld_ore(ctx, 'gold_ore', '#fcee4b')
    modifier.overworld_ore(ctx, 'iron_ore', '#d8af93')
    modifier.overworld_ore(ctx, 'lapis_ore', '#446fdc')
    modifier.overworld_ore(ctx, 'redstone_ore', '#ff0000')
    # nether
    drawer.border_block_texture(ctx, 'gilded_blackstone', '#a5650e')
    drawer.border_block_texture(ctx, 'nether_gold_ore', '#fcee4b')
    drawer.border_block_texture(ctx, 'nether_quartz_ore', '#d4caba')
    # nether ancient debris need colorful border
    drawer.colorful_border_block_texture(ctx, 'ancient_debris_side')
    drawer.colorful_border_block_texture(ctx, 'ancient_debris_top')
    # raw ore block
    drawer.border_block_texture(ctx, 'raw_copper_block', '#a65947')
    drawer.border_block_texture(ctx, 'raw_gold_block', '#fcee4b')
    drawer.border_block_texture(ctx, 'raw_iron_block', '#d8af93')
    # ore block
    # only coal block need border, other blocks is easy to distinguish
    drawer.border_block_texture(ctx, 'coal_block', '#292727')
    # amethyst
    drawer.border_block_texture(ctx, 'amethyst_block', '#5d3a9a')
    drawer.border_block_texture(ctx, 'budding_amethyst', '#be8e59')

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
        modifier.redstone_door(ctx, door_type + '_door')

def proc_common(ctx: common.McContext) -> None:
    # tree blocks
    # add border for log (原木), stripped_log (去皮原木), wood (木头), stripped_wood (去皮木头), planks (木板)
    # because wood use the same texture with log, so these proc can be merged.
    # color_tuple = tuple(log_color, log_top_color, stripped_log_color, stripped_log_top_color, planks_color)
    modifier.tree_block(ctx, 'oak', ('#382b18', None, '#846a3a', None, '#67502c'), modifier.TreeType.Overworld)
    modifier.tree_block(ctx, 'spruce', ('#553a1f', None, '#544525', None, '#553a1f'), modifier.TreeType.Overworld)
    modifier.tree_block(ctx, 'birch', ('#aea6a4', None, '#9d8754', None, '#907e58'), modifier.TreeType.Overworld)
    modifier.tree_block(ctx, 'jungle', ('#635820', None, '#977c45', None, '#68462f'), modifier.TreeType.Overworld)
    modifier.tree_block(ctx, 'acacia', ('#5b554d', None, '#8f4c2a', None, '#7b4024'), modifier.TreeType.Overworld)
    modifier.tree_block(ctx, 'dark_oak', ('#584428', '#53381a', '#32281a', None, '#291a0c'), modifier.TreeType.Overworld)
    modifier.tree_block(ctx, 'mangrove', ('#3c2f23', '#3c2f23', '#632122', None, '#5d1c1e'), modifier.TreeType.Overworld)
    modifier.tree_block(ctx, 'cherry', ('#1b0f16', None, '#c07974', None, '#cd8580'), modifier.TreeType.Overworld)
    modifier.tree_block(ctx, 'bamboo', ('#5a6627', '#505c23', '#615526', '#615526', '#615526'), modifier.TreeType.Bamboo)
    modifier.tree_block(ctx, 'crimson', ('#7b0000', '#442131', '#6a2640', None, '#3f1e2d'), modifier.TreeType.Nether)
    modifier.tree_block(ctx, 'warped', ('#16615b', '#442131', '#2e8578', None, '#113835'), modifier.TreeType.Nether)

    # tree leaves
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
    # there is a extra leaves type: azalea_leaves (杜鹃)
    modifier.tree_leaves(ctx, 'azalea', None)
    # nether leaves (nether wart + shroomlight) do not have levels, so we just border it.
    drawer.border_block_texture(ctx, 'nether_wart_block', '#3e0808')
    drawer.border_block_texture(ctx, 'warped_wart_block', '#13585d')
    drawer.border_block_texture(ctx, 'shroomlight', '#b62f09')

    # overworld block
    # stone, cobblestone, deepslate, cobbled deepslate
    drawer.border_block_texture(ctx, 'stone', '#5d5c5c')
    drawer.border_block_texture(ctx, 'cobblestone', '#4e4d4d')
    drawer.border_block_texture(ctx, 'deepslate', '#202028')
    drawer.border_block_texture(ctx, 'cobbled_deepslate', '#2b2b30')
    # todo...
    # sand, gravel, dirt, grass
    drawer.border_block_texture(ctx, 'sand', '#cab57d')
    drawer.border_block_texture(ctx, 'clay', '#8a919d')
    drawer.border_block_texture(ctx, 'grass_block_top', '#828282')
    drawer.border_block_texture(ctx, 'dirt', '#664730')
    drawer.border_block_texture(ctx, 'dirt_path_top', '#775f33')
    drawer.border_block_texture(ctx, 'coarse_dirt', '#676767')
    drawer.border_block_texture(ctx, 'gravel', '#5d5555')
    # todo...
    # overworld stone variants
    drawer.border_block_texture(ctx, 'diorite', '#757373')
    drawer.border_block_texture(ctx, 'andesite', '#514f4f')
    drawer.border_block_texture(ctx, 'granite', '#5f4034')
    drawer.border_block_texture(ctx, 'tuff', '#4d5046')
    drawer.border_block_texture(ctx, 'calcite', '#b3b3b3')
    # obsidian
    drawer.border_block_texture(ctx, 'obsidian', '#3b2754')

    # ice, packed ice, blue ice, snow
    # 3 types ice
    drawer.border_block_texture(ctx, 'ice', '#7daafb')
    drawer.border_block_texture(ctx, 'packed_ice', '#6794e8')
    drawer.border_block_texture(ctx, 'blue_ice', '#4c8ffb')
    # the ice created by enchantment frozen walker (4 levels)
    for i in range(4):
        drawer.border_block_texture(ctx, f'frosted_ice_{i}', '#7dabfa')
    # snow & snow block
    drawer.border_block_texture(ctx, 'snow', '#b5e1e1')
    # powder snow (细雪)
    # it need to add specific pattern
    drawer.snowflake_overlay_block_texture(ctx, 'powder_snow')

    # moss, azalea
    drawer.border_block_texture(ctx, 'moss_block', '#384926')
    drawer.border_block_texture(ctx, 'azalea_top', '#50692c')
    


    # nether block
    drawer.border_block_texture(ctx, 'magma', '#421616')
    drawer.border_block_texture(ctx, 'soul_sand', '#3a2d25')
    drawer.border_block_texture(ctx, 'soul_soil', '#3b2e25')
    drawer.border_block_texture(ctx, 'blackstone', '#3c3947')
    drawer.border_block_texture(ctx, 'blackstone_top', '#3c3947')
    # todo...

    # end block
    drawer.border_block_texture(ctx, 'end_stone', '#aba579')
    # todo...

