
python -m venv env 
.\env\Scripts\activate

pip install numpy (as example)
python -m pip freeze > requirements.txt (open file to see)
pip uninstall numpy (uninstall to show installing from requirements.txt)
pip show numpy (to show numpy is gone)
python -m pip install -r .\requirements.txt
pip show numpy (to show numpy is installed)



python -m pip freeze > requirements.txt (open file to see)
python -m pip install -r .\requirements.txt

