# Stable Diffusionに興味を持った方へ
これらのアプリには様々な機能が備わっており、本ソフトで使用したモデルを流用できるものもあります。上から順に使いやすいです。
## [InvokeAI](https://invoke.ai/start-here/installation/)
最も使いやすく、本ソフトとのモデルの共有もしやすいです。
### モデル流用
モデルパスに入力
## [SwarmUI](https://swarmui.net/)
事前に必要なものもないので使いやすいです(一部OS)。Windows版はWebUIにもGUIにもなります。
### モデル流用
Models内のStable-diffusionに移動またはコピー
## [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
王道で、アプリの容量が比較的小さく(本ソフトよりは大きい)、WebUI自体は使いやすいです。しかし公式の説明通りにインストールしようとすると必ず詰むので独自にインストール方法を説明します。
### Windowsへのインストール
1. [Python3.10.6](https://www.python.org/downloads/release/python-3106/)をインストール
2. [VC Redist](https://learn.microsoft.com/ja-jp/cpp/windows/latest-supported-vc-redist?view=msvc-170)がない場合はインストール
3. コマンドプロンプトを開き`winget install --id Git.Git -e --source winget`コマンドでgitをインストール
4. `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`コマンドでリポジトリをクローン
5. `webui-user.bat`の内容を下記に変更(remはなくてもよい)
```
@echo off
rem Pythonの初期パス(必要に応じて削除または変更)
rem 他のバージョンのPythonを使わないようにするために記載します。
set PYTHON="C:\Users\%username%\AppData\Local\Programs\Python\Python310\python.exe

rem Nvidia GPUがない場合は"--use-cpu all --precision full --no-half --skip-torch-cuda-test"を代入
set COMMANDLINE_ARGS=

rem 詰み防止のため
set STABLE_DIFFUSION_REPO=https://github.com/w-e-w/stablediffusion.git
set CLIP_PACKAGE=git+https://github.com/openai/CLIP.git

call webui.bat
```
6. `webui-user.bat`(起動ファイル)を実行
### Linuxへのインストール
1. 下記コマンドで依存関係をインストール
```bash
# Debian系(Ubuntuなど)
sudo apt install wget git libgl1 libglib2.0-0
```
```bash
# Arch系
sudo pacman -S wget git
```
2. 下記コマンドでPython3.11.16をインストール
```bash
# Debian系(Ubuntuなど)
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-venv
```
```bash
# Arch系
sudo pacman -S yay
yay -S python311
```
3. `webui-user.sh`の内容を下記に変更(#はコメント)
```bash
#!/bin/bash

# Pythonを3.11に設定
python_cmd="python3.11"

# Nvidia GPUがない場合は"--use-cpu all --precision full --no-half --skip-torch-cuda-test"を代入してハッシュタグを削除
#export COMMANDLINE_ARGS=""

# 詰み防止のため
export STABLE_DIFFUSION_REPO=https://github.com/w-e-w/stablediffusion.git
export CLIP_PACKAGE=git+https://github.com/openai/CLIP.git
```
4. `webui.sh`(起動ファイル)を実行
### モデル流用
Models内のStable-Diffusionに移動またはコピー(ただし本ソフトと同じモデルが自動ダウンロードされます)
## [ComfyUI](https://comfy.org/download) 
アプリ版ですが、ワークフローの知識が必要なため上級者向けです。
### モデル流用
Models内のdiffusion_modelsに移動またはコピー
## [FastSDCPU](https://github.com/rupeshs/fastsdcpu)
CPUだけで速く画像を生成でき、起動方法でGUIにもWebUIにもなります。アプリ自体の容量もダントツ少ないです。しかしPythonと[UV](https://docs.astral.sh/uv/)とStable Diffusionモデルの知識が必須なうえ、下記モジュールによってRAMが埋まるので上級者向けです。
### モデル流用
Huggingface Hubを利用しているので不可(設定からLCM LoRAモードをオンにしてベースモデルIDをrunwayml/stable-diffusion-v1-5を選択するとおそらく本ソフトと同じモデルを使用できます)
