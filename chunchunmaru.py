import common, utils, drawer
import argparse

def build_res_pack(ctx: common.McContext) -> None:
    # ===== process ores =====
    # overworld
    utils.border_ore_block(ctx, 'coal_ore', '#2e2e2e')
    utils.border_ore_block(ctx, 'copper_ore', '#a65947')
    utils.border_ore_block(ctx, 'diamond_ore', '#1ed0d6')
    utils.border_ore_block(ctx, 'emerald_ore', '#17c544')
    utils.border_ore_block(ctx, 'gold_ore', '#fcee4b')
    utils.border_ore_block(ctx, 'iron_ore', '#d8af93')
    utils.border_ore_block(ctx, 'lapis_ore', '#446fdc')
    utils.border_ore_block(ctx, 'redstone_ore', '#ff0000')
    # nether
    drawer.border_block_texture(ctx, 'nether_gold_ore', '#fcee4b')
    drawer.border_block_texture(ctx, 'nether_quartz_ore', '#d4caba')
    # nether ancient debris need colorful border
    drawer.colorful_border_block_texture(ctx, 'ancient_debris_side')
    drawer.colorful_border_block_texture(ctx, 'ancient_debris_top')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ChunChunMaru',
        description='My Minecraft texture package generator.'
    )
    parser.add_argument('-i', '--input', required=True, action='store', dest='input_path')
    parser.add_argument('-o', '--output', required=True, action='store', dest='output_path')
    parser.add_argument('-m', '--mc-ver', required=True, type=int, action='store', dest='mc_ver')
    args = parser.parse_args()

    ctx: common.McContext = common.McContext(
        args.input_path,
        args.output_path,
        args.mc_ver
    )
    build_res_pack(ctx)
