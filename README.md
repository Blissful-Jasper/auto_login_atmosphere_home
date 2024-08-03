# 自动化任务脚本

此项目包含几个自动化任务脚本，用于自动登录气象家园、下载葵花8号卫星轨道数据、爬取中国天气网雷达拼图图片以及自动登录河海大学校园网。脚本结合Linux的crontab任务进行定时执行。

## auto_login_air.py

- 自动登录气象家园并访问好友空间

## auto_down_hiw8.py

- 下载葵花8号卫星的轨道数据
  
## auto_down_radar.py

- 爬取中国天气网雷达拼图的png图片
  
## auto_login_hohai.py

- 自动登录河海大学校园网

# 环境设置
在运行这些脚本之前，请确保已安装必要的Python依赖包并配置好虚拟环境。可以使用Conda创建和管理虚拟环境。

## 创建并激活虚拟环境
conda create -n wrfpy38 python=3.8
conda activate wrfpy38

## 安装必要的依赖包
pip install requests beauti
fulsoup4 selenium

# 定时任务设置

使用Linux的crontab工具来定时执行这些Python脚本。以下是一个示例crontab配置文件，定期执行上述脚本。

```bash
DISPLAY=:0
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
SHELL=/usr/bin/bash


*/5  * * * *      /Users/xpji/.conda/envs/wrfpy38/bin/python "/DatadiskExt/xpji/down_hiw8.py"  >> /DatadiskExt/xpji/Datapool/get_hiw8_data.log 2>&1 &

*/10  * * * *      /Users/xpji/.conda/envs/wrfpy38/bin/python "/Users/xpji/work_for_AI_support/down_radar.py" >> /DatadiskExt/get_radar.log 2>&1 &

*/60  * * * *      /Users/xpji/.conda/envs/wrfpy38/bin/python "/DatadiskExt/xpji/auto_login_air.py" >> /Users/xpji/login_atmos.log 2>&1 &

```
# 使用说明

- 将Python脚本放置在相应的目录中。
- 确保脚本的可执行权限：chmod +x script_name.py
- 编辑crontab文件：crontab -e
- 添加上述crontab配置。
- 保存并退出编辑器。

# 免责申明

本项目中的自动化脚本及相关代码仅供学习和研究使用。使用本项目代码的用户应遵守相关法律法规及目标网站的使用条款。

## 使用者责任

合法性：用户在使用本项目时，应确保其行为符合所在国家或地区的法律法规，以及目标网站的使用条款和隐私政策。用户需自行承担因违反法律法规或网站条款而产生的任何责任。
权限：用户在访问和操作目标网站时，应确保拥有相应的权限和授权，不得进行任何未经授权的访问或操作。

## 项目开发者责任

无担保：本项目及其代码按“原样”提供，不附带任何明示或暗示的担保，包括但不限于适销性、特定用途的适用性或无侵权的暗示担保。在任何情况下，项目开发者均不对因使用本项目代码而引起的任何损害或损失负责。
代码修改：用户可根据自身需求修改和扩展本项目代码，但修改后的代码引起的任何问题与项目开发者无关。

## 风险声明

使用本项目代码存在一定风险，包括但不限于数据丢失、账号封禁等。用户应充分了解并接受使用本项目代码可能带来的所有风险。

## 终止使用

如果用户不同意本免责声明中的任何条款，应立即停止使用本项目代码。继续使用即表示用户接受并同意本免责声明的所有条款。
通过使用本项目中的代码，即表示您已阅读、理解并同意以上所有条款。
