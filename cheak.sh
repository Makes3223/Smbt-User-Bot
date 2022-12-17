if [[ -d "core_v1" ]] && [[ -f "main.py" ]] && [[ -d "moduls" ]]; then
  echo "all file are download"
else
  echo "Please download some files"  || exit 2
fi

if [[ -f "my_account.session" ]]; then
  echo "It seems that  is already installed. TO RUN TYPE 'python3 main.py' Exiting..."
elif echo "sorry the bot didn't install, please run 'python3 install.py'"; then
  exit 3
fi