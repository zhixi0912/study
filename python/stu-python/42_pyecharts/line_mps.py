# 安装pyecharts  pip install pyecharts
#
# https://pan.baidu.com/s/1KCKkV13ymltq9CMXE3qxJA?pwd=1234
# 提取码 ：1234

from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
line = Line()

line.add_xaxis(["中国联通", "中国移动", "中国电信"])
line.add_yaxis("月租价格", [20, 30, 80])
line.set_global_opts(
    title_opts=TitleOpts(title="月租价格展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
line.render()