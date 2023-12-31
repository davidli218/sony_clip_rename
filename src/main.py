"""
@@Intro:
    适用于索尼微单机型的素材自动重命名脚本。
    注意：重命名功能依赖于跟随视频生成的XML文件。

@@Naming Rule:
    @Brief:
        %y%m%d_%H%M%S-Resolution@FPS-ColorPrimaries-TransferFunc-Model(-Note).MP4

    @Details:
        * %y              |  两位数的年份表示(00-99)
        * %m              |  月份(01-12)
        * %d              |  月内中的一天(0-31)
        * %H              |  24小时制小时数(0-23)
        * %M              |  分钟数(00-59)
        * %S              |  秒(00-59)

        * Resolution      |  分辨率
        * FPS             |  帧率
        * ColorPrimaries  |  原色
        * TransferFunc    |  传递函数
        * Model           |  拍摄机型
        * (Note)          |  可选备注

    @Example:
        220504_125850-4K@29.97-Rec709-xvYCC-SX107-乌鸦洗澡.MP4
"""

from rename_utils import RenameUtils

if __name__ == '__main__':
    work_dir = r'Input working directory here'

    RenameUtils.batch_rename(
        RenameUtils.video_pairs_gen(work_dir), dry_run=False
    )
