import common, utils
import argparse

def build_res_pack(ctx: common.McContext) -> None:
    utils.proc_ore(ctx)
    utils.proc_redstone(ctx)
    utils.proc_tree(ctx)

    utils.proc_overworld(ctx)
    utils.proc_nether(ctx)
    utils.proc_end(ctx)

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
