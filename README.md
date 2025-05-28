# 困在盗梦空间(Inception)中的cursor

花费1个cursor次数，发送n条消息的方法。（尽可能多的）

和我一起冻结cursor请求次数！

## 环境&兼容性

### 操作系统

[ ok ] Windows

[ ok ] Linux

[ ok ] macOS

### 其他

1. 你需要拥有`python3`

2. 你需要拥有系统默认的文件编辑器，这通常自带，对于`arch`发行版，你可能需要安装一个:-)

## 安装

### 1. 退出你的cursor

### 2. 在任意终端执行命令

```
python3 -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/Deng-Xian-Sheng/cursor_inception/refs/heads/main/install.py').read())"
```

## 使用

正常使用cursor agent,当它弹出命令：

![image](https://github.com/user-attachments/assets/5db50054-16d2-43bd-9a92-abf654ca1be6)

请允许执行，然后，它会弹出一个文本编辑器，取决于你的操作系统和.txt的默认打开方式。

具体来说，windows下是记事本、macos和linux下是系统自带的文本编辑器。

然后，**你需要在弹出的文本编辑器中填写你的新消息**，记得`Ctrl + s`保存，然后关闭你的文本编辑器。

然后**你需要在cursor执行命令的地方，按下一个回车**，这是在告诉它：我把消息写完了。

cursor会按照你的新消息继续执行。

如此往复。

**我在gemini-2.5-pro上测试，它工作良好**

## 卸载

打开cursor的设置，删除安装脚本追加的提示词，如图所示：

![image](https://github.com/user-attachments/assets/18773440-19a4-4854-95e1-ab48b72eb56d)

## 开发者附言

1. 这个实现始终，贯彻“不在你的电脑上创建任何文件”的策略，为了打开编辑器获得用户输入产生的临时文件会立即删除。

2. 似乎它不会永远继续，因为即使你能获得最大工具调用次数，由于cursor有一个限制：

> Note: By default, we stop the agent after 25 tool calls. You can resume the conversation.

注意：默认情况下，我们会在 25 次工具调用后停止代理。您可以恢复对话。

所以，你最终会停下来。

“恢复对话”会花费1个cursor次数。
