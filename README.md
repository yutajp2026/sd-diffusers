# Stable Diffusion With Diffusers
画像生成AIであるStable Diffusionを簡単に使えるようにしたアプリ。

# 特徴
- Gradioを使ったWebUI(Windowsのみ自動でブラウザを開く)
- ワンクリックで実行
- txt2imgとimg2img
- 日本語プロンプト対応
- 推論ステップ数の指定
- diffusersを使用
- デバイスを自動選択(CPU、Nvidia GPU)
- Stable Diffusion 1.5を自動ダウンロード
- モデル変更(詳細は[モデルを探そう](https://github.com/yutajp2026/sd-diffusers#モデルを探そう))

# インストール
## Windows
[**Releases**](https://github.com/yutajp2026/sd-diffusers-jp/releases)にインストーラを公開

- ℹ️アップデートも最新版インストーラをダウンロードして開くことで行えます。
- ⚠️アンインストール時、ディレクトリ自体は完全には削除されないので、手動で削除してください。
## Linux
1. 下記のコマンドでPythonとgitをインストール
```bash
# Debian系(Ubuntuなど)
sudo apt update
sudo apt install python3 python3-pip python3-venv git
```
```bash
# Red Hat系(Oracle Linuxなど)
sudo dnf install python3 python3-pip python3-venv git
```
```bash
# Arch系
sudo pacman install python3 python3-pip python3-venv git
```
```bash
# SUSE系
sudo zypper install python3 python3-pip python3-venv git
```
2. `git clone https://github.com/yutajp2026/sd-diffusers-jp.git`でこのリポジトリをクローン
3. `cd sd-diffusers-jp`でスクリプトディレクトリに移動
4. `bash sdwebui.sh`で実行 ⚠️linuxの場合は自動でブラウザを開きません。
5. `git pull`でアップデート

# Stable Diffusionに興味を持った方へ
### モデルを探そう
本ソフトでは、safetensorsやckptを好きな場所にダウンロードして、ファイルパスを入力するとモデルを変更できます。ただし、チェックポイントのみ対応しています。

以下リンクにはたくさんのDiffusion(拡散)モデルが載っています。
- https://civitai.com/models
- https://huggingface.co/models?pipeline_tag=text-to-image&library=safetensors&sort=trending

### おすすめソフト
[recommend.md](https://github.com/yutajp2026/sd-diffusers-jp/blob/main/recommend.md)に記載したアプリには、様々な機能が備わっています。本ソフトでダウンロードしたモデルを使う方法なども載せてあります。
